from stockFighterAccessor import StockFighterAccessor;
from order import Order;

venue = raw_input("Enter the venue: ");
stock = raw_input("Enter the stock symbol: ");
account = raw_input("Enter the account: ");

marketOrder = Order(venue, stock, 10000, 100, "buy", "market")
accessor =  StockFighterAccessor(account);
print accessor.placeOrder(marketOrder).text;
