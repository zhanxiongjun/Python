def array_count9(nums):

    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count

    #return nums.count(9)

print(array_count9([4,6,9,9,0]))