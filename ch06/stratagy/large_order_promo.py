import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from promotion import Promotion

class LargeOrderPromo(Promotion):
    '''订单中的不同商品达到10个或者以上时提供7%折扣'''

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0
