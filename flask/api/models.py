from api import db


class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    occupation = db.Column(db.String(64))
    description = db.Column(db.Text)
    org_id = db.Column(db.Integer, db.ForeignKey('organizations.id'))

    def __repr__(self):
        return '{}, {}'.format(self.name, self.occupation)

    @staticmethod
    def to_dict(c):
        return { 'name': c.name, 'occupation': c.occupation, 'description': c.description }

class Organization(db.Model):
    __tablename__ = 'organizations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    members = db.relationship('Character', backref='org', lazy='dynamic')
    pubs = db.relationship("OrgToPub", backref="orgs")

    def __repr__(self):
        return '{}'.format(self.name)

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return '{}'.format(self.name)

class Publication(db.Model):
    __tablename__ = 'publications'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    orgs = db.relationship("OrgToPub", backref="pubs")

    def __repr__(self):
        return '{}'.format(self.name)

class OrgToPub(db.Model):
    __tablename__ = 'org_to_pup'
    org_id = db.Column(db.Integer, db.ForeignKey('organizations.id'), primary_key=True)
    pub_id = db.Column(db.Integer, db.ForeignKey('publications.id'), primary_key=True)
    pages = db.Column(db.String(64))
    org = db.relationship("Organization", backref="org")
    pub = db.relationship("Publication", backref="pub")

