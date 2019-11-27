from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

from . import login_manager
from . import db


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    full_name = db.Column(db.String)
    email = db.Column(db.String)
    pass_word = db.Column(db.String)


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_word = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_word,password)

    def __repr__(self):
        return f'User {self.username}'


class ClassName(object):
    """docstring for ."""

    def __init__(self, arg):
        pass
