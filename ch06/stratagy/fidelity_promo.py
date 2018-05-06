import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from promotion import Promotion

class FidelityPromo(Promotion):
    '''为积分100或以上的顾客提供5%折扣'''

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0
