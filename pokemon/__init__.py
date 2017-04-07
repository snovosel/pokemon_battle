from flask import Flask

app = Flask(__name__)
app.config.from_object('config.BaseConfiguration')

from pokemon import views
