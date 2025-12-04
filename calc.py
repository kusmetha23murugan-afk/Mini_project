def calc_amount(units):
    if units <= 200:
        return units * 3.00
    elif units <= 400:
        return 200*3.00 + (units-200)*4.50
    elif units <= 800:
        return 200*3.00 + 200*4.50 + (units-400)*6.50
    else:
        return 200*3.00 + 200*4.50 + 400*6.50 + (units-800)*8.00
    

def fine(amt,days):
    if days>30:
        return amt+amt*0.15
    elif days>20:
        return amt+amt*0.10
    elif days>10:
        return amt+amt*0.5
    elif days>0:
        return amt+amt*0.02
    else:
        return amt
