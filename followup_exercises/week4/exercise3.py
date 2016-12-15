#!/usr/bin/env python
"""
Exercise3

Ex3a:
--------
Create a function that prints "hello world". Call this function from your main program.


Ex3b:
--------
Create a function that accepts two arguments (x, y) and that prints out "hello world func2". The
function should also print out the values of x and y.

Call this function from your main program.


Ex3c:
--------
Create a function that accepts three arguments (x, y, z) where z has a default value of 10. The
function should print out "hello world func3". It should also print out the values of x, y, z
including labels indicating which variable you are printing out.

Call function3 with two positional arguments.
Call function3 with three positional arguments.
Call function3 with three named arguments.
Call function3 with one positional argument and two named arguments
Call function3 as follows func3(7, 9, y=8). Observe that this generates an exception; gracefully
handle the exception.


Ex3d:
--------
Call function3 using *args in other words:
func3(*my_list)

where my_list is a three element list


Ex3e:
--------
Call function3 using **kwargs in other words:
func3(**my_dict)

Where my_dict is a dictionary that contains three key-value pairs corresponding to x, y, and z.


Ex3f:
-------
Write a function4 that takes three arguments (x, y, z) and returns x + y + z

Call function4 using three integers; print the value returned from the function
Call function4 using three strings; print the value returned from the function


Ex3g:
--------
Write a function5 that takes a function (my_func) as an argument. Function5 should call my_func()
three times and return None.

"""

def func1():
    print "hello world"

def func2(x, y):
    print "hello world func2, argx: {}, argy: {}".format(x, y)

def func3(x, y, z=10):
    print "hello world func3"
    print "argx: {}, argy: {} argz: {}".format(x, y, z)

def func4(x, y, z):
    return x + y + z

def func5(my_func):
    """Call my_func three times."""
    my_func()
    my_func()
    my_func()

def print_wrapper(header=""):
    if header:
        print "\n"
        print header
        print '-' * 80
    else:
        print '-' * 80

def main():

    ##### Exercise 3A #####
    print_wrapper(header="Exercise 3A")
    func1()
    print_wrapper()

    ##### Exercise 3B #####
    print_wrapper(header="Exercise 3B")
    func2(22, 17)
    print_wrapper()

    ##### Exercise 3C #####
    print_wrapper(header="Exercise 3C")
    func3(22, 17)
    print
    func3(22, 17, 1)
    print
    func3(x=7, y=7, z=3)
    print
    func3(7, z=22, y=9)
    print
    try:
        func3(7, 9, y=8)        # generates exception
    except TypeError:
        print "Handled exception"
    print_wrapper()

    ##### Exercise 3D #####
    print_wrapper(header="Exercise 3D")
    my_args = [3, 4, 5]
    func3(*my_args)
    print_wrapper()

    ##### Exercise 3E #####
    print_wrapper(header="Exercise 3E")
    my_kwargs = {'x': 1, 'y': 2, 'z': 3}
    func3(**my_kwargs)
    print_wrapper()

    ##### Exercise 3F #####
    print_wrapper(header="Exercise 3F")
    return_val = func4(17, 8, 3)
    print return_val
    print
    my_val = func4('hello ', 'world ', 'whatever')
    print my_val
    print_wrapper()

    ##### Exercise 3G #####
    print_wrapper(header="Exercise 3G")
    func5(func1)
    print_wrapper()


if __name__ == "__main__":
    main()
