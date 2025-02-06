# queining systems, that accepts orders from customers
# orders: orderid, pickup/deliver time, userid
# design the interface to get the orders from the customer (api: add_order(order) -> add an order the queue))
# 2. get_order() -> the order that has the closest pickup/delivery time
# the orders may not be received in order of pickup or  delivery time
# [1,  a, 10], [2, b, 50], [3, c, 5], [4, f, 5], [5, a, 2]
# add_order(id: 505, time: 30)
# get_order() -> order that is highest priority, if the user has multiple orders pending, fulfill all orders pending for that users at that time.
#

import heapq as hp


class Order:
    def __init__(self, order_id, due_time, user_id):
        self.order_id = order_id
        if not due_time:
            raise Exception("Due time is null")
        self.due_time = due_time
        self.user = user_id

    def get_priority(self):
        return self.due_time

    def __le__(self, order):
        if self.get_priority <= order.due_time:
            return True
        else:
            return False


class OrderingSystem:
    def __init__(self):
        self.heap = hp([])
        self.order_ids = set()
        self.orders_by_user = {}

    def add_order(self, order_id, due_time, user_id):
        if not order_id:
            raise Exception("empty order")
        if not order_id in self.order_ids:
            order = Order(order_id, due_time, user_id)
            if not user_id in self.orders_by_user:
                self.orders_by_user[user_id] = []
            self.orders_by_user[user_id].append(order)
            self.heap.push(order)
            self.order_ids.add(order_id)
        else:
            raise Exception("Order ID already exists")

    def get_order(self):
        if len(self.heap) > 0:
            order = self.heap.pop()
            self.order_ids.discard(order.order_id)
            order_ids = [order.order_id]
            if not order.user_id in self.orders_by_user:
                raise Exception("user not in dict")
            orders_by_user = self.orders_by_user[order.user_id]
            for other_order in orders_by_user:
                order_ids.append(other_order.order_id)
                ## remove from heap
                self.remove_order_from_queue(other_order.order_id)
                ## remove from set
                self.order_ids.discard(other_order.order_id)
            ## remove from dictionary
            self.orders_by_user[order.user_id] = []
            return order_ids
        else:
            raise Exception("Ordering System is empty")

    def remove_order_from_queue(self, order_id):
        ### remove order based on order
        return None

# [order, priority/time, id]
# hash: {{user, priority}} keeps track if user has active orders
# [order_ids, ]
# add order
# look-up users order
# {priority,
# orders: [order, oder2, oder3],
# user}




