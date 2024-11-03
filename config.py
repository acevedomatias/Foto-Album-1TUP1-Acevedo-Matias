import os

class Config:
    SECRET_KEY = 'tu_secreto_aqui'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///photo_album.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
