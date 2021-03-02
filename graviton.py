from sqlalchemy import create_engine,Sequence
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow
import user
import uuid
import os

#https://gist.github.com/Babatunde13/81866103136d20090a6f5c17f5de336b
#https://github.com/rahmanfadhil/flask-rest-api

snf_password = os.getenv('SNOWFLAKE_PASSWORD')

conn = 'snowflake://{user}:{password}@{account}/{database}/{schema}'.format(
        user='adminuser',
        password=snf_password,
        account='uy60020.australia-east.azure',
        database = 'DQ',
        schema = 'app'
    )
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=conn
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'client_session_keep_alive': True})

db = SQLAlchemy(app)
#ma = Marshmallow(app)
api = Api(app)

user.register_class(db)

api.add_resource(user.get_list_resource(db), '/users')
api.add_resource(user.get_resource(db), '/users/<int:user_id>')

db.create_all()
