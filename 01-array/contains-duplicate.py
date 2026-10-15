arr = list(map(int, input().split()))

seen = set()

for x in arr :
    if x in seen :
        print(True)
        break
    else :
        seen.add(x)

else :
    print(False)

## leetcode veresion submission

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for x in nums :
            if x in seen :
                return True
            else :
                seen.add(x)
        else :
            return False
        