def front_times(str, n):
    if(len(str) >= 3):
        return str[:3] * n
    return str * n
print(front_times("zafd",4))