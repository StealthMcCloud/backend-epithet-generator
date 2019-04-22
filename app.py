from flask import Flask, jsonify
from dotenv import load_dotenv
from .helpers import Vocabulary, EpithetGenerator

import os
import random

app = Flask(__name__)
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
FLASK_APP = os.environ.get("FLASK_APP")
FLASK_ENV = os.environ.get("FLASK_ENV")

e_gen = EpithetGenerator()


@app.route('/')
def index():
    random_epithet = e_gen.get_epithets(1)
    dict_ = {"epithets": random_epithet}
    return jsonify(dict_)


@app.route('/vocabulary')
def vocabulary():
    dict_ = {"vocabulary": e_gen.vocab}
    return jsonify(dict_)


@app.route('/epithets/<qty>')
def epithets(qty):
    epithets = e_gen.get_epithets(int(qty))
    dict_ = {"epithets": epithets}
    return jsonify(dict_)


@app.route('/epithets/random')
def random_epithets():
    epithets = e_gen.get_random_epithets()
    dict_ = {"epithets": epithets}
    return jsonify(dict_)
    