from suitcase_app import suitcase_app

@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"
