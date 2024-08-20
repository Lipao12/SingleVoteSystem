from psycopg2.extensions import connection

class CandidateRepository:
    def __init__(self, conn:connection) -> None:
        self.conn = conn

    def get_all_candidates(self, columns=None):
        print("Dentro", )
        cursor = self.conn.cursor()
        try:
            column_list = '*'
            if columns:
                column_list = ', '.join(columns)
            print("Lista: ", column_list)
            query = f'SELECT {column_list} FROM candidates'
            cursor.execute(query)
            result = cursor.fetchall()
            
            if not result:
                return {"error": "No candidates found", "status": 404}
            
            print("resultado: ", result)
            
            return result
        
        except Exception as e:
            return {"error": str(e), "status": 500}
        
        finally:
            cursor.close()
