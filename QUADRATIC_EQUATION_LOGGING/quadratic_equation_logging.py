"""
This is a division program
author: Patrick Stephane
email: example@gmai.com
"""

import math
import logging
# CREATE AND CONFIGURE A LOGGER
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
# CALLING THE basicConfig meth and pass in the args that I need.
logging.basicConfig(filename = "quadratic_equation_logs.log", level = logging.DEBUG, format = LOG_FORMAT)
# CALLING THE getLogger meth TO CREATE A LOGGER OBJECT.
logger = logging.getLogger()

def quadratic_formula(a, b, c):
    """
    Return the solution of the equation ax^2 + bx + c = 0.
    args:
        a (float): the user will provide this number
        b (float): the user will provide this number
        c (float): the user will provide this number
    return:
        root1(float): first solution to the quadratic equation
        root2(float): second solution to the quadratic equation
    """
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))  # The is a dynamic way to have the args of the function take their respectives values
    
    # Compute the discriminant. 
    # A good place for a debug message is where there is a comment for a block of code.
    # logger.debug("# Compute the discriminant.")
    disc = b**2 - 4*a*c
    
    # Compute the 2 roots
    # logger.debug("# Compute the 2 roots")
    try:
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
    except ZeroDivisionError:
        return("Sorry! I cannot divide a number by zero; the value of a should be different from 0")
    except ValueError:
        return("Unless we are working with complex numbers, This equation has not solution")
    
    # Return the roots
    # logger.debug("# Return the roots")
    return (root1, root2)

if __name__ == '__main__':
    equation = quadratic_formula(1, 0, -4)
    print(equation)