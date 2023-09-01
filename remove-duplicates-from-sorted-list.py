class Solution:
    def deleteDuplicates(self, ls: Optional[ListNode]) -> Optional[ListNode]:
        prev = curr = dummy = ListNode()
        while ls:
            if prev != ls.val:
                curr.next = ListNode(ls.val)
                curr = curr.next
            prev = ls.val
            ls = ls.next
        return dummy.next
