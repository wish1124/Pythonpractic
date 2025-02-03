def main():
    n = eval(input("Enter a number: "))
    a = 1 
    b = 1
    
    for i in range(n -2):
        c = a + b
        a = b 
        b = c
    
    print("The nth Fibonacci number is", c)
    
    
    
if __name__ == "__main__":
    main()