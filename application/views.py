from flask import render_template

from application import app
import application.projects

@app.route('/')
def index():
    return render_template("index.html",cols=application.projects.get_test())

@app.route('/test')
def test():
    return render_template("addon/map-set.html")

@app.route('/test2')
def test2():
    pos={}
    pos["lng"]=117.189606
    pos["lat"]=31.774285
    return render_template("addon/map-show.html",pos=pos)