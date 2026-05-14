def isPalindrome(s):

  result=''.join([char for char in s if char.isalnum()])
  st=result.lower()
  arr=list(st)
  left=0
  right=len(arr)-1
  while left<=right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
  rev=''.join(arr)
  if st==rev:
    print("t")
  else:
    print("F")
s="A man, a plan, a canal: Panama"
isPalindrome(s)
