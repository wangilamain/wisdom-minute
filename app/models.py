from app import db
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50), unique=True, index=True)
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String())
    pitches = db.relationship('Comments', backref='user', lazy=True)
    comments = db.relationship('Pitch', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'{self}'

class Pitch(db.Model):
    __tablename__ ='pitches'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String())
    category = db.Column(db.String())
    content = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    @classmethod
    def get_pitches(cls):
        return Pitch.query.all()

    @classmethod
    def get_pitch(cls,pitch_id):
        return Pitch.query.filter_by(id=pitch_id).first()

    @classmethod
    def get_user_pitches(cls,user_id):
        return Pitch.query.filter_by(user_id=user_id).all()
        # pitches = Pitch.get_user_pitches(current_user.id)

class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.String()) 
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @classmethod
    def get_comments(cls,id):
        return Comments.query.filter_by(pitch_id=id)

class Reactions(db.Model):
    __tablename__='reactions'
    id = db.Column(db.Integer,primary_key=True)
    reaction = db.Column(db.String(10))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

