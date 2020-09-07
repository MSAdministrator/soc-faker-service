import pendulum
from mongoengine import Document, StringField, DateTimeField, IntField
from .tokenizer import Tokenizer

Tokenizer().connect()


class TokenModel(Document):
    email = StringField(required=True, unique=True)
    token = StringField(required=True, unique=True)
    first_request_date = DateTimeField(default=pendulum.now(), required=True)
    last_request_date = DateTimeField(default=pendulum.now())

    def __repr__(self):
        return '<Token {}>'.format(self.token) 

