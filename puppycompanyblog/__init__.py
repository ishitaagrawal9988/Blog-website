import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_login import LoginManager


app=Flask(__name__)
login_manager=LoginManager()
app.config['SECRET_KEY'] = 'mysecret'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#rest api
api=Api(app)

login_manager.init_app(app)
login_manager.login_view='users.login'

from puppycompanyblog.core.views import core
from puppycompanyblog.users.views import users
from puppycompanyblog.blog_posts.views import blog_posts
from puppycompanyblog.error_pages.handlers import error_pages
from puppycompanyblog.models import User,BlogPost


app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)

#rest
class AllNames(Resource):
    #@jwt_required()
    def get(self):
        users=User.query.all()
        return [user.json() for user in users]

class AllNamesPost(Resource):
    #@jwt_required()
    def get(self):
        posts=BlogPost.query.all()
        return [post.json() for post in posts]

api.add_resource(AllNames,'/users')
api.add_resource(AllNamesPost,'/posts')
