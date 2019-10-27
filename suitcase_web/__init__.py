from flask import Flask

suitcase_app = Flask(__name__)

from suitcase_web import routes
