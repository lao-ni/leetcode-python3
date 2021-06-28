# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        curr=head
        pre=sentinel
        #print(curr.val,val)
        while curr:
            if curr.val==val:
                pre.next=curr.next
                #print(pre)
                #print(head)
            else:
                pre=curr
            curr=curr.next
        return sentinel.next
