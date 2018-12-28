class Permutations:

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.permute_helper(nums, 0, len(nums)-1, res)
        if not res:
            return [[]]
        print(res)

    def permute_helper(self, nums, l, r, res):
        if r == l:
            this_nums = [i for i in nums]
            res.append(this_nums)
        else:
            for i in range(l, r+1):
                nums[i], nums[l] = nums[l], nums[i]
                self.permute_helper(nums, l+1, r, res)
                nums[i], nums[l] = nums[l], nums[i]


obj = Permutations()
obj.permute([1, 2, 3, 4])
