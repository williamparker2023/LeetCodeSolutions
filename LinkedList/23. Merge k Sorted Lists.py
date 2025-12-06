"""
Hard

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

https://leetcode.com/problems/merge-k-sorted-lists/description/
"""

"""
This one is basically just a mix of heaps and linked lists. We maintain a min heap of 
the current smallest elements of each linked list. We pop the smallest element from the heap
and add it to our answer linked list. Then we push the next element from that same linked list 
into the heap if the current one has a next. We repeat this process until the heap is empty.
"""

import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []
        for i in range(len(lists)):
            if lists[i] is None:
                continue
            heap.append( (lists[i].val, lists[i]) )
        heapq.heapify(heap)

        if len(heap)==0:
            return None

        firstVal, firstNode = heapq.heappop(heap)
        head = ListNode()
        head.val = firstVal
        ans = head
        if firstNode.next:
            heapq.heappush(heap, (firstNode.next.val, firstNode.next) )
        
        
        while len(heap)>0:
            curVal, curNode = heapq.heappop(heap)
            nextNode = ListNode()
            nextNode.val = curVal
            ans.next = nextNode
            ans = ans.next

            if curNode.next:
                heapq.heappush(heap, (curNode.next.val, curNode.next))
        return head