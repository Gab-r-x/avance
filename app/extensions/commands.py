from app.extensions.sql_database import db


def create_db():
    """Creates database"""
    db.create_all()
    # mongo.init_app()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    pass


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))
