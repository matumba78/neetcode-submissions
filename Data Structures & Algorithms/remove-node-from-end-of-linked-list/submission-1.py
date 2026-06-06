# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_list = 0
        curr = head
        while curr:
            curr = curr.next
            len_list += 1
        req_length = len_list - n
        if req_length == 0:
            return head.next
        curr = head
        ct = 0
        while curr:
            print(ct, req_length)
            if ct + 1 == req_length:
                curr.next = curr.next.next
                break
            curr = curr.next
            ct += 1
        return head

        