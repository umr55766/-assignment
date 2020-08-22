from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email, password):
    from models import User
    user = User.objects(email=email).first()

    if not user:
        return False

    return check_password_hash(user.password, password)
