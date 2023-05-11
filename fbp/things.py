from flask import(
    Blueprint,
    g,
    redirect,
    render_template,
    request,
    url_for,
    flash
)
from fbp.db import get_db

bp=Blueprint('redthings', __name__)

@bp.route('/index')
def things():
    db = get_db()
    return 'list of red things'