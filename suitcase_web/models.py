from suitcase_web import db
from datetime import datetime

class Word(db.Model):
    id = id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(60), index=True)
    approval = db.Column(db.Boolean(1))
    definitions = db.relationship('Definitions', backref='word', lazy=True)

    def __repr__(self):
        return f'<Word: {self.word}>'

class Definitions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    word_id = db.Column(db.Integer, db.ForeignKey('word.id'))

    def __repr__(self):
        return '<Definition {}>'.format(self.body)