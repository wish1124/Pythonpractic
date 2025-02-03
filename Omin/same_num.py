def solution(arr):
  answer = []
  for i in range(len(arr)): # i = 0, 1 , 2, 3, 4, 5, 6
    if i == 0:
      answer.append(arr[i])
    else:
      if arr[i] != arr[i-1]:
        answer.append(arr[i])
    
  return answer
  
  
arr = [1,2,1,2,1,2,1]

print(solution(arr)) # [1,3,0,1]