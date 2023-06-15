from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class PaymentGateway(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    api_url = db.Column(db.String(200), nullable=False)
    # additional fields can be added for unique requirements of each gateway

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    payment_gateway_id = db.Column(db.Integer, db.ForeignKey('payment_gateway.id'), nullable=False)
    transaction_limit = db.Column(db.Integer, nullable=False)
    current_transaction_count = db.Column(db.Integer, default=0)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(10), default='PENDING')
    error_message = db.Column(db.String(500))
