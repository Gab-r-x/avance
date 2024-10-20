import click
from app.extensions.sql_database import db
from app.extensions.nosql_database import mongo
from app.models.questions import Question


def create_db():
    """Creates database"""
    db.create_all()
    # mongo.init_app()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    # data = [
    #     Product(
    #         id=1, name="Ciabatta", price="10", description="Italian Bread"
    #     ),
    #     Product(id=2, name="Baguete", price="15", description="French Bread"),
    #     Product(id=3, name="Pretzel", price="20", description="German Bread"),
    # ]
    # db.session.bulk_save_objects(data)
    # db.session.commit()
    # return Product.query.all()
    pass

def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))