class Solution:
    def maxSubarraySumCircular(self, nums):

        total = sum(nums)

        currentMax = maximum = nums[0]
        currentMin = minimum = nums[0]

        for num in nums[1:]:

            currentMax = max(num, currentMax + num)
            maximum = max(maximum, currentMax)

            currentMin = min(num, currentMin + num)
            minimum = min(minimum, currentMin)

        if maximum < 0:
            return maximum

        return max(maximum, total - minimum)