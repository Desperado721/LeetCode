class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.bt(nums, 0, [], res)
        return res
    def bt(self, nums, idx, tempList, res):
        res.append(tempList)
        for i in range(idx, len(nums)):
            self.bt(nums, i+1, tempList+[nums[i]], res)