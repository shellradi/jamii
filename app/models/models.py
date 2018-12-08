from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class  User(UserMixin,db.Model):

    __tablename__ = 'users'
    id  = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(20), nullable = False )
    email = db.Column(db.String(20), unique = True, nullable = False )
    password_hash = db.Column(db.String())


    def __repr__(self):
        return '<User {}>'.format(self.username)

    #set password to hash
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

        #checks if hashd password is same as provide
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
