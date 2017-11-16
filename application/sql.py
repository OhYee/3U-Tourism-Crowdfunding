from flask import g

from application import app

import hashlib
import re
import application.database as db


def md5(string):
    m = hashlib.md5()
    m.update(string.encode("utf-8"))
    return m.hexdigest()

def register(username, password):
    if len(db.query_db("select * from user where username='%s';" % (username))) == 0:
        db.query_db("insert into user(uid,username,password,avatar) values('%s','%s','%s','%s');" % (
            db.getNextId('uid', 'user'), username, md5(password), '/static/img/default.png'), True, True)
        return True
    else:
        return False


def login(username, password):
    if len(db.query_db("select * from user where username='%s' and password='%s';" % (username, md5(password)))) == 0:
        return False
    return True


def getUser(username):
    return db.query_db("select * from user where username='%s';" % username, True)
