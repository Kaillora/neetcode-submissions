"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [interval.start for interval in intervals]
        ends = [interval.end for interval in intervals]
        starts.sort()
        ends.sort()

        i, j = 0, 0
        used_rooms = 0
        max_rooms = 0
        
        while i < len(starts):
                if starts[i] < ends[j]:
                    used_rooms += 1
                    max_rooms = max(max_rooms, used_rooms)
                    i += 1
                else:
                    used_rooms -= 1
                    j += 1
        return max_rooms