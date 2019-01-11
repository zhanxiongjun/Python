#这个函数耗费了我多一点时间，要么就是超时，要么就是错误
"""
def array123(nums):
    array = []
    i = 0
    while i < len(nums) - 2:
        if nums[i] == 1:
            array.append(nums[i:i + 3])
            i = i + 1
        else:
            i = i + 1
    if [1,2,3] in array:
        return True
    else:
        return False

print(array123([1,1,2,3]))
"""
#接下来有个新的方法:
def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 3] == 3:
            return True
    return False



