import json
from flask import Flask, jsonify, request
from services.fee_calculator import the_fee_calculator
from entitites.response_object import ResponseObject

class App:

    def __init__(self):
        pass

    def calculate_fee(self):
        return the_fee_calculator.calculate_fee()

the_app = App()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def return_delivery_fee():
    return "hello"

@app.route("/", methods=["POST"])
def insert_delivery_info():
    delivery_info = request.get_json()
    return jsonify({"delivery_fee": the_app.calculate_fee()})