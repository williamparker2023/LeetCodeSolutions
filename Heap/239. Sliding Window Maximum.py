"""
Hard

You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves 
right by one position.

Return the max sliding window.

Basically return a new array where at every index, ans[i] is equal to the biggest
number between nums[i] and nums[k]
"""

"""
Whenever I see a problem that requires finding the max of something a bunch of times,
my brain goes to trying to use a heap. There are also tree and dequeue solutions here,
but in my opinion the heap/sliding window strategy makes the most sense and is
the most readable.

The idea is that we have a max heap storing all of the (nums[j], j) pairs,
and at every index i we find the first max value in the heap such that 
the j value associated with it is within our current i - k window.
"""

import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        initialFreq = {}
        big = nums[0]
        ans = [0]*(len(nums)+1-k)
        for i in range(k):
            if -nums[i] not in initialFreq:
                initialFreq[-nums[i]] = 0
            initialFreq[-nums[i]] = i
        
        heap = []
        for key in initialFreq:
            heap.append((key,initialFreq[key]))
        heapq.heapify(heap)
        
        
        for i in range(len(nums)-k+1):
            heapq.heappush(heap,(-nums[i+k-1],i+k-1))
            while heap[0][1]<i:
                heapq.heappop(heap)
            if heap[0][1]>=i:
                ans[i] = -heap[0][0]
            
        
        return ans