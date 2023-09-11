from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        skip = 0

        if len(intervals) == 1:
            return intervals

        for i in range(len(intervals)):
            if i + 1 < len(intervals):
                if skip == 1:
                    skip = 0
                    continue
                if intervals[i][1] < intervals[i+1][0]:
                    res.append(intervals[i])
                    res = res + intervals[i+1:]
                    skip = 0
                else:
                    res.append([min(intervals[i][0], intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1])])
                    #res = res + intervals[i+2:]
                    skip = 1
                
        #res.append(intervals)

        return res

intervals = [[1,4],[0,2],[3,5]]
solution = Solution()
print(solution.merge(intervals)) 