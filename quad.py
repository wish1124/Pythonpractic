def solution(dot):
  quad = [(3,2),(4,1)]
  
  x = dot[0] > 0 
  
  print("x : ", x) # True
  
  a = [1,2,3,4,5]
  
  print("a[x]: ", a[False]) # True -> 1 False -> 0
  
  
  return quad[dot[0]>0][dot[1]>0]



print(solution([5,-10])) # 1

