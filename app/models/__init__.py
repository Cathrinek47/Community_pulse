#app/models/__init__.py
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

db = SQLAlchemy()

from app.models.responses import *
from app.models.questions import *
