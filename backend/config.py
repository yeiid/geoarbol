import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecreto")
    SQLALCHEMY_DATABASE_URI = "sqlite:///geoarbol.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
