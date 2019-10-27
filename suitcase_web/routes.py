from flask import render_template
from suitcase_web import suitcase_app
from suitcase_web.word_input import word_input

@suitcase_app.route('/')
@suitcase_app.route('/two_words')
def two_words():
	form = word_input()
	return render_template('two_words.html', title='Suitcase', form=form)