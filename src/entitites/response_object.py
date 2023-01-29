from datetime import date, datetime


class ResponseObject:
    """Class for response objects to easier handle all the fields.
        ISO date is parsed for conviency to time of day and weekday fields.
    """

    def __init__(self, cart_value, delivery_distance, number_of_items, time):
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.time = time
        self.weekday = date(
            year=int(self.time[0:4]),
            month=int(self.time[5:7]),
            day=int(self.time[8:10]
                    )
        ).isoweekday()
        self.time_of_day = datetime.strptime(
            self.time[11:19],
            "%H:%M:%S"
        )
