from datetime import datetime
from faker import Faker
from models import db, Restaurant, Pizza, RestaurantPizza
from app import app

fake = Faker()

def seed_restaurants():
    restaurants_data = [
        {"name": fake.company(), "address": fake.address()} for _ in range(5)
    ]

    for restaurant_info in restaurants_data:
        restaurant = Restaurant(**restaurant_info)
        db.session.add(restaurant)

def seed_pizzas():
    pizzas_data = [
        {"name": fake.word(), "ingredients": fake.text()[:50]} for _ in range(10)
    ]

    for pizza_info in pizzas_data:
        pizza = Pizza(**pizza_info, created_at=datetime.now(), updated_at=datetime.now())
        db.session.add(pizza)

def seed_restaurant_pizzas():
    restaurants = Restaurant.query.all()

    for restaurant in restaurants:
        for _ in range(1, 4):
            pizza = Pizza.query.order_by(db.func.random()).first()
            restaurant_pizza = RestaurantPizza(
                restaurant_id=restaurant.id,
                pizza_id=pizza.id,
                price=fake.random_int(min=5, max=20),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            db.session.add(restaurant_pizza)
            db.session.commit()

def seed_data():
    seed_restaurants()
    seed_pizzas()
    seed_restaurant_pizzas()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding started -----")
        seed_data()
        print("Seeded successfully")
