"""
def front_back(str):
    return str[len(str) - 1] + str[1:len(str) - 1] + str[0] if len(str) != 1 else str
print(front_back("abcd"))
"""
"""
def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[len(str) - 1] + str[1:len(str) - 1] + str[0]
print(front_back("f"))
#这个要小于等于1？？？
#考虑字符串为零的时候
"""
def front_back(str):
    if len(str) <= 1:
        return str
    mid = str[1:len(str) - 1]
    return str[len(str) - 1] + mid + str[0]
#看一下人家是怎么写的
#借鉴一下，我觉得学习一门语言，大量的题目是非常必要的
#因为这样你会掌握它的最基础知识，为你的以后向上发展打下坚实基础


