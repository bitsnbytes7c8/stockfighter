import requests
from order import Order
import json

KEYS_FILE_NAME = "keys.json";

class StockFighterAccessor:
    BASE_URL = "https://api.stockfighter.io/ob/api"

    def __init__(self, account):
        self.account = account;
        with open(KEYS_FILE_NAME) as f:
            self.api_key = json.load(f)['api_key'];

    def placeOrder(self, order):
        orderBody = json.loads(order.getOrderString());
        orderBody['account'] = self.account;
        response = requests.post(self.BASE_URL + "/venues/" + order.venue + "/stocks/" + order.symbol + "/orders", data=json.dumps(orderBody), headers = {"X-Starfighter-Authorization":self.api_key});
        return response;

    def isApiUP(self):
        response = requests.get(BASE_URL + "/heartbeat");
        return (response.status_code == 200);
