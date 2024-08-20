from psycopg2.extensions import connection

class CandidateRepository:
    def __init__(self, conn:connection) -> None:
        self.conn = conn

    def get_all_candidates(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                '''
                SELECT * FROM candidates
                '''
            )
            result = cursor.fetchall()
            
            if not result:
                return {"error": "No candidates found", "status": 404}
            
            print("resultado: ", result)
            
            return result
        
        except Exception as e:
            return {"error": str(e), "status": 500}
        
        finally:
            cursor.close()
