def solution(x, n):

  answer = []
  for i in range(n): # i = 0, 1, 2, 3, 4
    answer.append(x*(i+1))
  return answer
  
  
print(solution(2,5)) # [2,4,6,8,10]