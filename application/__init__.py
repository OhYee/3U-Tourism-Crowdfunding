from flask import Flask

DATABASE = 'sql.db'
SECRET_KEY = '\xf2\x92Y\xdf\x8ejY\x04\x96\xc4V\x88\xfb\xfc\xb2\x18F\xa3\xee\xb9\xb9t\x01\xf0\x96'
UPLOAD_FOLDER = r'./application/static/uploads/'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

app = Flask(__name__)
app.config.from_object(__name__)

import application.views
import application.database
