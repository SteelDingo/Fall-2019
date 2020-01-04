class ticket(object):
    def __init__(self, destination='', departure_time='', date='', seat_class='', price=0, passengers=0, ticket_holder=''):
        self.dest_str = destination
        self.dep_time_str = departure_time
        self.date_str = date
        self.seat_class_str = seat_class
        self.price_int = price
        self.passengers_int = passengers
        self.ticket_holder_str = ticket_holder

    def update(self, destination='', departure_time='', date='', seat_class='', price=0, passengers=0, ticket_holder=''):
        if destination:
            self.dest_str = destination
        if departure_time:
            self.dep_time_str = departure_time
        if date:
            self.date_str = date
        if seat_class:
            self.seat_class_str = seat_class
        if price:
            self.price_int = price
        if passengers:
            self.passengers_int = passengers
        if ticket_holder:
            self.ticket_holder_str = ticket_holder

    def __str__(self):
        return "{}, Departure: {}, {}, Seat: {}, {}, {} passengers, Holder: {}".\
               format(self.dest_str, self.dep_time_str, self.date_str, self.seat_class_str, self.price_int, self.passengers_int, self.ticket_holder_str)
    
