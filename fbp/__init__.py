from flask import Flask, current_app, g
import sqlite3
import os

def create_app(test_config=None):
    app=Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskbp.sqlite'),
        )
    
    # if test_config is None:
    #     app.config.from_file('config.py')
    # else:
    #     app.config.from_file('test_config.py')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return 'index'
    
    from . import db
    db.init_app(app)
    # with app.app_context():
    #     db.init_db()
    from . import things, otherthings
    app.register_blueprint(things.bp, url_prefix = '/redthings')
    app.register_blueprint(otherthings.bp, url_prefix = '/bluethings')


    return app