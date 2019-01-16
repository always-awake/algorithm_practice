# input: [3,2,3], [2,2,1,1,1,2,2] ... (list)
# output: 3, 2 ... (int)


class Solution:
    def majorityElement(self, nums):
        
        result_dict = {}
        
        # nums를 순회하면서, nums 내 숫자 i의 개수를 key로, 숫자 i 를 value로 저장
        for i in set(nums):
            result_dict[nums.count(i)] = i
        
        # result_dict의 모든 key 중 가장 큰 값(=more than n/2)을 갖는 key를 구함
        dic_max = max(result_dict.keys())
        
        # 해당 key값의 value를 return
        return result_dict[dic_max]