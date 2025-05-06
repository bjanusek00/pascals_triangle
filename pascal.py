###########################
# Benjamin Gregory Janusek
# CSUN 2017
# 2/25/2025
###########################

# calculates factorial for input n
def factorial (n):
    if (n <= 0):
      return 1;
    else:
      return factorial(n-1)*n;

# calculates binomial coefficient for n choose k
def nChooseK (n, k):
  return factorial(n) / (factorial(k) * factorial(n - k))

# builds a string of for desired row of pascal's triangle
def printPascalRow(n):
  numbers = "";
  a = 0;
  while(a <= n):
    numbers += (str(round(nChooseK(n, a)))) + " ";
    a = a + 1;

  return numbers;

# prints pascals triangle from 0 until whatever value input for n
def printPascalTriangle(n):
  print("");
  a = 0;
  while(a < n-1):
    print(printPascalRow(a))
    a = a + 1;

# introduction
def introduction ():
  a = "Programmer: Benjamin Gregory Janusek"
  b = ""
  c = """Program: Write a program to print a limited Pascal's Triangle. First, the user is instructed to enter the number of
rows to be displayed, and is prompted to enter an integer in the range [1 ... 13]. The user enters a 
number, x, and the program verifies that 1 <= x <= 13. If x is out of range, the user is re-prompted until
they enter a value in the specified range. The program then calculates and displays the first x rows of Pascal's Triangle"""

  print(a);
  print(b);
  print(c);

# getUserInput
def getUserInput():
  val = int(input("Please enter an integer that is: 1 >= x <= 13:  "))
  print("");

  if ((val < 1) or (val > 13)):
    print("Out of Bounds: Try again");
    print("");
    getUserInput();

  return val;

# fareWell
def fareWell():
  print("Thanks for Playing, Farewell")

# main
def main():
  introduction();
  print("");
  printPascalTriangle(getUserInput());
  print("");
  fareWell();

main();
