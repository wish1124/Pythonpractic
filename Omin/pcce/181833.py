def solution(n):
    answer = []

    for i in range(0, n): # n 번 반복
      answer.append([])  # answer = [ [0, 0, 0], [] ]
      for j in range(0, n): # n 번 반복
        if i == j:
          answer[i].append(1)
        else:
          answer[i].append(0) # answer = [[0, 0, 0, 0, ....]]
    print(answer) 