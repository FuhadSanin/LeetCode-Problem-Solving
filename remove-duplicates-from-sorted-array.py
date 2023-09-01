class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i+1

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         for i in nums:
#             c = nums.count(i)
#             if c > 1:
#                 for _ in range(c-1):
#                     nums.remove(i)

#         return len(nums)
