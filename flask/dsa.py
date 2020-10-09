from api import app, db
from api.models import Character, Organization, Publication, Location, OrgToPub

@app.shell_context_processor
def make_shell_context():
    return { 'db': db,
             'Character': Character,
             'Organization': Organization,
             'Publication' : Publication,
             'Location' : Location,
             'OrgToPub' : OrgToPub }
