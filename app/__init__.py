# app/__init__.py
from flask import Flask
from app.routes.questions import questions_bp
from app.routes.responses import responses_bp
from config import DevelopmentConfig
from app.models import db

from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    app.register_blueprint(questions_bp)
    app.register_blueprint(responses_bp)
    migrate = Migrate()
    migrate.init_app(app, db)
    return app

