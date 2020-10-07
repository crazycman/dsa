from api import app, db
from api.models import Character, Organization

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Character': Character, 'Organization': Organization}
