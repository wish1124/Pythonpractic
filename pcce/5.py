def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr: # ["respiration", "repeat", "check", "pressure", "call"]
        for i in range(len(basic_order)):
            if action == basic_order[i]:
                print(i)
                answer.append(i+1)
    return answer
  
# Input: ["respiration", "repeat", "check", "pressure", "call"]
# Output: [4, 5, 1, 3, 2]

input = ["respiration", "repeat", "check", "pressure", "call"]

print(solution(input)) # ["check", "call", "pressure", "respiration", "repeat"]
