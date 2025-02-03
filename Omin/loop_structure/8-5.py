import math

def main():
    x = eval(input("Enter a number: "))
    for i in range(3,x+1):
        is_prime = True
        for j in range(2,math.sqrt(x)+1):
          # 소수를 확인하기 위해서는 2부터 sqrt(i) 까지만 j 를 증가시키면서 확인하면 된다.
          if i % j == 0:
            is_prime = False
            break
        if is_prime == True:
            print(i, "is a prime number")

if __name__ == "__main__":
    main()