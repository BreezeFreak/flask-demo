def add_record(mongo_obj, money, charge=False, buy=False):
    from datetime import datetime
    if charge:
        status = '+'
    elif buy:
        status = '-'
    else:
        return 'error'
    mongo_obj["purchase_record"][str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))] = status + str(money)
    return mongo_obj
