from p1 import totals_by_customer

def test_multiple_customers():
    orders = [{"customer": "varun", "amount": 500}, {"customer": "amit", "amount": 300}]
    assert totals_by_customer(orders) == {"varun": 500, "amit": 300}
def test_repeated_customer():
    orders = [{"customer": "amit", "amount": 500}, {"customer": "amit", "amount": 300}]
    assert totals_by_customer(orders) == {"amit": 800}
def test_zero_total():
    orders = [{"customer": "varun", "amount": 500}, {"customer": "varun", "amount": -500}]
    assert totals_by_customer(orders) == {"varun": 0}
def test_empty_input():
    orders = []
    assert totals_by_customer(orders) == {}
def test_input_not_modified():
    orders = [{"customer": "varun", "amount": 500}, {"customer": "amit", "amount": 300}]
    orders_before = [dict(o) for o in orders]
    totals_by_customer(orders)
    assert orders == orders_before
