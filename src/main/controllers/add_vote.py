class AddVote:
    def __init__(self, vote_repository) -> None:
        self.vote_repository = vote_repository

    def vote(self, candidateId):
        try:
            self.vote_repository.validation_vote(candidateId)
            return {
                "body": {"canditateId": candidateId, },
                "status_code": 201
                } 
        except Exception as exception:
            return{
                "body":{"error":"Bad Request", "message":str(exception)},
                "status_code":400
            }