class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap={}
        for i,v in enumerate(nums):
            diff=target-nums[i]
            if diff in HashMap:
                return [HashMap[diff],i]
            else:
                HashMap[v]=i
            