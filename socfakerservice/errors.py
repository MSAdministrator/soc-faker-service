from flask import render_template
from socfakerservice import app
from .words import funny_words
import random


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', funny_word=random.choice(funny_words)), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', funny_word=random.choice(funny_words)), 500