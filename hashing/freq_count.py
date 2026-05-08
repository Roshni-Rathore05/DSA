# counting freqency
# brute force 
arr=[1,5,3,5,1,5,3,5,7,7]
fre_map={}
for i in range(0,len(arr)):
  if arr[i] in fre_map:
    fre_map[arr[i]]=+1
  else:
    fre_map[arr[i]]=1
fre_map

# optimal solution
arr=[1,5,3,5,1,5,3,5,7,7]
fre_map={}
for i in range(0,len(arr)):
  fre_map[i]=fre_map.get(arr[i],0)+1
print(fre_map)

# .get(ind,0)  (if value not exists , return 0 else return value)
