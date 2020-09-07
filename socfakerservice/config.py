import os, hashlib
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', str(hashlib.sha512().hexdigest))
    SESSION_TYPE = os.environ.get('SESSION_TYPE', 'filesystem')
    MONGO_INITDB_HOST = os.environ.get('MONGO_INITDB_HOST', 'tokenizer')
    MONGO_INITDB_DATABASE = os.environ.get('MONGO_INITDB_DATABASE', 'tokenizer')
    MONGO_INITDB_PORT = os.environ.get('MONGO_INITDB_PORT', 27017)
    MONGO_INITDB_ROOT_USERNAME = os.environ.get('MONGO_INITDB_ROOT_USERNAME', 'root')
    MONGO_INITDB_ROOT_PASSWORD = os.environ.get('MONGO_INITDB_ROOT_PASSWORD', 'password')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', True)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')