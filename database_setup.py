from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        data = pd.read_csv('test.csv')
        for i in range(len(data)):
            product = Product(name=data['name'][i], description=data['description'][i], price=data['price'][i], quantity=data['quantity'][i])
            db.session.add(product)
        db.session.commit()