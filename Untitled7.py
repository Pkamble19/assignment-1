#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT 3

# # Q.1 Why are functions advantageous to have in your programs?

# ANS. Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update. The main advantage of functions is code Reusability.

# # Q.2 When does the code in a function run: when it&#39;s specified or when it&#39;s called?

# ANS. The code in a function executes when the function is called, not when the function is specified.

# # Q.3 What statement creates a function?

# ANS . The def statement defines a function
# 
# Syntax of Function:
# 
# def function_name(parameters):
# 
#     """doc string"""          
#     -----function body-----
#     -----function body-----
#     return value

# # Q.4. What is the difference between a function and a function call?

#  function is procedure to achieve a particular result. while function call is using this function to achive that task. Using a function to do a particular task any point in program is called as function call.

# # Q.5. How many global scopes are there in a Python program? How many local scopes?

# There is one global scope, and a local scope is created whenever a function is called.

# # Q.6. What happens to variables in a local scope when the function call returns?
# 

# |Ans: When a function returns, the local scope is destroyed, and all the variables in it are forgotten.

# # Q.7. What is the concept of a return value? Is it possible to have a return value in an expression?
# 

# Ans: A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression.

# # Q.8. If a function does not have a return statement, what is the return value of a call to that function?
# 

# Ans: If there is no return statement for a function, its return value is None.

# # Q.9. How do you make a function variable refer to the global variable?
# 

# Ans: A global statement will force a variable in a function to refer to the global variable. If you want to refer to a global variable in a function, you can use the global keyword to declare which variables are global.

# # Q.10. What is the data type of None?
# 

# Ans: The data type of None is NoneType.

# # Q.11. What does the sentence import areallyourpetsnamederic do?

# That import statement imports a module named areallyourpetsnamederic.

# # Q.12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
# 

# Ans: This function can be called with spam.bacon().

# # Q.13. What can you do to save a programme from crashing if it encounters an error?

# Ans: Place the line of code that might cause an error in a try clause and use except block to handle the error.

# # Q.14. What is the purpose of the try clause? What is the purpose of the except clause?

# ANS:The code that could potentially cause an error goes in the try clause. The code that executes if an error happens goes in the except clause.
