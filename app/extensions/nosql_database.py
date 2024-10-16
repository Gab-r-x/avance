from flask_pymongo import PyMongo

mongo = PyMongo()

def init_app(app):
    # Configure MongoDB with app configurations
    mongo.init_app(app)
