import math

def main():
    print("This program finds the real solutions to a quadratic")
    
    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
        discrim = b * b - 4 * a * c
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2)
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No Real Roots")
        else:
            print("Invalid input")
    except NameError:
        print("Invalid input")
    #else
    except SyntaxError:
        print("Syntax Error")

    
  
    
if __name__ == '__main__':
    print("main is called")
    print("math.__name__ is", math.__name__)
    main()