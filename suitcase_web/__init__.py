from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

suitcase_app = Flask(__name__)
suitcase_app.config.from_object(Config)
db = SQLAlchemy(suitcase_app)
migrate = Migrate(suitcase_app, db)

from suitcase_web import routes, models
