class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # [[1,1], [3,4], [-1, 0]]
        totalSecs = 0
        for i in range(len(points) - 1):
            curr = points[i]
            next = points[i + 1]

            maxNumOfSecs = max(abs(next[0] - curr[0]), abs(next[1] - curr[1]))

            totalSecs += maxNumOfSecs

        return totalSecs