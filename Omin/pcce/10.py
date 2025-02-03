def can_place(mats, park, r, c, s):
    for i in range(s):
      for j in range(s):
        if r+i >= len(park) or c+j >= len(park[0]):
          return False
        if park[r+i][c+j] != "-1":
          return False
    return True



def solution(mats, park):
    rows = len(park) # 6
    cols = len(park[0]) # 8
    
    mats.sort(reverse=True)
    
    for s in mats:
        for r in range(rows):
            for c in range(cols):
                is_place =  can_place(mats, park, r, c, s)
                if is_place == True:
                    return s
                else:
                    continue

  
def main():
    mats = [5,3,2]
    park = [["A", "A", "-1", "B", "B", "B", "B", "-1"], 
            ["A", "A", "-1", "B", "B", "B", "B", "-1"], 
            ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], 
            ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], 
            ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], 
            ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]
    
    print(solution(mats, park))    
  
  
if __name__ == "__main__":
    main()