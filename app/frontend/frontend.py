#!/bin/python3

from flask import Flask, render_template, request, send_file
import requests
from RipV2 import RipR, BorraRip
from OSPF import ospfR, BorraOSPF
from graphviz import Digraph, Source

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
    if rout_status == "RIP Activado":
        print("RIP---------------------------------")
        rout_status = RipR()
        
    if rout_status == "RIP Desactivado":
        print("RIP De")
        rout_status = BorraRip()
        
    if rout_status == "OSPF Activado":
        print("OSPF---------------------------------")
        rout_status = ospfR()
        
    if rout_status == "OSPF Desactivado":
        print("OSPF De")
        rout_status = BorraOSPF()
    return render_template('enrutamiento.html', rout_status=rout_status)
    
@app.route("/find")
def find():
    my_graph = Digraph("My_Network")
    my_graph.edge("MV", "R1")
    my_graph.edge("PC1", "R2")
    my_graph.edge("PC2", "R3")
    my_graph.edge("R1", "R2")
    my_graph.edge("R2", "R1")
    my_graph.edge("R2", "R3")
    my_graph.edge("R3", "R2")
    my_graph.render('static/topologia')
    #return send_file('templates/topologia.pdf')
    return render_template('topologia.html')

if __name__ == "__main__":
    app.run(debug=True)
