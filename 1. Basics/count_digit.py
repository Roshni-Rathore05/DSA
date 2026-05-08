count digit of elements 
Brute Force:
def countDigit(n: int) -> int:
  count=0
  digit=n%10
  count+=1
  n=n//10
  return count
  
optimal solution:
def countDigit(n: int) -> int:
   return int(log10(n)+1)
   pass
