from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, ItemList
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'ian'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# class Student(Resource):
#     def get(self, name):
#         return {'student': name}
#
# api.add_resource(Student, '/student/<string:name>')

# call app.run only when app.py is called and not when it is imported by other files
if __name__ == '__main__':
    app.run(port=5003, debug=True)
