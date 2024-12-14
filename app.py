from flask import Flask, jsonify, request

import json

from flask_cors import CORS


app = Flask(__name__)

CORS(app)

obj= None

with open("objs.json","r") as file:
    objs = json.load(file)



@app.route("/list",methods=["GET"])
def list():
    print(objs)
    return objs,200


@app.route("/list",methods=["POST"])
def Post():
    list = request.json

    objs.append(list)
    print(objs)
    with open("objs.json","w") as file:
        json.dump(objs, file, indent=4)

    return objs,201

if __name__ == '__main__':
    app.run(debug=True)