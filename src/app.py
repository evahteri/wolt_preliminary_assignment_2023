from flask import Flask, jsonify, request
from services.fee_calculator import FeeCalculator
from entitites.response_object import ResponseObject

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    """Function to handle and response to the incoming POST request.

    Returns:
        JSON -file: A json object, which includes a delivery fee field as the fee as it's value.
    """
    delivery_info = request.get_json()
    # Forming a response object from the incoming json.
    response_object = ResponseObject(
        cart_value=delivery_info["cart_value"],
        delivery_distance=delivery_info["delivery_distance"],
        number_of_items=delivery_info["number_of_items"],
        time=delivery_info["time"]
    )
    fee_calculator = FeeCalculator(response_object)
    # Counting the fee using fee calculator
    delivery_fee = fee_calculator.calculate_fee()
    return jsonify({"delivery_fee": delivery_fee})
