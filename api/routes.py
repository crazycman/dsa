from api import app
from flask import Blueprint, jsonify

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"

main = Blueprint('main', __name__)

@main.route('/add_org', methods=['POST'])
def add_movie():
    return 'DONE', 201

@main.route('/orgs')
def movies():
    orgs = []
    return jsonify({'orgs' : orgs})

