from flask_marshmallow import Marshmallow
from mongoengine import Document, StringField, IntField

from app import application

ma = Marshmallow(application)


class User(Document):
    email = StringField(max_length=30, unique=True)
    password = StringField()

    def log_login(self):
        from tasks.tasks import log_last_login
        log_last_login.delay(self.email)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('email', )


user_schema = UserSchema()
users_schema = UserSchema(many=True)
