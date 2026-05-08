
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1


Potential Edge Cases:
Negative Numbers:
Negative numbers should immediately return False.
Single-Digit Numbers:
Any single-digit number should return True as it is inherently a palindrome (e.g., x = 5).
Zero:
x = 0 should return True as it reads the same forward and backward.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        sign=-1 if x <0 else 1
        num=x
        rev=0
        while num>0:
            digit=num%10
            rev=rev*10+digit
            num=num//10
        rev=rev*sign
        if rev==x:
            return True
        else:
            return False
