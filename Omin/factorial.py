

# 1! = 1
# 2! = 2 * 1 = 2
# 3! = 3 * 2 * 1 = 6
# ...
# n! = n * (n-1) * (n-2) * ... * 1
# n! = n * (n-1)!



# 100! = 100 * 99!
# 99! = 99 * 98!
#...

# 2! = 2 * 1!
# 1! = 1





def factorial(n):
  if n == 1:
    return 1
  print("pre visit of ", n)
  answer = n * factorial(n-1)
  print("post visit of ", n)
  return answer


# factorial(5) -> factorial(4) -> ... -> factorial(1) 

factorial(5) # 5 * 4 * 3 * 2 * 1 = 120




