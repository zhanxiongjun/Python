"""def missing_char(str, n):
    if n == 0:
        return str[1:len(str)]
    else:
        if n == len(str) - 1:
            return str[0:len(str) - 1]
        return str[0:n] + str[n + 1:len(str)]
print((missing_char('kitten', 1)))"""
"""啊啊啊，再次留下没技术的泪水
看了一下他们的解决方法，瞬间发现自己真的很垃圾
不行，向他们学习。
记住一点，python很重要的一点就是简洁，不要搞得太复
"""
def missing_char(str, n):
    front = str[:n]
    back = str[n + 1:]
    return front + back