from flask import Flask, jsonify, render_template
from dotenv import load_dotenv

import os

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

app = Flask(__name__)

@app.route('/')
def generate_epithets():
    return jsonify({"epithets": []})

@app.route('/vocabulary')
def vocabulary():
    return jsonify({"vocabulary": {}})