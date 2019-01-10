def pos_neg(a, b, negatiove):
    if negatiove == True and a < 0 and b < 0:
        return True
    else:
        if (a > 0 and b < 0 or a < 0 and b > 0) and negatiove == False:
            return True
        else:
            return False
print(pos_neg(1,-1,True))