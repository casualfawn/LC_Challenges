class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class sol:

    def addlists(self, l1:ListNode, l2 = ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            l1num = l1.val
            l2num = l2.val
            value = l1num + l2num
            carryval = value // 10
            value = value % 10
            cur.next = ListNode(value)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next






# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next  # by 1
            fast = fast.next.next  # by 2 once out of bounds we hit mid
        return slow

    def merge(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # split list into halves
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
