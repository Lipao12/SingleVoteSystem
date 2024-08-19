from psycopg2.extensions import connection

class VoteRepository:
    def __init__(self, conn:connection) -> None:
        self.conn = conn

    def validation_vote(self, candidateId):
        def verify_IP(personIP):
            pass
        
        valid = verify_IP()
        if not valid:
            return {"error":"Already voted", "status":400}

        cursor = self.conn.cursor()
        cursor.execute(
            '''
            SELECT vote_qnt FROM candidates WHERE id = %s
            ''', (candidateId,)
        )

        qnt_votes = cursor.fetchone()[0] + 1

        cursor.execute(
            '''
            UPDATE candidates 
            SET vote_qnt = %s   
            WHERE id = %s
            ''', (qnt_votes, candidateId,)
        )

        self.conn.commit()
