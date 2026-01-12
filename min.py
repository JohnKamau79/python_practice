import heapq

sell_orders = []

heapq.heappush(sell_orders, (100, 20))
heapq.heappush(sell_orders, (90, 10))
heapq.heappush(sell_orders, (70, 20))
heapq.heappush(sell_orders, (130, 20))

# best_sell_price, sell_qty = heapq.heappop(sell_orders)

# print(best_sell_price, sell_qty)


buy_orders = []

heapq.heappush(buy_orders, (-110, 5))
heapq.heappush(buy_orders, (-80, 5))
heapq.heappush(buy_orders, (-50,4))
heapq.heappush(buy_orders, (-150, 5))

best_buy_price, buy_qty = heapq.heappop(buy_orders)

print(-best_buy_price, buy_qty)

traded_qty = None
remaining_qty = None

if sell_orders and buy_qty > 0:
    best_sell_price, sell_qty = heapq.heappop(sell_orders)
    traded_qty = min(buy_qty, sell_qty) # 5
    buy_qty = buy_qty - traded_qty # 0
    sell_qty = sell_qty - traded_qty # 15
    
    if sell_qty > 0:
        heapq.heappush(sell_orders, (best_sell_price, sell_qty))
        print(sell_orders)
        
    else:
        print('Order is fully filled')