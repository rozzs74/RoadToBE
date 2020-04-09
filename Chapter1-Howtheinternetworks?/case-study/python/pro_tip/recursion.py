"""
What is a recursion? In my experience recursion is a technique that
ables you to solve the reapting problem.

When to use recusion, let say on an API your required to poll or 
self calling invocation so recursion is the solution.
Recursion should stop.
"""


# Author: John Royce Punay
# Date created: March 3, 2020 5:34 PM

def foo(n):
    if n != 0:
        print(f"I am recursion you can't stop me {n}")
        foo(n-1)


foo(5)