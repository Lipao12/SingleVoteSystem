from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor

class CandidateRepository:
    def __init__(self, conn:connection) -> None:
        self.conn = conn

    def get_all_candidates(self, columns=None):
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        try:
            column_list = '*'
            if columns:
                column_list = ', '.join(columns)
            query = f'SELECT {column_list} FROM candidates'
            cursor.execute(query)
            result = cursor.fetchall()
            
            if not result:
                return {"error": "No candidates found", "status": 404}
            
            return result
        
        except Exception as e:
            return {"error": str(e), "status": 500}
        
        finally:
            cursor.close()
