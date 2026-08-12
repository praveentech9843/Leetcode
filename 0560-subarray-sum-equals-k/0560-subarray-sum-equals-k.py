class Solution:
    def subarraySum(self, nums, k):

        count = {0: 1}

        total = 0
        answer = 0

        for num in nums:

            total += num

            needed = total - k

            if needed in count:
                answer += count[needed]

            if total in count:
                count[total] += 1
            else:
                count[total] = 1

        return answer