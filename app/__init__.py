from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/main')

    from app.transactions import bp as transactions_bp
    app.register_blueprint(transactions_bp, url_prefix='/transactions')

    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    return app

from app import models