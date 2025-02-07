def solution(my_string, is_suffix):
    answer = 0 # False
    for i in range(len(my_string)):
      token = my_string[i:]
      if token == is_suffix:
        answer = 1 # True
        
    if answer == False:
      return 0 # 없다라는 내용을 리턴
      

print(solution("banana", "nan")) # Expected output: 1





a= [1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 1, 10, 1, 1, 2, 1, 3, 1, 1]



answer = 0
for i in a:
  if i > 5:
    answer = 1
  else:
    pass
  
  
  
if answer == 0:
  print("없다")

else:
  print("있다")