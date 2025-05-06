Download [Python](https://www.python.org/)

git clone https://github.com/bjanusek00/pascals_triangle.git

to desktop:

cd to folder and run program: 

```
py pascal.py
```
/////////////////////////////////////////////////////////////////////

Program Description:

Write a program to print a limited Pascal's Triangle. First, the user is instructed to enter the number of
rows to be displayed, and is prompted to enter an integer in the range [1 ... 13]. The user enters a
number, **x**, and the program verifies that 1 <= **x** <= 13. If x is out of range, the user is re-promted until
they enter a value in the specified range. The program then calculates and displays the first **x** rows of
Pascal's Triangle.

Program Requirements
1. The programmer's name and program title must appear in the output.
2. The **main** procedure must consist of only procedure calls (with any necessary framing). It should be
    a readable "list" of what the program will do.
3. Each procedure will implement a section of thte program logic, i.e., each procedure will specify how
   the logic of its section is implemented. The program must be modularized into at ***least*** the following
    procedures and sub-procedures:
    - **introduction** - Introduce the Program and Programmer
    - **getUserInput** - Prompt for and receives number of rows of Pascal's Triangle to print. Prints this number of
        rows of Pascal's Triangle. Uses **printPascalRow** to print each line.
        - **nChooseK** - Receives two values, n and k. Outputs the result of "n Choose k" computation.
             See [Binomial Coefficient Wikipedia Article](https://en.wikipedia.org/wiki/Binomial_coefficient) for more details.
        - **printPascalRow** - Receives index of row to be printed. Prints all elements of Pascal's Triangle
            for this row. Uses **nChooseK** procedure to obtain each element to be printed.
        - **farewell** Thanks user for using the program.
- The upper and lower bounds of user input must be defined as **constants**.
- The **USES** directive is not allowed on this project.
- If the user enters a number outside the range [1 ... 13] an error message must be displayed and the
  user must be prompted to re-enter the number of lines of the Triangle to be shown.

  [Recursion (computer science)](https://en.wikipedia.org/wiki/Recursion_(computer_science))

  [Factorial: wikipedia](https://en.wikipedia.org/wiki/Factorial)

  ```
  int fac1(int n) {
   if (n <= 0)
      return 1;
   else
      return fac1(n-1)*n;
}
```
  
