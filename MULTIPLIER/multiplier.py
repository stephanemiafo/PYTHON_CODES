"""
This is a multiplication program
author: Patrick Stephane
email: multiplication@gmai.com
"""

def list_even_numbers(list):
    """
    This function return a list of even numbers

    args:
        list (list): it is a given list of random numbers
        even_numbers (list): An empty list
        x (looping var): temporary variable that takes the different variable in the loop
    return:
        even_numbers (list): A list of even numbers
    """
    even_numbers = []
    for x in list:  
        if x % 2 == 0:
            even_numbers.append(x)    
    return(even_numbers)

def multiply_even_numbers(even_list):
    """
    This function return the product of items in a list

    args:
        prod (literal) set to 1 because it's neutral in multiplication
        even_list (list): the list of even numbers
    
    return:
        prod (int): product of the items in the list
    """
    try:
        prod = 1
    except NameError:           # IF prod  IS A str
        print("please enter a number") 
    
    for y in even_list:
        try:
            prod = prod * y
        except UnboundLocalError:           # IF prod  IS A str
            print("do not reference variable before assigning it")
            break
    try:
        return(prod)
    except UnboundLocalError:                         # IF prod  IS A str
            print("the product will be None since since prod is not a number")

Numbers = [8,9,11,20,32,101,100]
my_even_list = list_even_numbers(Numbers)
print(my_even_list)
product = multiply_even_numbers(my_even_list)
print(f"the product of all even numbers in the list is: {product}")