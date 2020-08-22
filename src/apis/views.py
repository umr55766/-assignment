import base64
import logging

from flask import request, jsonify

from models import User
from models.user import users_schema
from services import UserService
from utils.auth import auth

logger = logging.getLogger("default")


def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"


def login():
    data = request.get_json()
    user_service = UserService(data)
    user_service.login_user()
    return (
        jsonify({"Token": base64.b64encode(("%s:%s" % (data["email"], data["password"])).encode()).decode("utf-8")}),
        200
    )


def register():
    data = request.get_json()
    user_service = UserService(data)
    user_service.register_user()
    return (
        jsonify({"Token": base64.b64encode(("%s:%s" % (data["email"], data["password"])).encode()).decode("utf-8")}),
        201
    )


@auth.login_required
def users():
    all_users = User.objects().all()
    result = users_schema.dump(all_users)
    return jsonify(result)
