import os
import time
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from application import app


ALLOWED_EXTENSIONS = set(['jpg', 'png', 'gif', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def upload_file(file):
    if file and allowed_file(file.filename):
        path = getRandomString() + secure_filename(file.filename)
        print("upload: ", path)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], path))
        return [0, path]
    else:
        return [1]


def getRandomString():
    return (str)(time.time())
