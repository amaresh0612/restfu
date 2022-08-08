from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app= Flask(__name__)

api= Api(app)

@app.route("/")
def hello():
    return "hello Amaresh"

@app.route('/add', methods=["POST"])
def add():
    datadict = request.get_json()
    x=datadict["x"]
    y=datadict["y"]
    z=x+y
    resp = {"z":z}
    return jsonify(resp)

class Sum(Resource):
    def post(self):
        postedData =  request.get_json()
        x=postedData["x"]
        y=postedData["y"]
        z=x+y
        retMap={
            "msg": z,
            "statuscode": 200
        }
        return jsonify(retMap)

api.add_resource(Sum, '/sum')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)