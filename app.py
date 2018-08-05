import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
#SQLAlchemy creates tables when StoreModel and ItemModel are imported (via resource.store/item)

app = Flask(__name__)
# the db URI could point to a sqlite, postgre, oracle or whatever db you want
# if DATABASE_URL isn't found on Heroku version then default SQLite url is used for local testing
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'topchekeret'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
