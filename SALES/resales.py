"""
This is a buy-and-sellam program
author: Patrick Stephane
email: example@gmai.com
"""

def grocery(mylist):            
    """
    This function return the total price of all items on the grocery list.

    args:
        mylist (list): Grocery list
        price_list (list): will be use to record the different price
        price (float): individual price on the grocery list
    return:
        total (str): The sum of prices converted into a string
    """    
    price_list = []                            # CREATE AN EMPTY LIST
    for item in mylist:            
        price = mylist.get(item)               # GET THE PRICE FROM THE GROCERY CART
        price_list.append(price)               # APPEND THE PRICE TO THE empty list  
    try:
        total = str(sum(price_list))           # TOTAL OF THE PRICES CONVERTED INTO A STRING    
    except TypeError:
        return("please make sure to convert the value of total into a string")
    return(total)         

def purchase(item):
    """
    This function will create a file and write the total of prices calculated from the above function.

    args:
        item (str): the name of the file to be created.
        mytotal (str): the total previously calculated.
    return:
        item (str): the name of the file to be created.
    """
    with open(item, 'w') as mycart:
        try:
            mycart.write(mytotal)
        except TypeError:
            return("Only a string is accepted, nothing else")
    return(item)

try:
    order = {
        'tomato':30,
        'thyme': 4.50,
        'garlic': 7.50,
        'rice': 10,
        'onions': 4,
        'fish': 9.99
    }
except TypeError:
    print("Only numbers are allowed")

mytotal = grocery(order)
print(mytotal)
myreceipt = purchase("receipt.txt")
print(myreceipt)





