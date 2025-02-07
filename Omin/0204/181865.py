def solution(binomial):
    answer = 0
    # binomial : (number, operator, number)
    if "+" in binomial:
      list = binomial.split("+")
      answer = int(list[0]) + int(list[1])
      
    elif "-" in binomial:
      list = binomial.split("-")
      answer = int(list[0]) - int(list[1])
      
    elif "*" in binomial:
      list = binomial.split("*")
      answer = int(list[0]) * int(list[1])
    
    return answer
  
  
  
  
  
#custom split function
def split(sentence, delimiter):
    result = []
    temp = ""
    for i in sentence:
        print(temp)
        if i == delimiter:
            result.append(temp)
            temp = ""
        else:
            temp += i
    result.append(temp)
    return result