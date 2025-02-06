# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_recursive(self, head):
        if not head:
            return head
        newHead = head
        if head.next:
            newHead = self.reverse_recursive(head.next)
            head.next.next = head
        head.next = None
        return newHead

    def reverse_iterative(self, head):
        parent = None
        current = head
        while current:
            child = current.next
            current.next = parent
            parent = current
            current = child
        return parent

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.reverse_recursive(head)
        return self.reverse_iterative(head)