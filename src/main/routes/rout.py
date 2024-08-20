from flask import jsonify, Blueprint, request

vote_routes_bp = Blueprint("vote_routes", __name__)

# Imoportação de Controllers
from src.main.controllers.add_vote import AddVote
from src.main.controllers.candidate_finder import CandidateFinder

# Importação de Repositorios
from src.repositories.vote_repository import VoteRepository
from src.repositories.candidate_repository import CandidateRepository

# Importação o gerente de conexões
from src.settings.service.db_connection_handler import db_connection_handler

@vote_routes_bp.route("/vote", methods=["POST"])
def vote_candidate():
    conn = db_connection_handler.get_connection()
    print(db_connection_handler)
    vote_repository = VoteRepository(conn)
    controller = AddVote(vote_repository)

    response = controller.vote(request.json, request.remote_addr)

    return jsonify(response['body']), response['status_code']

@vote_routes_bp.route("/candidates", methods=["GET"])
def get_candidates():
    conn = db_connection_handler.get_connection()
    vote_repository = CandidateRepository(conn)
    controller = CandidateFinder(vote_repository)


    response = controller.get_candidates(request.json)


    return jsonify(response['body']), response['status_code']
