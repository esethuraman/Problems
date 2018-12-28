class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = loc_count = 0
        if nums:
            prev = nums[0]
            loc_count = -1
        for n in nums:
            if n > prev:
                loc_count += 1
            else:
                max_count = loc_count if (loc_count > max_count) else max_count
                loc_count = 1
            prev = n
        return max(max_count, loc_count)

