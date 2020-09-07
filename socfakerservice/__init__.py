from flask import Flask 
from flask_session import Session
from flask_mail import Mail
from flask_api import FlaskAPI, status, exceptions
from flask_api.renderers import HTMLRenderer
from flask_api.decorators import set_renderers
from flask_bootstrap import Bootstrap
from .config import Config
from .frontend.nav import nav


app = FlaskAPI(__name__)

app.config.from_object(Config)
mail = Mail(app)
Bootstrap(app)

from .base import app

from .frontend.frontend import general_bp
app.register_blueprint(general_bp, url_prefix='/')

from .api.api import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

Session(app)

from socfakerservice import errors
