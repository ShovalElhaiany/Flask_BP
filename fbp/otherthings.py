from flask import(
    Blueprint,
    g,
    redirect,
    render_template,
    request,
    url_for,
    flash
)

bp=Blueprint('bluethings', __name__)

@bp.route('/index')
def things():
    return 'list of blue things'