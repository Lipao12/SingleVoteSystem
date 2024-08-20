from psycopg2.extensions import connection

class VoteRepository:
    def __init__(self, conn:connection) -> None:
        self.conn = conn

    def verify_IP(self, personIP: str) -> bool:
        with self.conn.cursor() as cursor:
            cursor.execute(
                '''
                SELECT 1 FROM computerIP 
                WHERE ip = %s
                ''', (personIP,)
            )
            result = cursor.fetchone()
            return result is None

    def validation_vote(self, candidateId:str, IP:str):
        
        if not self.verify_IP(IP):
            return {"error": "IP already voted", "status_code": 400}
        
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                '''
                SELECT vote_qnt FROM candidates WHERE id = %s
                ''', (candidateId,)
            )
            result = cursor.fetchone()

            if result is None:
                return {"error": "Candidate does not exist", "status_code": 400}

            cursor.execute(
                '''
                INSERT INTO computerIP (ip) VALUES (%s);
                ''', (IP,)
            )

            cursor.execute(
                '''
                UPDATE candidates 
                SET vote_qnt = vote_qnt + 1
                WHERE id = %s
                ''', (candidateId,)
            )

            self.conn.commit()
            return {"message": "Vote recorded successfully", "candidateId": candidateId, "status_code": 200}
        
        except Exception as e:
            print(f"Error: {e}")
            return {"error": "Internal server error", "status_code": 500}
        
        finally:
            cursor.close()
