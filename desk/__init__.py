from flask import Flask

from desk.reverse_proxy import ReverseProxied


app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)
