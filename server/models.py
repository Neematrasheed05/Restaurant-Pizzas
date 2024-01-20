from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(256))

    pizzas = db.Relationship('Pizza', secondary='restaurant_pizzas')
    
class Pizza(db.Model):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients=db.Column(db.String(256))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    restaurants = db.Relationship('Restaurant', secondary='restaurant_pizzas')

class RestaurantPizza(db.Model):
    __tablename__='restaurant_pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    
    restaurant = db.relationship('Restaurant', backref=db.backref('restaurant_pizzas'))
    pizza = db.relationship('Pizza', backref=db.backref('restaurant_pizzas'))



# You need to create the following relationships:
# - A `Restaurant` has many `Pizza`s through `RestaurantPizza`
# - A `Pizza` has many `Restaurant`s through `RestaurantPizza`
# - A `RestaurantPizza` belongs to a `Restaurant` and belongs to a `Pizza`
# add any models you may need. 