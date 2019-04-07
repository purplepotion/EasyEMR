from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# Association table
appointments = db.Table('appointments',
                        db.Column('employee_id', db.Integer, db.ForeignKey('user.employee_id')),
                        db.Column('patient_id', db.String, db.ForeignKey('patient.patient_id'))
                        )


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    clients = db.relationship('Patient', secondary=appointments, backref=db.backref('appointments', lazy='dynamic'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.employee_id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.String)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(16))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    prescription = db.Column(db.String(250))
    medications = db.Column(db.String(200))
    tests = db.Column(db.String(200))

    def __repr__(self):
        return '<Patient {}>'.format(self.name)



