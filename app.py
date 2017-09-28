import os

from security import authenticate, identity
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ian'
api = Api(app)



jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

# class Student(Resource):
#     def get(self, name):
#         return {'student': name}
#
# api.add_resource(Student, '/student/<string:name>')

# call app.run only when app.py is called and not when it is imported by other files
if __name__ == '__main__':
    # importing it here because of circular imports
    from db import db
    db.init_app(app)
    app.run(port=5003, debug=True)
