def missing_char(str, n):
    if n == 0:
        return str[1:len(str)]
    else:
        if n == len(str) - 1:
            return str[0:len(str) - 1]
        return str[0:n] + str[n + 1:len(str)]
print((missing_char('kitten', 1)))
