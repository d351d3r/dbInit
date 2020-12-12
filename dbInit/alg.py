def formula_fedosa(positive, neutral, negative):
    
    not_neut = positive + negative
    if neutral > not_neut:
        return 0
    elif positive>negative:
        return 1
    else:
        return -1