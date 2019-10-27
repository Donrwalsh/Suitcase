from flask import flask

suitcase_app = Flask(__name__)

from app import routes
