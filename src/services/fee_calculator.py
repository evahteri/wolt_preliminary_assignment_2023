import math
import datetime
from datetime import date



class FeeCalculator:

    def __init__(self, response_object):
        self.response_object = response_object
        self.fee = 0
        self.rush_start_time = datetime.datetime.strptime("15:00:00", "%H:%M:%S")
        self.rush_end_time = datetime.datetime.strptime("19:00:00", "%H:%M:%S")

    def calculate_fee(self):
        self._cart_value_less_than_1000()
        self._delivery_distance_fee()
        self._number_of_items()
        self._rush_hour_fee()
        if self.fee > 1500:
            self.fee = 1500
        if self.response_object.cart_value >= 10000:
            self.fee = 0
        return self.fee
    
    def _cart_value_less_than_1000(self):
        """This functions adds surcharge to the fee, if cart value is under
            10 euros (1000 units).
        """
        if self.response_object.cart_value < 1000:
            surcharge = 1000 - self.response_object.cart_value
            self.fee += surcharge
    
    def _delivery_distance_fee(self):
        """This function counts the extra fee from distance and adds it to the total fee.
        """

        if self.response_object.delivery_distance < 500: # Minimum delivery fee
            self.fee += 100
        
        if self.response_object.delivery_distance >= 500: # Delivery fee is 2 euros for the first 1km
            self.fee += 200
        
        if self.response_object.delivery_distance > 1000: # Counting the delivery fee for the extra 500 metres
            extra_charge = math.ceil((self.response_object.delivery_distance - 1000) / 500) # Extra charge is counted by deducting the first 1000 metres from the distance, then dividing it with 500 and rounding it upwards.
            self.fee += extra_charge * 100 # Add the extra charge and multiple it with 100 so that is matches the notation.
    
    def _number_of_items(self):
        """This function counts the fee for larger orders. No charge is added if there are only 4 items or less.
        """
        if self.response_object.number_of_items > 4:
            extra_items = self.response_object.number_of_items - 4 # Count how many extra items there are.
            self.fee += extra_items * 50 # Multiply the amount by 50 (50 cents) and add it to the total fee.
        if self.response_object.number_of_items > 12: # If there are more than 12 items, add the bulk fee (120 cents).
            self.fee += 120
    
    def _rush_hour_fee(self):
        """This function calculates the rush hour fee. Rush hours are defined in the class constructor.
        """
        if self.response_object.weekday == 5:
            if self.response_object.time_of_day >= self.rush_start_time and self.response_object.time_of_day <= self.rush_end_time:
                self.fee * 1.2




            