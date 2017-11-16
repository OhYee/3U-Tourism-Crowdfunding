from flask import g, session

from application import app

import hashlib
import re
import application.database as db


def md5(string):
    m = hashlib.md5()
    m.update(string.encode("utf-8"))
    return m.hexdigest()


def register(username, password):
    if len(db.query_db("select * from user where username=='%s' collate nocase;" % (username))) == 0:
        uid = db.getNextId('uid', 'user')
        if uid == '1':
            db.query_db("insert into user(uid,username,password,avatar,usergroup) values('%s','%s','%s','%s','%s');" % (
                uid, username, md5(password), '/static/img/default.png', '0'), True, True)
        else:
            db.query_db("insert into user(uid,username,password,avatar,usergroup) values('%s','%s','%s','%s','%s');" % (
                uid, username, md5(password), '/static/img/default.png', '1'), True, True)
        return True
    else:
        return False


def login(username, password):
    if len(db.query_db("select * from user where username=='%s' collate nocase and password=='%s';" % (username, md5(password)))) == 0:
        return False
    return True


def getUser(username):
    res = db.query_db("select * from user where username='%s' collate nocase;" %
                      username, True)
    for key in res.keys():
        if res[key] == None:
            res[key] = ""
    return res


def getAllUsers():
    res = db.query_db("select * from user")
    l = len(res)
    for i in range(0, l):
        for key in res[i].keys():
            if res[i][key] == None:
                res[i][key] = ""
    return res


def getAllProjects():
    return db.query_db("select * from project")


def config_updata(password, avatar, phone, qq, realname, info):
    uid = session['user']['uid']
    usergroup = session['user']['usergroup']
    db.query_db("update user set avatar='%s',phone='%s',qq='%s',info='%s' where uid=='%s';" %
                (avatar, phone, qq, info, uid), True, True)
    if password != "":
        db.query_db("update user set password='%s' where uid=='%s';" %
                    (md5(password), uid), True, True)
    if usergroup == "1" and realname == "":
        db.query_db("update user set realname='%s' where uid=='%s';" %
                    (realname, uid), True, True)


def admin_user_update():
    pass


def admin_user_del(uid):
    db.query_db("delete from user where uid == '%s';" % (uid), True, True)


def admin_project_update():
    pass


def admin_project_del():
    pass
