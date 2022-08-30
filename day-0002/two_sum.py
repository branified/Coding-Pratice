from collections import defaultdict

class Solution:
    # Another solution:
    # keep a map of number needed per diff
    # E.g. when you see 2 at index 0: m[9-2] = [0]
    # see 8 at index 1: m[9-8] = [1]
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        complement = defaultdict(set)
        for i in range(len(nums)):
            print(f"[{i}] = {nums[i]}, C[{target - nums[i]}] now includes {i}")
            complement[target - nums[i]].add(i)
        for i in range(len(nums)):
            this_complement = complement[nums[i]]
            print(f"Checking [{i}]\n\tC[{i}] = {this_complement}")
            if len(this_complement) > 0:
                return i, list(this_complement)[0]

def main():
  l = [2, 8, 7, 1, -1, -10]
  target_num = 9

  s = Solution()

  print(s.twoSum2(l, target_num))


if __name__ == '__main__':
  main()
