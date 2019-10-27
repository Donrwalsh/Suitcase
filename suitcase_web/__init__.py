from flask import Flask
from config import Config

suitcase_app = Flask(__name__)
suitcase_app.config.from_object(Config)

from suitcase_web import routes
