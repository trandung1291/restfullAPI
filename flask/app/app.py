from flask import Flask,request
from flask_restful import Resource,Api
from flask_jwt import JWT

from security import authenticate,identity
from resources.item import Item,ItemList
from resources.store import Store,StoreList
from resources.user import UserRegister

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key = 'dung'
api = Api(app)


jwt = JWT(app,authenticate,identity) #/auth

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')

if __name__=='__main__':
	from database import db
	db.init_app(app)
	app.run(port=4996)