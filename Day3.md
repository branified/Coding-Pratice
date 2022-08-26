08/25/2022

https://www.youtube.com/watch?v=xvEKQefqQ7A&ab_channel=Simplilearn

Chapter 3- Linear Regression
What is Linear Regression. How to calculate it using data and when to use it. Y = mx+b

Leetcode

https://leetcode.com/problems/add-two-numbers/

```
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        curr = result
        carry = 0
        
        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result.next
```

Linked Lists

Future reference- look at Linked Lists and what they do
