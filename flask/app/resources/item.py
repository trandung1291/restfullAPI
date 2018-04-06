import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument(
			'price',
			type=float,
			required=True,
			help='Truong nay khong the bo trong'
	)
	parser.add_argument(
			'store_id',
			type=int,
			required=True,
			help='Truong store id nay khong the bo trong'
	)
	@jwt_required()
	def get(self,name):
		item = ItemModel.find_by_name(name)
		if item:
			return item.json()
		return {"Mess":"Khong tim thay item"},404
	
	def post(self,name):
		if ItemModel.find_by_name(name):
			return {'mess': "mot item ten la '{}'".format(name)},404
		data = Item.parser.parse_args()
		item = ItemModel(name ,data['price'],data['store_id'])
		
		try:
			item.save_to_db()
		except:
			return {"Mess":"khong insert dc item"},500
		return item.json(),201
		

		
	def delete(self,name):
		item = ItemModel.find_by_name(name)
		if item is None:
			return {'mess': "ko co item"},404
		item.delete_from_db()
		return {'Mess': 'item deleted'}
	
	def put(self,name):
		data = Item.parser.parse_args()
		item = ItemModel.find_by_name(name)
		if item is None:
			item = ItemModel(name,data['price'],data['store_id'])
		else:
			item.price = data['price']
		item.save_to_db()
		return item.json()

class ItemList(Resource):
	def get(self):
		return {'lists':list(map(lambda x: x.json(),ItemModel.query.all()))}
