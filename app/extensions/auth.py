import jwt
from flask import current_app, request, jsonify
from datetime import datetime, timedelta, UTC, timezone
from functools import wraps

def create_jwt_token(user_id):
    expiration = datetime.now() + timedelta(hours=1)
    token = jwt.encode({
        'user_id': user_id,
        'exp': expiration
    }, current_app.config['SECRET_KEY'], algorithm='HS256')
    return token

def verify_jwt_token(token):
    try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return data['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token:
            token = token.split(" ")[1]  # Remove 'Bearer' of token
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        user_id = verify_jwt_token(token)
        if not user_id:
            return jsonify({'message': 'Invalid token!'}), 401
        return f(user_id, *args, **kwargs)
    return decorated_function
