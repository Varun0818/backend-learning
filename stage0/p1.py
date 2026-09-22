def totals_by_customer(orders):
    result={}
    for order in orders:
        name=order["customer"]
        sum_=0
        for order_ in orders:
            if order_["customer"]==name:
                sum_+=order_["amount"]
        result[name]=sum_
    return(result)


