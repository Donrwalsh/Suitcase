from suitcase_web import suitcase_app

@suitcase_app.route('/')
@suitcase_app.route('/index')
def index():
	return "Hello, World!"
