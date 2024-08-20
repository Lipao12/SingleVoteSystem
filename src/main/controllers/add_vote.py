class AddVote:
    def __init__(self, vote_repository) -> None:
        self.vote_repository = vote_repository

    def vote(self, candidateId, IP):
        try:
            response = self.vote_repository.validation_vote(candidateId['candidateId'], IP)

            if response['status_code'] == 400:
                return {
                    "body": response,
                    "status_code": 400
                    }
            if response['status_code'] == 500:
                return {
                    "body": response,
                    "status_code": 500
                    }
            
            return {
                "body":  response,
                "status_code": 201
                } 
        except Exception as exception:
            return{
                "body":{"error":"Bad Request - Vote Candidate", "message":str(exception)},
                "status_code":400
            }