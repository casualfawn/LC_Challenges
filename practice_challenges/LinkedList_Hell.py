

## use slow and fast fo find the middle

def findmid(list1):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    dummy = ListNode()
    tail = dummy = ListNode()
    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    if left:
        tail.next = left
    if right:
        tail.next = right

    return dummy.next



left = head
right = self.findmid(head)
tmp = right.next
right.next = None
right = tmp


left = self.sortList(left)
right = self.sortList(right)
return self.merge(left, right)





def findmid(head):

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def mergelist(left, right):
    tail = dummy = listNode()
    while left and right:
        if left.next < right.next:
            tail.next = left.next
            left = left.next
        if left.next >= right.next:
            tail.next = right.next
            right = right.next
    tail = tail.next
    if left:
        tail.next = left
    if right:
        tail.next = right
    return dummy.next
