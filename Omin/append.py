
# solution1
def solution1(message):
  answer = 0
  for i in range(len(message)):
    if message[i] != " ":
      answer += 2
  return answer


# solution2 : remove the " " character in message

def solution2(message):
  
  print(message.replace(" ", "d"))
  
  return 2* len(message.replace(" ", ""))




print(solution1("abc def")) # 6
print(solution2("abc def")) # 6
    