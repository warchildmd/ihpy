# Boostrap Application and Database
from app.base import app, db

# Import a module / component using its blueprint handler variable (mod_auth)
from app.modules.auth.controllers import auth_blueprint as auth_module
# from app.modules.auth.models import User

# Import password / encryption helper tools
# from werkzeug import check_password_hash, generate_password_hash

# Register blueprint(s)
app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

# admin =
# User('admin', 'mihail@burduja.com', generate_password_hash('password'))

# db.session.add(admin)
# db.session.commit()
