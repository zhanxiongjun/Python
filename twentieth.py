"""
def array_front9(nums):
    if len(nums) <=4:
        return 9 in nums
    for i in range(4):
        if 9 == nums[i]:
            return True

    return False

print(array_front9([1,1,2,4,4]))
"""
def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4
    for i in range(end):
        if nums[i] == 9:
            return True
    return False