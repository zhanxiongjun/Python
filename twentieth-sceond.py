"""
注意在列表中，其方法extend和append是不一样的，
append是整个数据类型不变存进去的
而extend是将数据类型分割出来存进去

"""
"""
def string_match(a, b):
    a_list = []
    b_list = []
    i = 0
    j = 0
    count = 0
    #对a求出两个子字符串
    while i < len(a) - 1:
        a_list.append(a[i:i + 2])
        i = i + 1
    while j < len(b) - 1:
        b_list.append(b[j:j + 2])
        j = j + 1
    i = 0
    j = 0
    while i < len(a_list) and j < len(b_list):
        if a_list[i] == b_list[j]:
            count = count + 1
        i = i + 1
        j = j + 1
    return count
print(string_match('aabbccdd', 'abbbxxd'))
"""
"""
def string_match(a,b):
    i = 0
    j = 0
    count = 0
    while i < len(a) - 1 and j < len(b) - 1:
        if a[i:i + 2] == b[j:j + 2]:
            count = count + 1
        i = i + 1
        j = j + 1
    return count
print(string_match('aabbccdd', 'abbbxxd'))
"""
def string_match(a, b):
    shorter = min(len(a), len(b))
    count = 0
    for i in range(shorter - 1):
        a_sub = a[i:i + 2]
        b_sub = b[i:i + 2]
        if a_sub == b_sub
            count = count + 1
    return count

#题目：
"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0

"""

