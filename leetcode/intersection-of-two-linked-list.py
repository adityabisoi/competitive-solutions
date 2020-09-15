# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        arr = {}
        while headA != None:
            arr[headA] = 0
            headA = headA.next
        while headB != None:
            if headB in arr.keys():
                return headB
            headB = headB.next

        return None
