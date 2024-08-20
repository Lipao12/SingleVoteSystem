class CandidateFinder:
    def __init__(self, candidate_repository) -> None:
        self.candidate_repository = candidate_repository

    def get_candidates(self, columns):
        try:
            if columns:
                candidates = self.candidate_repository.get_all_candidates(columns['columns'])
            else:
                candidates = self.candidate_repository.get_all_candidates([])
            return {
                "body":  candidates,
                "status_code": 201
                } 
        except Exception as exception:
            return{
                "body":{"error":"Bad Request", "message":str(exception)},
                "status_code":400
            }