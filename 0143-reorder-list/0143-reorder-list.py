# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        first_half = head

        second_half_reversed = self._reverseList(mid)

        self._mergeLists(first_half, second_half_reversed)

    def _reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

    def _mergeLists(self, l1: ListNode, l2: ListNode) -> None:
        while l1 and l2:
            l1_next_temp = l1.next
            l2_next_temp = l2.next

            l1.next = l2
            if l1_next_temp:
                l2.next = l1_next_temp

            l1 = l1_next_temp
            l2 = l2_next_temp