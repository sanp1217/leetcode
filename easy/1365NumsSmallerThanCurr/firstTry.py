class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        smallerThan = []
        for numToCompare in nums:
            for num in nums:
                if numToCompare == num:
                    continue
                if num < numToCompare:
                    count += 1
            smallerThan.append(count)
            count = 0

        return smallerThan

# O(n^2) runtime