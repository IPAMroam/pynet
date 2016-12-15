#!/usr/bin/env python
"""
Exercise2 - Python List Review


Ex2a:
--------
Create a random list (my_list) that contains seven elements.

Loop over the list printing out all of the elements.


Ex2b:
--------
Add an 8th element to the list.

Loop over the list printing out both the list index and the element value.


Ex2c:
--------
Change the third element of the list to a different value.

Change the last element of the list to a different value.

Print your list


Ex2d:
--------
Remove the last element from your list.

Remove the first element from your list.

Remove the current third element from your list.

Print your list and also print how long it is.


Ex2e:
--------
Create another list that is three elements in length.

Add the elements of the new_list to my_list such that my_list is now eight elements long.


Ex2f:
--------
Insert a new element between the current 1st and 2nd elements.


Ex2g:
--------
Print only the first four elements of the list.

Create a new list that is the last five elements of your current list. Print out this new list.

"""

if __name__ == "__main__":

    #### Exercise 2a #####
    print "\nExercise 2a"
    print "-" * 80
    my_list = ['whatever', 99, True, 'hello', 22, 'some string', 'another']

    for entry in my_list:
        print entry
    print "-" * 80

    #### Exercise 2b #####
    print "\nExercise 2b"
    print "-" * 80
    my_list.append('whatever')

    for i, entry in enumerate(my_list):
        print i, entry
    print "-" * 80

    #### Exercise 2c #####
    print "\nExercise 2c"
    print "-" * 80
    my_list[2] = False
    my_list[-1] = 'changed'
    print my_list
    print "-" * 80

    #### Exercise 2d #####
    print "\nExercise 2d"
    print "-" * 80
    my_list.pop()
    my_list.pop(0)
    my_list.pop(2)
    print "List length: {}".format(len(my_list))
    print my_list
    print "-" * 80

    #### Exercise 2e #####
    print "\nExercise 2e"
    print "-" * 80
    new_list = [3, 2, 9]
    my_list.extend(new_list)
    print my_list
    print "-" * 80

    #### Exercise 2f #####
    print "\nExercise 2f"
    print "-" * 80
    my_list.insert(1, 'whatever')
    print my_list
    print "-" * 80

    #### Exercise 2g #####
    print "\nExercise 2g"
    print "-" * 80
    print my_list[:4]

    new_list = my_list[-5:]
    print new_list
    print "-" * 80
    print
