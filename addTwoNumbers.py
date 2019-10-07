""" You are given two non-empty linked lists representing two non-negative
    integers. The digits are stored in reverse order and each of their nodes
    contain a single digit. Add the two numbers and return it as a linked list.
    You may assume the two numbers do not contain any leading zero, except the
    number 0 itself.
    """
# Example
""" Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
    """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# """class Solution:
#    def addTwoNumbers(self, l1, l2):
#        """
#        :type l1: ListNode
#        :type l2: ListNode
#        :rtype: ListNode
#        """


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class solution:
    def addTwoNumbers(self, l1, l2):
        result = Node()
        current = result
        carry = 0

        while l1 or l2:
            value = carry
            if l1:
                value += l1.value
                l1 = l1.next
            if l2:
                value += l2.value
                l2 = l2.next
            carry, value = divmod(value, 10)
            current.next = Node(value)
            current = current.next

        if carry > 0:
            current.next = Node(carry)

        return result.next
