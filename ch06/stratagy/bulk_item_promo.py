import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from promotion import Promotion

class BulkItemPromo(Promotion):
    '''单个商品或20个以上时提供10%折扣'''

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount