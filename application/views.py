from flask import render_template, request, session, redirect, url_for, send_from_directory

from application import app
import application.projects as projects
import application.sql as sql
import application.projects as projects
from application.upload import upload_file


@app.route('/')
def index():
    return render_template("index.html", cols=projects.get_test())


@app.route('/help/')
def help_page():
    return render_template("pages/help.html")


@app.route('/contact/')
def contact_page():
    return render_template("pages/contact.html")


@app.route('/agreement/')
def agreement_page():
    return render_template("pages/agreement.html")


@app.route('/join/')
def join_page():
    return render_template("pages/join.html")


@app.route('/about/')
def about_page():
    return render_template("pages/about.html")


@app.route('/add_project/')
def add_project():
    if 'user' not in session:
        return redirect(url_for('login'))
    session['user'] = sql.getUser(session['user']['username'])

    return render_template("add_project.html")


@app.route('/project/<pid>/')
def view_project(pid):
    return render_template("view_project.html", pid=pid)


@app.route('/search/')
def search():
    key = request.args.get("search")
    res = False
    if key != None:
        res = sql.search(key)
    return render_template("search.html", res=res)


@app.route('/register/', methods=["POST", "GET"])
def register():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['password']
        if sql.register(username, passwd):
            message = '<span class="green-text">注册成功,现在<a href="/login">登陆</a></span>'
        else:
            message = '<span class="red-text">注册失败</span>'
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
    if 'user' not in session:
        return redirect(url_for('login'))
    session.pop('user', None)
    return redirect(url_for('index'))


@app.route('/upload/', methods=["POST", "GET"])
def upload():
    message = ""
    url = ""
    if request.method == "POST":
        status = upload_file(request.files['file'])
        if status[0] == 1:
            message = '<span class="red-text">格式不支持</span>'
        else:
            url = "/static/uploads/" + status[1]
            message = '''<span class="green-text">上传成功</span> <span>地址<a href="{0}">{0}</a></span>
            <br><span>引用方式: &lt;img class="responsive-img materialboxed" src="{0}" data-caption="标题"></span>'''.format(url)
    return render_template("upload.html", message=message, src=url)


@app.route('/config/', methods=["POST", "GET"])
def config():
    if 'user' not in session:
        return redirect(url_for('login'))
    session['user'] = sql.getUser(session['user']['username'])

    message = ""
    if request.method == "POST":
        password = request.form['password']
        avatar = request.form['avatar']
        phone = request.form['phone']
        qq = request.form['qq']
        realname = request.form['realname']
        info = request.form['info']
        sql.config_updata(password, avatar, phone, qq, realname, info)
        session['user'] = sql.getUser(session['user']['username'])
        message = '<span class="green-text">更新成功</span>'

    return render_template("config.html", message=message)


@app.route('/admin/')
def admin():
    if 'user' not in session:
        return redirect(url_for('login'))
    session['user'] = sql.getUser(session['user']['username'])
    if session['user']['usergroup'] != '0':
        return redirect(url_for('index'))
    return render_template("admin.html", allUsers=sql.getAllUsers(), allProjects=sql.getAllProjects())


@app.route('/admin_user_update/', methods=["POST", "GET"])
def admin_user_update():
    if request.method == "POST":
        dic = request.form.copy()
        sql.admin_user_update(dic)
    return redirect(url_for('admin'))


@app.route('/admin_user_del/', methods=["POST", "GET"])
def admin_user_del():
    if request.method == 'POST':
        sql.admin_user_del(request.form['uid'])
    return redirect(url_for('admin'))


@app.route('/admin_project_update/', methods=["POST", "GET"])
def admin_project_update():
    pass


@app.route('/admin_project_del/', methods=["POST", "GET"])
def admin_project_del():
    pass


@app.route('/test')
def test():
    return render_template("addon/map-set.html")


@app.route('/test2')
def test2():
    pos = {}
    pos["lng"] = 117.189606
    pos["lat"] = 31.774285
    return render_template("addon/map-show.html", pos=pos)
