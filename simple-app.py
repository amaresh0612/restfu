from tkinter import Y
from urllib import response
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello1():
    return "Hi Amaresh"

@app.route('/rusu')
def hello2():
    return "Hi Rusu"

@app.route('/add', methods = ["POST"])
def add():
    #Get x,y from POST
    dataDict = request.get_json()
    #add Z=x+y
    x=dataDict["x"]
    y=dataDict["y"]
    if "y" not in dataDict:
        return "error", 305
    z=x+y
    response ={"z":z}
    return jsonify(response)


@app.route('/sum')
def hello3():
    js ={
        "field1":1,
        "field2":2
    }
    x= js["field1"]
    y= js["field2"]
    z= x+y
    js1={"result":z}
    return jsonify(js1)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)