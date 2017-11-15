from flask import render_template, request, session, redirect, url_for, send_from_directory

from application import app
import application.projects as projects
import application.sql as sql
import application.projects as projects
from application.upload import upload_file


@app.route('/')
def index():
    return render_template("index.html", cols=projects.get_test())


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
            session['user'] = sql.getUser(username)
            return redirect(url_for('index'))
        else:
            message = '<span class="red-text">登陆失败</div>'
    return render_template("login.html", message=message)


@app.route('/logout/')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


@app.route('/upload/', methods=["POST", "GET"])
def upload():
    message = ""
    url = ""
    if request.method == "POST":
        status = upload_file(request.files['file'])
        if status[0] == 1:
            message = '<span class="red">格式不支持</span>'
        else:
            url = "/static/uploads/" + status[1]
            message = '<span class="green">上传成功</span>' + url
    return render_template("upload.html", message=message, src=url)

@app.route('/test')
def test():
    return render_template("addon/map-set.html")


@app.route('/test2')
def test2():
    pos = {}
    pos["lng"] = 117.189606
    pos["lat"] = 31.774285
    return render_template("addon/map-show.html", pos=pos)
