from collections import namedtuple
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from order import Order
from line_item import LineItem
from bulk_item_promo import BulkItemPromo
from fidelity_promo import FidelityPromo
from large_order_promo import LargeOrderPromo

Customer = namedtuple('Customer', 'name fidelity')

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('bannana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

print(Order(joe, cart, FidelityPromo()))
print(Order(ann, cart, FidelityPromo()))