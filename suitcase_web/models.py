from suitcase_web import db

class Word(db.Model):
    word = db.Column(db.String(60), index=True, primary_key=True)
    definition = db.Column(db.String(120), index=True)
    approval = db.Column(db.Boolean(1))

    def __repr__(self):
        return f'<Word: {self.word}>'