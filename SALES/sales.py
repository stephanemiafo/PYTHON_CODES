
def grocery(mylist):   
    price_list = []                            # CREATE AN EMPTY LIST
    for item in mylist:            
        price = mylist.get(item)               # GET THE PRICE FROM THE GROCERY CART
        price_list.append(price)               # APPEND THE PRICE TO THE LIST
    total = str(sum(price_list))               # TOTAL OF THE PRICES CONVERTED INTO A STRING    
    return(total)         


# THIS FUNCTION WILL CREATE A FILE AND WRITE THE TOTAL PRICE OF ALL ITEMS 
def purchase(item):
    with open(item, 'w') as mycart:
        mycart.write(mytotal)

myreceipt = 'receipt.txt'
order = {
    'tomato':30,
    'thyme': 4.50,
    'garlic': 7.50,
    'rice': 10,
    'onions': 4,
    'fish': 9.99
}
mytotal = grocery(order)
print(mytotal)
receipt = purchase(myreceipt)
print(receipt)

