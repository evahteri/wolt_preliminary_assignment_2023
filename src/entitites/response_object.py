class ResponseObject:
    """Class for response objects to easier handle all the fields.
    """

    def __init__(self, cart_value, delivery_distance, number_of_items, time):
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.time = time