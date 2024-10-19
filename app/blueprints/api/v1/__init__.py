from flask import Blueprint
from flask_restful import Api

from .user_resources import SingupResource, LoginResource, RefreshResource, ProtectedResource

bp = Blueprint('restapi', __name__, url_prefix='/api/v1')
api = Api(bp)

def init_app(app):
    api.add_resource(SingupResource, "/singup/")
    api.add_resource(LoginResource, "/login/")
    api.add_resource(RefreshResource, "/refresh/")
    api.add_resource(ProtectedResource, "/protected/")
    
    app.register_blueprint(bp)