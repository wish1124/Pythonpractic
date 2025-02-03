def main():
    x = eval(input("Enter a number: "))
    for i in range(x):
        star_count = 2 * i + 1
        space_count = x - i - 1
        print(" " * space_count, end="")
        print("*" * star_count)
        
        
if __name__ == "__main__":
  main()
  
  