# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result=ListNode(0)
        cur=result
        carry=0
        while l1 or l2:
            sum=0
            if l1:
                sum=sum+l1.val
                l1=l1.next
            if l2:
                sum=sum+l2.val
                l2=l2.next
            sum=sum+carry
            carry=sum//10
            cur.next=ListNode(sum%10)
            cur=cur.next
        if carry==1:
            cur.next=ListNode(1)
        return result.next

        
