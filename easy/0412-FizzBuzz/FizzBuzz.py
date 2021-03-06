from typing import List

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def fizzBuzz(self, n: int) -> List[str]:
        list = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                list.append("FizzBuzz")
            elif i % 5 == 0:
                list.append("Buzz")
            elif i % 3 == 0:
                list.append("Fizz")
            else:
                list.append(str(i))
        return list

# test
solution = Solution()
print(solution.fizzBuzz(3))
print(solution.fizzBuzz(5))
print(solution.fizzBuzz(15))