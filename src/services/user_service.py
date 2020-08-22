from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash, generate_password_hash

from models import User


class UserService(object):
    """
    service function for user related business logic
    """
    data = None
    user = None

    def __init__(self, data=None, user=None):
        self.data = data
        self.user = user

    def validate_payload(self):
        if not self.data:
            raise BadRequest({"Error": "Email & Password are required"})

        if "email" not in self.data:
            raise BadRequest({"Error": "Email is required"})

        if "password" not in self.data:
            raise BadRequest({"Error": "Password is required"})

    def login_user(self):
        self.validate_payload()

        self.user = User.objects(email=self.data["email"]).first()

        if not self.user:
            raise BadRequest({"Error": "Email not registered"})

        if not check_password_hash(self.user['password'], self.data["password"]):
            raise BadRequest({"Error": "Wrong Password"})

        self.user.log_login()

        return self.user

    def register_user(self):
        self.validate_payload()

        if User.objects(email=self.data["email"]).first():
            raise BadRequest({"Error": "Email already exists"})

        return User(self.data["email"], generate_password_hash(self.data["password"])).save()
