#!/bin/python3

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/routing")
def routing():
    return render_template('enrutamiento.html')

if __name__ == "__main__":
    app.run(debug=True)
