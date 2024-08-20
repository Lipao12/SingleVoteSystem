from flask import jsonify, Blueprint, request

vote_routes_bp = Blueprint("vote_routes", __name__)

# Imoportação de Controllers
from src.main.controllers.add_vote import AddVote

# Importação de Repositorios
from src.repositories.vote_repository import VoteRepository

# Importação o gerente de conexões
from src.settings.service.db_connection_handler import db_connection_handler

@vote_routes_bp.route("/vote", methods=["POST"])
def vote_candidate():
    conn = db_connection_handler.get_connection()
    vote_repository = VoteRepository(conn)
    controller = AddVote(vote_repository)

    response = controller.login(request.json)

    return jsonify(response['body']), response['status_code']
