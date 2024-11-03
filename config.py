import os

class Config:
    SECRET_KEY = ''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///photo_album.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
