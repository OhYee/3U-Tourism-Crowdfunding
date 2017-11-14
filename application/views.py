from flask import render_template, request, session, redirect, url_for

from application import app
import application.projects
import application.sql as sql


@app.route('/')
def index():
    return render_template("index.html", cols=application.projects.get_test())


@app.route('/add_project/')
def add_project():
    return render_template("add_project.html")


@app.route('/project/<pid>/')
def view_project(pid):
    return render_template("view_project.html", pid=pid)


@app.route('/register/', methods=["POST", "GET"])
def register():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['password']
        if sql.register(username, passwd):
            message = '<span class="green-text">注册成功</div>'
        else:
            message = '<span class="red-text">注册失败</div>'
    return render_template("register.html", message=message)


@app.route('/login/', methods=["POST", "GET"])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['password']
        if sql.login(username, passwd):
            message = '<span class="green-text">登陆成功</div>'
            session['username'] = username
            return redirect(url_for('index'))
        else:
            message = '<span class="red-text">登陆失败</div>'
    return render_template("login.html", message=message)


@app.route('/logout/')
def logout():
    session.pop('id', None)
    return redirect(url_for('index'))


@app.route('/test')
def test():
    return render_template("addon/map-set.html")


@app.route('/test2')
def test2():
    pos = {}
    pos["lng"] = 117.189606
    pos["lat"] = 31.774285
    return render_template("addon/map-show.html", pos=pos)
