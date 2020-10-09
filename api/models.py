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

    def __repr__(self):
        return '{}'.format(self.name)

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return '{}'.format(self.name)
