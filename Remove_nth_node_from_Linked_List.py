# Complete Python Program to Remove Nth Node From End of Linked List

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):

        # Create dummy node
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Move fast pointer n+1 steps ahead
        for i in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove nth node from end
        slow.next = slow.next.next

        return dummy.next


# Function to create linked list
def createLinkedList(arr):

    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# Function to print linked list
def printLinkedList(head):

    result = []

    while head:
        result.append(head.val)
        head = head.next

    print(result)


# ---------------- MAIN PROGRAM ----------------

solution = Solution()

# Example 1
head1 = createLinkedList([1, 2, 3, 4, 5])
n1 = 2

newHead1 = solution.removeNthFromEnd(head1, n1)

print("Output for Example 1:")
printLinkedList(newHead1)


# Example 2
head2 = createLinkedList([1])
n2 = 1

newHead2 = solution.removeNthFromEnd(head2, n2)

print("Output for Example 2:")
printLinkedList(newHead2)


# Example 3
head3 = createLinkedList([1, 2])
n3 = 1

newHead3 = solution.removeNthFromEnd(head3, n3)

print("Output for Example 3:")
printLinkedList(newHead3)