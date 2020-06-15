import math
def eoq(D: float, K: float, h: float) -> int:
    """
    The EOQ is the order cuantity that minimizes
    the total holding costs and ordering costs.

    D: annual demand
    K: cost of emmiting an order per unit
    h: cost of storing an unit
    """
    return math.ceil(((2*D*K)/h)**(1/2))

def cycle_time(q: float, D: float) -> float:
    """
    The cycle team is the order quantity
    divided by the demand.
    """
    return q / D

def total_cost(D: float, K: float, h: float, eoq: float) -> float:
    """
    The total cost is the cost of ordering plus mantaining
    """
    return ordering_cost(D, K, eoq) + mantain_cost(D, h)

def ordering_cost(D: float, K: float, eoq: float) -> float:
    return K * (D / eoq)

def mantain_cost(D: float, h: float):
    return h * (D/ 2) # because y/2 is the average amount of items

def reorder_point(D: float, L: float, working_days: int) -> int:
    return math.floor(D * (L/working_days))
