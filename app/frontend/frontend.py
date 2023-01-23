#!/bin/python3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/routing")
def routing():
    return render_template('enrutamiento.html')

@app.route("/routing_change", methods=['POST'])
def routing_change():
    rout_status = request.form['routStatus']
    return render_template('enrutamiento.html', rout_status=rout_status)
    
@app.route("/find")
def find():
    #do something
    return render_template('topologia.html')

if __name__ == "__main__":
    app.run(debug=True)
