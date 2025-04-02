class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        currInd = 0
        nextInd = 1
        addingNumsList = []

        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    addingNumsList.append(i)
                    addingNumsList.append(j)
                    return addingNumsList