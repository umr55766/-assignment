from datetime import datetime

from mongoengine import Document, DateTimeField, ReferenceField

from models import User


class UserLastLogin(Document):
    datetime = DateTimeField(required=True, default=datetime.now())
    user = ReferenceField(User, required=True, unique=True)
