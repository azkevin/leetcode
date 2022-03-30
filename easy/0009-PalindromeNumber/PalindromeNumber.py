class Solution:
    # Time Complexity: O(log n)
    # Space Complexity: O(n)
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        reverseNum = 0
        while temp > 0:
            reverseNum = (reverseNum * 10) + (temp % 10)
            temp = temp // 10
        return reverseNum == x

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isPalindromeBF(self, x: int) -> bool:
        reverse = str(x)[::-1]
        return reverse == str(x)

solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))