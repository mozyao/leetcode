from max_area_island import Solution
from typing import List
from heapq import heappush, heappop


class Solution:

    def overlapping(self, inter1:List[int],inter2:List[int]) -> bool:
        if inter1[0]<=inter2[0] <=inter1[1]:
            return True
        return False



    def merge(self,intervals: List[List[int]]) -> List[List[int]]:
        heap,sorted_intervals,ans = [],[],[]

        for interval in intervals:
            heappush(heap,interval)

        ans.append(heappop(heap))
        while heap:
            sorted_intervals.append( heappop(heap))
        
        for interval in sorted_intervals:
            if not self.overlapping(ans[-1],interval):
                ans.append(interval)
            else:
                ans[-1][1]=max(ans[-1][1],interval[1])
        return ans

        
intervals = [[1,3],[2,6],[8,10],[15,18]]

if __name__=="__main__":
    x=Solution()
    


    print(x.merge(intervals))



