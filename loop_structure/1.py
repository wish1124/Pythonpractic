def main():
  # fileName = input("What file are the numbers in? ") 
  fileName = "numbers.txt"
  infile = open(fileName,'r')
  sum = 0.0
  count = 0
  line = infile.readline()
  print("line: ", line)
  while line != "":
      splitLine = line.split(",")
      print("splitLine: ", splitLine)
      for xStr in line.split(","):
          sum = sum + eval(xStr)
          count = count + 1
      line = infile.readline()
      print("line: ", line)
  print("\nThe average of the numbers is", sum / count)
  
if __name__ == "__main__":
  main()