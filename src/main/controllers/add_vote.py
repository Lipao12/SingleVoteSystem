class AddVote:
    def __init__(self, vote_repository) -> None:
        self.vote_repository = vote_repository

    def vote(self, candidateId):
        print(candidateId)
        try:
            self.vote_repository.validation_vote(candidateId['candidateId'])
            return {
                "body":  candidateId,
                "status_code": 201
                } 
        except Exception as exception:
            return{
                "body":{"error":"Bad Request - Vote Candidate", "message":str(exception)},
                "status_code":400
            }