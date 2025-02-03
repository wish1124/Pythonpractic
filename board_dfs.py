def solution(board, h, w):
    answer = 0
    #
    if (h-1)>= 0 and board[h-1][w] == board[h][w]:
      answer += 1  
    #
    if (h+1) < len(board) and board[h+1][w] == board[h][w]:
      answer += 1     
    #
    if (w-1) >= 0 and board[h][w-1] == board[h][w]:
      answer += 1
    #
    if (w+1) < len(board[0]) and board[h][w+1] == board[h][w]:
      answer += 1
    return answer
  
  
  
# board = 4 x  20
# h = 0, 1, 2, 3
# w = 0, ..., 19


  
  
board = [["red", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
h = 1
w = 1

print(solution(board, h, w)) #2