from flask import Flask, render_template
from flask import Markup
import numpy as np
import json
import glob
import datetime

app = Flask(__name__)


def random_list(n):
    ''' Returns a list of random normal variables'''
    return [np.round(k, 2) for k in list(np.random.normal(size=n).cumsum())]


def named_series(names):
    ''' Returns a list of dictionaries with "name" as string and "data" as a list of floats'''
    return [{"name": name, "data": random_list(6)} for name in names]


def daily_range(start=datetime.date.today(), days=6):
    ''' Create a range of n days. Default start is today'''
    drange = [start]
    for _ in range(days):
        drange.append(drange[-1] + datetime.timedelta(hours=24))
    return [i.strftime("%d-%b-%Y") for i in drange]


@app.route('/')
def index():
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
