import unittest
from services.fee_calculator import FeeCalculator
from entitites.response_object import ResponseObject

class TestFeeCalculator(unittest.TestCase):
    def setUp(self):
        self.test_response_object = ResponseObject(
            cart_value=790,
            delivery_distance=2235,
            number_of_items=4,
            time="2021-10-12T13:00:00Z"
        )
        self.test_fee_calculator = FeeCalculator(response_object=
        self.test_response_object
        )
    
    def test_fee_calculator(self):
        correct_fee = 710
        calculated_fee = self.test_fee_calculator.calculate_fee()
        self.assertEqual(correct_fee, calculated_fee)

    def test_fee_calculator_cart_value_over_10000(self):
        correct_fee = 0
        test_response_object = ResponseObject(
            cart_value=11000,
            delivery_distance=2235,
            number_of_items=4,
            time="2021-10-12T13:00:00Z"
        )
        test_fee_calculator = FeeCalculator(response_object=
        test_response_object
        )
        calculated_fee = test_fee_calculator.calculate_fee()
        self.assertEqual(correct_fee, calculated_fee)
    
    def test_fee_calculator_cart_value_under_1000(self):
        correct_fee = 310
        test_response_object = ResponseObject(
            cart_value=790,
            delivery_distance=200,
            number_of_items=4,
            time="2021-10-12T13:00:00Z"
        )
        test_fee_calculator = FeeCalculator(response_object=
        test_response_object
        )
        calculated_fee = test_fee_calculator.calculate_fee()
        self.assertEqual(correct_fee, calculated_fee)
