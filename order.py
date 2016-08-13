# class for an order
import json

class Order:
    def __init__(self, venue, stock, price, quantity, direction, orderType):
        self.venue = venue;
        self.symbol = stock;
        self.price = price;
        self.qty = quantity;
        self.direction = direction;
        self.orderType = orderType;

    def getOrderString(self):
        return json.dumps(self.__dict__);
