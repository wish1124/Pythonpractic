def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        print("storage: ", storage[i])
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            print("pos: ", pos)
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i])
            clean_num.append(num[i])
            
        print("clean storage: ",clean_storage)
        print("clean num: ", clean_num)
        print(" ")
        print(" ")
            
    # 아래 코드에는 틀린 부분이 없습니다.
    max_num = max(clean_num)
    answer = clean_storage[clean_num.index(max_num)]
    return answer
  
  
storage = ["book", "pencil", "pencil", "book"]
num = [2, 4, 3, 1]

print(solution(storage, num)) # pencil