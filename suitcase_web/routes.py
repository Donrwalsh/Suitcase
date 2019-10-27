from flask import render_template
from suitcase_web import suitcase_app

@suitcase_app.route('/')
@suitcase_app.route('/index')
def index():
	user = {'username': 'Miguel'}
	return render_template('index.html', title='Home', user=user)
