"""
https://leetcode.com/problems/two-sum/
"""


nums = [3, 4, 2]
target = 6

map = dict()
for i in range(len(nums)):
    # nums[i] + ? = target => ? = target - nums[i]
    x = (target - nums[i])
    if map.get(x) is not None:
        print([i, map[x]])
    else:
        map[nums[i]] = i