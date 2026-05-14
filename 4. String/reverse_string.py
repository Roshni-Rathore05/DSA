# print reverse of string
str="roshni"
s=""
for i in range(len(str)-1,-1,-1):
  s+=str[i]
print(s)

# reverse string
# using left right pointer
st="roshni"
arr=list(st)
left=0
right=len(arr)-1
while left<=right:
  arr[left],arr[right]=arr[right],arr[left]
  left+=1
  right-=1
rev=" ".join(arr)
print(rev)

# using recurtion
def rev(arr,l,r):
  if l>r:
    return arr
  arr[l],arr[r]=arr[r],arr[l]
  return rev(arr,l+1,r-1)
st="roshni"
arr=list(st)
left=0
right=len(arr)-1
reverse=rev(arr,left,right)
print(type(" ".join(reverse)))

