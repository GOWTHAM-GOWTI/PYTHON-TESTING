def twoSum(nums, target):

    ind_map = {}
    for i in range(len(nums)):

        num = nums[i]
        pair = target - num
        if pair in ind_map:
            return [ind_map[pair], i]
        ind_map[num] = i
    return None


nums = [1,4,8,3,2,9,15]
target = 4
print("Nums: ", nums)
print("Target: ", target)
print("Solution: ", twoSum(nums, target))