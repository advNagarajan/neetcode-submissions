class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        new = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = new[-1]

            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                new.append(intervals[i])

        return new
