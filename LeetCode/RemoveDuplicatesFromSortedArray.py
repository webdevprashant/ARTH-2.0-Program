nums = [0,0,1,1,1,2,2,3,3,4]

def removeduplicatesfromarray(arr):
   #s = set(arr)
   #l = len(s)
   #return l
   visited = []
   while not len(nums) == len(visited):
        for i in nums:
           if i not in visited:
               visited.append(i)
           else:
               visited.append("_")
   return visited
   
print(removeduplicatesfromarray(nums))