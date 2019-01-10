"""
def front_back(str):
    return str[len(str) - 1] + str[1:len(str) - 1] + str[0] if len(str) != 1 else str
print(front_back("abcd"))
"""
def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[len(str) - 1] + str[1:len(str) - 1] + str[0]
print(front_back("f"))
#这个要小于等于1？？？
#考虑字符串为零的时候

