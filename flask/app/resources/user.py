import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument(
			'username',
			type=str,
			required=True,
			help='Truong nay khong the bo trong'
	)	
	parser.add_argument(
			'password',
			type=str,
			required=True,
			help='Truong nay khong the bo trong'
	)
	def post(self):
		data =  UserRegister.parser.parse_args();
		if UserModel.find_by_username(data['username']):
			return {"Mess":"Tai khoan da ton tai"},400
			
		user = UserModel(**data)
		user.save_to_db()
		return '{"Mess":" da tao user"}',201