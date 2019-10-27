from suitcase_web import suitcase_app, db
from suitcase_web.models import Word, Definitions

@suitcase_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Word': Word, 'Definition': Definitions}
