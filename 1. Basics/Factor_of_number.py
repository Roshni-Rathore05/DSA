Examples:

Input: n = 5
Output: 2
Explanation: 5 has 2 factors 1 and 5
Input: n = 25
Output: 3
Explanation: 25 has 3 factors 1, 5, 25 

brute force:
n=15
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
print(l)

better solution:

n=15
l=[]
for i in range(1,n//2):
    if n%i==0:
        l.append(i)
print(l)


Optimal solution:
from math import sqrt
class Solution:
    def countFactors (self, n):
        count = 0
        for i in range(1, int(sqrt(**0.5)) + 1):
            if n % i == 0:
                if i == n // i:
                    count += 1   # perfect square case
                else:
                    count += 2   # pair of factors

        return count
