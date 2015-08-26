from bottle import TEMPLATE_PATH
from bottle import Bottle

from envutils import set_local_or_prod

VIEWS_PATH = set_local_or_prod('OPENSHIFT_REPO_DIR', 'wsgi/views', 'views')
STATIC_PATH = set_local_or_prod('OPENSHIFT_REPO_DIR', 'wsgi/static', 'static')
CONTENT_PATH = set_local_or_prod('OPENSHIFT_DATA_DIR', '.', '../data')

# This must be added in order to do correct path lookups for the views
if VIEWS_PATH not in TEMPLATE_PATH:
	TEMPLATE_PATH.append(VIEWS_PATH)

app = Bottle()

@app.route('/name/<name>')
def nameindex(name='Stranger'):
    return '<strong>Hello, %s!</strong>' % name
 
@app.route('/')
def index():
    return '<strong>Hello World!</strong>'
