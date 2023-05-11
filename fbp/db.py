import sqlite3, click
from flask import g, current_app

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
        ) 
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db=get_db()
    db.execute(
        'CREATE TABLE contacts (contact_id INTEGER PRIMARY KEY,\
	        first_name TEXT NOT NULL,\
                last_name TEXT NOT NULL,\
                    email TEXT NOT NULL UNIQUE,\
                        phone TEXT NOT NULL UNIQUE);')
    db.commit()

@click.command('init_db')
def init_db_command():
    init_db()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)