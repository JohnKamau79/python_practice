import heapq
import time

class MatchingEngine:
    def __init__(self) -> None:
        self.buy_orders = []
        self.sell_orders = []
        self.timestamp = time.localtime()
        
    def place_buy_order(self, price, quantity):
        heapq.heappush(self.buy_orders, (-price, self.timestamp, quantity))
        self.match()
        
    def place_sell_order(self, price, quantity):
        heapq.heappush(self.sell_orders, (price, self.timestamp, quantity))
        self.match()
    
    def match(self):
        while self.buy_orders and self.sell_orders:
            buy_price, buy_time, buy_quantity = self.buy_orders[0]
            sell_price, sell_time, sell_quantity = self.sell_orders[0]
            
            buy_price = -buy_price
            
            if buy_price < sell_price:
                print(f'Best buy_price({buy_price} USD ) is less than best sell_price({sell_price} USD)')
                break
            
            heapq.heappop(self.buy_orders)
            heapq.heappop(self.sell_orders)
            
            traded_quantity = min(buy_quantity, sell_quantity)
            trade_price = sell_price
            
            print(f'Traded {traded_quantity} shares at {sell_price * traded_quantity} USD')
            
            buy_quantity = buy_quantity - traded_quantity
            sell_quantity = sell_quantity - traded_quantity
            
            if buy_quantity > 0:
                heapq.heappush(self.buy_orders, (-buy_price, buy_time, buy_quantity))\
            
            if sell_quantity > 0:
                heapq.heappush(self.sell_orders, (sell_price, sell_time, sell_quantity))

engine = MatchingEngine()
engine.place_sell_order(50, 20)
engine.place_sell_order(50, 20)
engine.place_sell_order(55, 6)
engine.place_sell_order(55, 5)

engine.place_buy_order(60, 10)
engine.place_buy_order(50, 10)

print(engine.buy_orders)
print(engine.sell_orders)