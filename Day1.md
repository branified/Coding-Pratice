*Java Programming Assesment. NDA*

*Leetcode Exercises*
https://leetcode.com/problems/palindrome-linked-list/

```class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        ls = []
        while head != None:
            ls.append(head.val)
            head = head.next
            
        if ls == ls[::-1]:
            return True
        else: 
            return False```
