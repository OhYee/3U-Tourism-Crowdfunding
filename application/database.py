import sqlite3

from flask import g

from application import app
from application.file import readFromFile


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = connect_db()
    print("database connected")


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
    print("database closed")


def query_db(query, args=(), one=False, commit=False):
    print("database query", query)
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    if commit == True:
        g.db.commit()
    return (rv[0] if rv else None) if one else rv


def init_db():
    c = connect_db().cursor()
    c.execute(readFromFile('init.sql'))
    c.commit()
