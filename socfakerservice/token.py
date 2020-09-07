from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class Token(FlaskForm):
    email = StringField(label='Email Address',validators=[DataRequired(), Email(message='Please provide a valid email address')])
    submit = SubmitField(label='Get Token')