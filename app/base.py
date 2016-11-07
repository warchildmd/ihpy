# Import flask and template operators
from flask import Flask
from flask.json import JSONEncoder
import flask.json as json

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)


class ObjectJSONEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, db.Model):
            obj = obj.__dict__
        return super(MyJSONEncoder, self).default(obj)


class AlchemyEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, db.Model):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj)
                          if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    # this will fail on non-encodable values, like other
                    # classes
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return JSONEncoder.default(self, obj)


app.json_encoder = AlchemyEncoder

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
