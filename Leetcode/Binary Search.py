"""
https://leetcode.com/problems/binary-search/
"""

nums = [-1, 0, 3, 5, 9, 12]
target = 132
ans = nums.index(target) if target in nums else -1
print(ans)