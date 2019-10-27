from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class word_input(FlaskForm):
    word_one = StringField('First Word', validators=[DataRequired()])
    word_two = StringField('Second Word', validators=[DataRequired()])
    submit = SubmitField('Sign In')