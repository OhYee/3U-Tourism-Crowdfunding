from flask import g

from application import app

import application.database as db


def register(username, password):
    if len(db.query_db("select * from user where username='%s';" % (username))) == 0:
        db.query_db("insert into user(uid,username,password) values('%s','%s','%s');" % (
                    db.getNextId('uid', 'user'), username, password), True, True)
        return True
    else:
        return False


def login(username, password):
    if len(db.query_db("select * from user where username='%s' and password='%s';" % (username, password))) == 0:
        return False
    return True


def getUser(username):
    return db.query_db("select * from user where username='%s';" % username, True)
