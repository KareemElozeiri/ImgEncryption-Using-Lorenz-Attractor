from crypt import methods
import json
from flask import Flask, request, jsonify
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from lorenz import Lorenz
import numpy as np 
app = Flask(__name__)



@app.route("/api/encrypt", methods=["POST"])
def encrypt():
    reqJson = request.json
    try:
        x_0 = float(reqJson["x_0"])
        y_0 = float(reqJson["y_0"])
        z_0 = float(reqJson["z_0"])
        a = float(reqJson["a"])
        b = float(reqJson["b"])
        r = float(reqJson["r"])

        encrypt_lorenz = Lorenz(x_0, y_0, z_0, a, b, r)

        return jsonify({"success":True,"data":None})

    except Exception as e:
        print(type(e).__name__,e.args)
        return jsonify({"success":False,"msg":type(e).__name__})



@app.route("/api/decrypt", methods=["POST"])
def decrypt():
    reqJson = request.json
    print(reqJson)
    try:
        x_0 = float(reqJson["x_0"])
        y_0 = float(reqJson["y_0"])
        z_0 = float(reqJson["z_0"])
        a = float(reqJson["a"])
        b = float(reqJson["b"])
        r = float(reqJson["r"])

        encrypt_lorenz = Lorenz(x_0, y_0, z_0, a, b, r)

        return jsonify({"success":True,"data":None})

    except Exception as e:
        print(type(e).__name__,e.args)
        return jsonify({"success":False,"msg":type(e).__name__})

    



if __name__=="__main__":
    app.run()