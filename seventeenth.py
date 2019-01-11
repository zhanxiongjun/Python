def last2(str):
    count1 = 0
    if len(str) <= 2:
        return 0;
    else:
        sub_str = str[len(str) - 2:len(str)]
        # print(sub_str)
        for i in range(len(str)):
            if(i >= 2):
                if sub_str is str[i - 2:i]:
                    count1 = count1 + 1
    return count1
print(last2("axxxaaxx"))
"""
str = 'zhanzhanzhanzhsdzhanxxxx'
print(str.count("xx",0,len(str)))
其实str.count这个方法是很奇怪的，他并不能把所有的子字符串都统计得到

"""