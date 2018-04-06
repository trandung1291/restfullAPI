from flask_restful import Resource,reqparse
from models.store import StoreModel

class Store(Resource):
	def get(self,name):
		store = StoreModel.find_by_name(name)
		if store:
			return store.json()
		return {'Mess':'khong tim thay store'},404
	def post(self,name):
		if StoreModel.find_by_name(name):
			return {'mess': "mot store ten la '{}'".format(name)},404
		store = StoreModel(name)
		
		try:
			store.save_to_db()
		except:
			return {"Mess":"khong insert dc store"},500
		return store.json(),201
	
	def delete(self,name):
		store = StoreModel.find_by_name(name)
		if store is None:
			return {'mess': "ko co store"},404
		store.delete_from_db()
		return {'Mess': 'store deleted'}

class StoreList(Resource):
	def get(self):
		return {'lists':list(map(lambda x: x.json(),StoreModel.query.all()))}
