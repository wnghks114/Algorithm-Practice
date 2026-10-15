arr = list(map(int, input().split()))

current = arr[0]
best = arr[0]

for x in arr[1:]:
    current = max(current + x, x)
    best = max(best, current)

print(best)

## leetcode version

class Solution(object):
    def maxSubArray(self, nums):
        current = nums[0]
        best = nums[0]

        for x in nums[1:] :
            current = max(current + x, x)
            best = max(best, current)

        return best