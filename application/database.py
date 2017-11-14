import sqlite3

from flask import g

from application import app


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


def query_db(query, one=False, commit=False):
    print("database query    ", query)
    cur = g.db.execute(query)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    if commit == True:
        g.db.commit()
    res = (rv[0] if rv else None) if one else rv
    print(res)
    return res


def getNextId(xid, db):
    lid = query_db("select %s from %s order by %s DESC limit 1;" %
                   (xid, db, xid))
    print("lid", lid)

    if len(lid) == 0:
        return '1'
    return (str)((int)(lid[0][xid]) + 1)
