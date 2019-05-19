from flask import Flask, render_template
from flask import Markup
import numpy as np
import json
import glob
import datetime

from appfuncs import random_list, named_series, daily_range

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("landing.html")  


@app.route('/dashboard')
def landing():
    return render_template("index.html")


@app.route("/script.js")
def script():
    dataObject = {
        "spark1": random_list(20),
        "spark2": random_list(20),
        "spark3": random_list(20),
        "spark4": random_list(20),
        "multi-line": named_series(["Product %s" % i for i in ("A", "B", "C")]),
        "multi-line-labels": daily_range()
    }
    return render_template('scripts.js', dataObject=dataObject)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
