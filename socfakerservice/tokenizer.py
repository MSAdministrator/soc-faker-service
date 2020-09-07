import os
from mongoengine import connect, disconnect
from .config import Config


class Tokenizer(object):

    __config = Config()

    
    def connect(self):
        self.client = connect(
            self.__config.MONGO_INITDB_DATABASE,
            username=self.__config.MONGO_INITDB_ROOT_USERNAME,
            password=self.__config.MONGO_INITDB_ROOT_PASSWORD,
            authentication_source='admin',
            host=self.__config.MONGO_INITDB_HOST,
            port=int(self.__config.MONGO_INITDB_PORT)
        )

    def disconnect(self):
        disconnect(self.__config.MONGO_INITDB_DATABASE)
