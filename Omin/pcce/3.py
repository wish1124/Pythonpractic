# import ipdb

# ipdb.set_trace()

number = int(input()) # 2^31 - 1 = 2147483647
# Input: 4859 

answer = 0 # 48 + 59

while number > 0:
    print("number: ", number, "answer: ", answer)
    print("number % 100: ", number % 100)
    answer += number % 100 # 48 -> 48
    
    # answer = answer + number % 100
    
    print("number // 100: ", number // 100)
    number //= 100 # 0048 -> 0
    # number = number // 100

print(answer)