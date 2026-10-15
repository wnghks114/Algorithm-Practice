arr = list(map(int, input().split()))
target = int(input())
seen = {}

for i, x in enumerate(arr) :
    need = target - x

    if need in seen :
        print([seen[need], i]) 
        break
    else :
        seen[x] = i

## leetcode version submission 

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, x in enumerate(nums) :
            need = target - x

            if need in seen :
                return [seen[need], i]
            else :
                seen[x] = i        