08/24/2022

https://www.youtube.com/watch?v=xvEKQefqQ7A&ab_channel=Simplilearn

Chapter 1- Data Science Tools and Day to Day
Tools used by Data Scientists. The workflow of Data Science Projects. Knowledge required for Data Scientists

https://www.simplilearn.com/tutorials/data-science-tutorial/data-science-interview-questions

Data Science Technical Interview Questions

Leetcode

https://leetcode.com/problems/power-of-three/- Python

```
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #1162261467 comes from 3^19 which is the highest power of 3 that exists in the constraints.
        return (n > 0) and 1162261467 % n == 0
```

https://leetcode.com/problems/two-sum/ -Python

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]

#Brute force method: O(n^2) Time
```

https://leetcode.com/problems/combine-two-tables/ -MySQL

```
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
;
```
Future reference: Look up hashmaps
