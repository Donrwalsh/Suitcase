from suitcase_web import suitcase_app

@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"
