from api import app, db
from api.models import Organization, Character
from flask import Blueprint, jsonify, request

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"

main = Blueprint('main', __name__)

@main.route('/add_org', methods=['POST'])
def add_movie():
    org_data = request.get_json()
    org = Organization(name=org_data['name'])
    db.session.add(org)
    db.session.commit()
    return 'DONE adding \'{}\''.format(org.name), 201

@main.route('/orgs')
def movies():
    org_list = Organization.query.all()
    orgs = []
    for org in org_list:
        # orgs.append({ 'name': org.name, 'members': list(map(Character.to_dict, org.members)) })
        orgs.append({ 'name': org.name,
                      'members': list(map(lambda x: x.name, org.members)) })
    return jsonify({ 'orgs' : orgs })

