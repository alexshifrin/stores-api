from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    # no put endpoint because changing name changes everything about a store

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        #this is a tuple with message then status code
        #default is 200 which is what happens above
        return {'message': 'store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': f"store named '{name}' already exists"}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            # 500 means our error / internal server error not user fault
            return {'message': "an error occurred while creating store"}, 500

        # means we succeeded at saving to db
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'store deleted or doesn\'t exist'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
