from flask import render_template
from suitcase_web import suitcase_app

@suitcase_app.route('/')
@suitcase_app.route('/index')
def index():
	user = {'username': 'Miguel'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@suitcase_app.route('/two_words')
def two_words():
	form = two_words
	return return_template('two_words.html', title='Suitcase', form=form)