from flask import request, jsonify
from flask_restx import Namespace, Resource, abort

from project.setup_db import db

from project.services import UsersService

from project.services import auth_service

auth_ns = Namespace("auth")

@auth_ns.route("/register")
class RegisterView(Resource):
    def post(self):
        if not request.json:
            abort(400, "Bad request")
        new_user_data = request.json
        print(new_user_data)
        UsersService(db.session).create(new_user_data)
        return f"Created user"


@auth_ns.route("/login")
class LoginView(Resource):
    def post(self):
        if not request.json:
            abort(400, "Bad request")
        user_data = request.json

        # email = user_data.get("email")
        # password = user_data.get("password")
        #
        # if None in [email, password]:
        #     abort(400, "")

        # tokens = auth_service.get_tokens(email, password)
        tokens = auth_service.get_tokens(user_data)


        print(f"Tokens {tokens}")

        return jsonify(tokens)

    def put(self):
        data = request.json

        tokens = auth_service.get_refresh_tokens(data)

        print(f"Tokens regreshed: {tokens}")

        return tokens








