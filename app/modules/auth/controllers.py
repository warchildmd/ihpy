# Import flask dependencies
from flask import Blueprint, request, abort, jsonify

import config

# Import JWT related stuff
import jwt

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db

# Import module models (i.e. User)
from app.modules.auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')


# Set the route and accepted methods
@auth_blueprint.route('/signin', methods=['POST'])
def authenticate():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)  # missing arguments
    user = User.query.filter_by(name=username).first()
    if user and check_password_hash(user.password, password):
        # Create JWT and return
        user.password = 'private'
        payload = {'user': {'name': user.name}}
        encoded = jwt.encode(payload,
                             config.SECRET_KEY, algorithm='HS256')
        return jsonify({'access_token': encoded.decode("utf-8")})
    abort(400)
