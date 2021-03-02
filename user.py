import sqlalchemy as sa
from flask_restful import Api, Resource
import flask_marshmallow.schema
from flask import Flask, request
import uuid

#Define a schema for User - limit to just name and email

User = None

class Schema(flask_marshmallow.schema.Schema):
    class Meta:
        fields = ("name", "email", "is_admin")

def register_class(db):
    global User
    class User(db.Model):
        id = sa.Column('id', sa.Integer, sa.Sequence('user_id_seq'), primary_key=True, nullable=True)
        name = sa.Column(sa.String(20), nullable=False)
        email = sa.Column(sa.String(28), nullable=False)
        public_id = sa.Column(sa.String, nullable=False)
        is_admin = sa.Column(sa.Boolean, default=False)

        def __repr__(self):
            return f'User <{self.email}>'


def get_list_resource(db):
    users_schema = Schema(many=True)
    user_schema = Schema()

    class UserListResource(Resource):
        def get(self):
            users = User.query.all()
            return users_schema.dump(users)

        def post(self):
            new_user = User(
                name=request.json['name'],
                email=request.json['email'],
                public_id = str(uuid.uuid4())
            )
            db.session.add(new_user)
            db.session.commit()
            return user_schema.dump(new_user)
  
    return UserListResource

def get_resource(db):
    user_schema = Schema()
    
    class UserResource(Resource):
        def get(self, user_id):
            user = User.query.get_or_404(user_id)
            return user_schema.dump(user)

        def patch(self, user_id):
            post = Post.query.get_or_404(user_id)
            if 'name' in request.json:
                user.name = request.json['name']
            if 'email' in request.json:
                user.email = request.json['email'
            db.session.commit()
            return post_schema.dump(user)

        def delete(self, post_id):
            post = User.query.get_or_404(user_id)
            _db.session.delete(user)
            _db.session.commit()
            return '', 204

    return UserResource

