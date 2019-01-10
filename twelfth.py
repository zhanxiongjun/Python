def front3(str):
    if(len(str) < 3):
        return str * 3
    return str[:3] * 3
print(front3("zh"))
#这个做的是比答案要好的，答案有点复杂，而且也没有运用乘法

