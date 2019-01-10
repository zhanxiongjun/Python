def not_string(str):
    if 'not' not in str[:3]:
        return 'not ' + str
    else:
        return str
print(not_string("not bad'"))