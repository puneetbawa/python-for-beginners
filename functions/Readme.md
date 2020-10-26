In Python, a function is a group of related statements that performs a specific task.

Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.

Furthermore, it avoids repetition and makes the code reusable.


Syntax of Function

'''
def function_name(parameters):
        """docstring"""
        statement(s)
'''

Above shown is a function definition that consists of the following components.

1) Keyword def that marks the start of the function header.
2) A function name to uniquely identify the function. Function naming follows the same rules of writing identifiers in Python.
3) Parameters (arguments) through which we pass values to a function. They are optional.
4) A colon (:) to mark the end of the function header.
5) Optional documentation string (docstring) to describe what the function does.
6) One or more valid python statements that make up the function body. Statements must have the same indentation level (usually 4 spaces).
7) An optional return statement to return a value from the function.

-----------------Scope and Lifetime of variables----------------------------

1) Scope of a variable is the portion of a program where the variable is recognized. Parameters and variables defined inside a function are not visible from outside the function. Hence, they have a local scope.

2) The lifetime of a variable is the period throughout which the variable exits in the memory. The lifetime of variables inside a function is as long as the function executes.

3) They are destroyed once we return from the function. Hence, a function does not remember the value of a variable from its previous calls.
