from psycopg2.extensions import connection

class VoteRepository:
    def __init__(self, conn:connection) -> None:
        self.conn = conn

    def validation_vote(self, candidateId):
        print(candidateId)
        def verify_IP(personIP="0000"):
            return True
        
        valid = verify_IP()
        if not valid:
            return {"error":"Already voted", "status":400}
        
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                '''
                SELECT vote_qnt FROM candidates WHERE id = %s
                ''', (candidateId,)
            )
            result = cursor.fetchone()

            if result is None:
                return {"error": "Candidate does not exist", "status": 400}

            cursor.execute(
                '''
                UPDATE candidates 
                SET vote_qnt = vote_qnt + 1
                WHERE id = %s
                ''', (candidateId,)
            )

            self.conn.commit()
            return {"message": "Vote recorded successfully", "status": 200}
        
        except Exception as e:
            print(f"Error: {e}")
            return {"error": "Internal server error", "status": 500}
        
        finally:
            cursor.close()
