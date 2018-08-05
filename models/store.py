from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # lazy='dynamic' means items isn't created every time store is made
    # could turn into a costly computational endeavor
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        # added .all() because of lazy='dynamic' parameter on relationship
        # turns self.items into query builder
        # trade off is that .all() when calling json means we go into table vs. computed up-front
        return {'store_id': self.id, 'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self): #up-serting = updating or inserting
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
