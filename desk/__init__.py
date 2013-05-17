from flask import Flask, render_template

from desk.reverse_proxy import ReverseProxied
from desk.connection import get_data

app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)

@app.route('/')
def index():
    total = get_data()
    return render_template('index.html', total=total)
