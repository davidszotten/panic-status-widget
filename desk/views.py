from flask import render_template

from desk import app
from desk.connection import get_data


@app.route('/')
def index():
    data = get_data()
    total = data['total_entries']
    return render_template('index.html', total=total)
