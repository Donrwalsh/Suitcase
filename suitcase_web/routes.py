from flask import render_template, url_for
from werkzeug.utils import redirect
from suitcase_web import suitcase_app, db
from suitcase_web.forms import word_input
from suitcase_web.models import Word, Definitions
from flask import request
from werkzeug.urls import url_parse


@suitcase_app.route('/')
@suitcase_app.route('/two_words', methods=['GET','POST'])
def two_words():
	form = word_input()
	if form.validate_on_submit():
		word1 = Word(word=form.word_one.data)
		word2 = Word(word=form.word_two.data)
		db.session.add(word1)
		db.session.add(word2)
		db.session.commit()
		return redirect(url_for('/two_words'))
	return render_template('two_words.html', title='Suitcase', form=form)