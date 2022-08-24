*Java Programming Assesment. NDA*

-understanding of iterators
-Class creation
-Running code on VM and fixing errors
-Debugging: Understanding error messages and how to fix them: NullPointerException
-XOR Base64 Encoding and Decoding: Python

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
            return False
