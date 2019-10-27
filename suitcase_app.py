from suitcase_web import suitcase_app, db
from suitcase_web.models import Word, Definitions

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Word': Word, 'Definition': Definitions}
