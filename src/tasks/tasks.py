from datetime import datetime

from app import celery
from models import User
from models.user_last_login import UserLastLogin


@celery.task
def log_last_login(email):
    user = User.objects(email=email).first()
    if not user:
        return

    is_returning_user = UserLastLogin.objects(user=user).first()

    if is_returning_user:
        is_returning_user.datetime = datetime.now()
        is_returning_user.save()
    else:
        UserLastLogin.objects(user=user, datetime=datetime.now()).save()
