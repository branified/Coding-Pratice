Harvard CS50 Algorithms Course
https://learning.edx.org/course/course-v1:HarvardX+CS50+X/block-v1:HarvardX+CS50+X+type@sequential+block@cf1f9844062147a6bd68e9348a8eb946/block-v1:HarvardX+CS50+X+type@vertical+block@03a700bf59d042a4bc3c8a7d56ad421d

How algorithms work with computers. Human bird's eye vision vs computer hidden vision. Time complexities. Optimization and sorting

Leetcode
https://leetcode.com/problems/rotate-image/

```
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
#Brute force solution
```
