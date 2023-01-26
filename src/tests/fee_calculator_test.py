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
        """Testing the calculator with the example order
        """
        correct_fee = 710
        calculated_fee = self.test_fee_calculator.calculate_fee()
        self.assertEqual(correct_fee, calculated_fee)

    def test_fee_calculator_cart_value_over_10000(self):
        """Testing the calculator with over 100 euro cart value
        """
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
    
    def test_fee_calculator_delivery_distance_value_under_1000(self):
        """Testing the calculator with delivery distance under one kilometer
        """
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

    def test_fee_calculator_delivery_distance_under_500(self):
        """Testing the calculator with delivery distance under 500 meters
        """
        correct_fee = 100
        test_response_object = ResponseObject(
            cart_value=1100,
            delivery_distance=200,
            number_of_items=4,
            time="2021-10-12T13:00:00Z"
        )
        test_fee_calculator = FeeCalculator(response_object=
        test_response_object
        )
        calculated_fee = test_fee_calculator.calculate_fee()
        self.assertEqual(correct_fee, calculated_fee)

    def test_fee_calculator_delivery_distance_over_500_under_1000(self):
        """Testing the calculator with delivery distance between 500 and 1000 meters
        """
        correct_fee = 200
        test_response_object = ResponseObject(
            cart_value=1100,
            delivery_distance=700,
            number_of_items=4,
            time="2021-10-12T13:00:00Z"
        )
        test_fee_calculator = FeeCalculator(response_object=
        test_response_object
        )
        calculated_fee = test_fee_calculator.calculate_fee()
        self.assertEqual(correct_fee, calculated_fee)

    def test_fee_calculator_delivery_distance_over_1000_under_1500(self):
        """Testing the calculator with delivery distance between 1000 and 1500 meters
        """
        correct_fee = 300
        test_response_object = ResponseObject(
            cart_value=1100,
            delivery_distance=1499,
            number_of_items=4,
            time="2021-10-12T13:00:00Z"
        )
        test_fee_calculator = FeeCalculator(response_object=
        test_response_object
        )
        calculated_fee = test_fee_calculator.calculate_fee()
        self.assertEqual(correct_fee, calculated_fee)

    def test_fee_calculator_delivery_distance_over_1500_under_2000(self):
        """Testing the calculator with delivery distance between 1500 and 2000 meters
        """
        
        correct_fee = 400
        test_response_object = ResponseObject(
            cart_value=1100,
            delivery_distance=1501,
            number_of_items=4,
            time="2021-10-12T13:00:00Z"
        )
        test_fee_calculator = FeeCalculator(response_object=
        test_response_object
        )
        calculated_fee = test_fee_calculator.calculate_fee()
        self.assertEqual(correct_fee, calculated_fee)


    def test_fee_calculator_number_of_items_10(self):
        """Testing the calculator if there are 10 items
        """
        correct_fee = 400
        test_response_object = ResponseObject(
            cart_value=1100,
            delivery_distance=300,
            number_of_items=10,
            time="2021-10-12T13:00:00Z"
        )
        test_fee_calculator = FeeCalculator(response_object=
        test_response_object
        )
        calculated_fee = test_fee_calculator.calculate_fee()
        self.assertEqual(correct_fee, calculated_fee)

    def test_fee_calculator_number_of_items_13(self):
        """"Testing the calculator if there are 13 items
        """
        correct_fee = 670
        test_response_object = ResponseObject(
            cart_value=1100,
            delivery_distance=300,
            number_of_items=13,
            time="2021-10-12T13:00:00Z"
        )
        test_fee_calculator = FeeCalculator(response_object=
        test_response_object
        )
        calculated_fee = test_fee_calculator.calculate_fee()
        self.assertEqual(correct_fee, calculated_fee)

    def test_fee_calculator_fee_not_over_1500(self):
        """Test that the fee never exceeds 1500 cents
        """
        correct_fee = 1500
        test_response_object = ResponseObject(
            cart_value=1100,
            delivery_distance=20000,
            number_of_items=20,
            time="2021-10-12T13:00:00Z"
        )
        test_fee_calculator = FeeCalculator(response_object=
        test_response_object
        )
        calculated_fee = test_fee_calculator.calculate_fee()
        self.assertEqual(correct_fee, calculated_fee)
    
    def test_fee_calculator_fee_friday_rush(self):
        """Test the calculator during friday rush
        """
        correct_fee = 852
        test_response_object = ResponseObject(
            cart_value=790,
            delivery_distance=2235,
            number_of_items=4,
            time="2023-01-27T16:00:00Z"
        )
        test_fee_calculator = FeeCalculator(response_object=
        test_response_object
        )
        calculated_fee = test_fee_calculator.calculate_fee()
        self.assertEqual(correct_fee, calculated_fee)
    
    def test_fee_calculator_fee_friday_not_rush(self):
        """Test the calculator if it is friday but not rush hour
        """
        correct_fee = 710
        test_response_object = ResponseObject(
            cart_value=790,
            delivery_distance=2235,
            number_of_items=4,
            time="2023-01-27T11:00:00Z"
        )
        test_fee_calculator = FeeCalculator(response_object=
        test_response_object
        )
        calculated_fee = test_fee_calculator.calculate_fee()
        self.assertEqual(correct_fee, calculated_fee)