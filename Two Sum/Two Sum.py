# 시간 복잡도 O(n**2)
class Solution:
    def twoSum(self, nums: List[int], target: int):
        for i in range(0, len(nums)):
            a = nums[i]
            for j in range(i+1, len(nums)):
                b = nums[j]
                if a+b == target:
                    return [i, j]

# 시간 복잡도 O(n)
class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i + 1
            else:
                return map[num[i]], i + 1

        return -1, -1