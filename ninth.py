def not_string(str):
    if 'not' not in str[:3]:
        return 'not ' + str
    else:
        return str
print(not_string("not bad'"))

"""但是这样做是错的，因为没有考虑到字符串长度小于三"""

def not_string_two(str):
    if len(str) < 3 or 'not' not in str[:3]
        return 'not ' + str
    else:
        return str
    