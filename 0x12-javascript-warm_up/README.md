0x12. JavaScript - Warm up 

Requirements
General

    Allowed editors: vi, vim, emacs
    All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/node
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should be semistandard compliant (version 16.x.x). Rules of Standard + semicolons on top. Also as reference: AirBnB style
    All your files must be executable
    The length of your files will be tested using wc

Tasks
0. First constant, first print
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that prints “JavaScript is amazing”:

    You must create a constant variable called myVar with the value “JavaScript is amazing”
    You must use console.log(...) to print all output
    You are not allowed to use var


1. 3 languages
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that prints 3 lines:

    The first line: “C is fun”
    The second line: “Python is cool”
    The third line: “JavaScript is amazing”
    You must use console.log(...) to print all output
    You are not allowed to use var


2. Arguments
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that prints a message depending of the number of arguments passed:

    If no arguments are passed to the script, print “No argument”
    If only one argument is passed to the script, print “Argument found”
    Otherwise, print “Arguments found”
    You must use console.log(...) to print all output
    You are not allowed to use var

Reference: process.argv


3. Value of my argument
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that prints the first argument passed to it:

    If no arguments are passed to the script, print “No argument”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You are not allowed to use length


4. Create a sentence
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that prints two arguments passed to it, in the following format: “ is ”

    You must use console.log(...) to print all output
    You are not allowed to use var


5. An Integer
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

    If the argument can’t be converted to an integer, print “Not a number”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You are not allowed to use try/catch


6. Loop to languages
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

    The first line: “C is fun”
    The second line: “Python is cool”
    The third line: “JavaScript is amazing”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You are not allowed to use any if/else statement
    You can use only one console.log
    You must use a loop (while, for, etc.)


6. Loop to languages
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

    The first line: “C is fun”
    The second line: “Python is cool”
    The third line: “JavaScript is amazing”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You are not allowed to use any if/else statement
    You can use only one console.log
    You must use a loop (while, for, etc.)

8. Square
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that prints a square

    The first argument is the size of the square
    If the first argument can’t be converted to an integer, print “Missing size”
    You must use the character X to print the square
    You must use console.log(...) to print all output
    You are not allowed to use var
    You must use a loop (while, for, etc.)

9. Add
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that prints the addition of 2 integers

    The first argument is the first integer
    The second argument is the second integer
    You have to define a function with this prototype: function add(a, b)
    You must use console.log(...) to print all output
    You are not allowed to use var

10. Factorial
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that computes and prints a factorial

    The first argument is integer (argument can be cast as integer) used for computing the factorial
    Factorial of NaN is 1
    You must do it recursively
    You must use a function
    You must use console.log(...) to print all output
    You are not allowed to use var


11. Second biggest!
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a script that searches the second biggest integer in the list of arguments.

    You can assume all arguments can be converted to integer
    If no argument passed, print 0
    If the number of arguments is 1, print 0
    You must use console.log(...) to print all output
    You are not allowed to use var


12. Object
mandatory
Score: 0.0% (Checks completed: 0.0%)

Update this script to replace the value 12 with 89:

    You are not allowed to use var


13. Add file
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a function that returns the addition of 2 integers.

    The function must be visible from outside
    The name of the function must be add
    You are not allowed to use var

14. Const or not const
#advanced
Score: 0.0% (Checks completed: 0.0%)

Write a file that modifies the value of myVar to 333


15. Call me Moby
#advanced
Score: 0.0% (Checks completed: 0.0%)

Write a function that executes x times a function.

    The function must be visible from outside
    Prototype: function (x, theFunction)
    You are not allowed to use var


16. Add me maybe
#advanced
Score: 0.0% (Checks completed: 0.0%)

Write a function that increments and calls a function.

    The function must be visible from outside
    Prototype: function (number, theFunction)
    You are not allowed to use var


17. Increment object
#advanced
Score: 0.0% (Checks completed: 0.0%)

Update this script by adding a new function incr that increments the integer value.

    You are not allowed to use var
