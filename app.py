from flask import Flask, jsonify, render_template
from tinydb import TinyDB
import random

app = Flask(__name__)
# epithets_db = TinyDB('epithets.json')
# vocabulary_db = TinyDB('vocabulary.json')

@app.route('/')
def generate_epithets():
    # random_epithets = random.choice(epithets_db.all())
    return jsonify({"epithets": []})

@app.route('/vocabulary')
def vocabulary():
    # random_vocabulary = random.choice(vocabulary_db.all())
    return jsonify({"vocabulary": {}})

if __name__ == "__main__":
    main()