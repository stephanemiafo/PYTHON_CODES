
# Users' credentials in our DB
database= {
    "romeo": "Malanga12#",
    "matheo": "Gerdin45$"
}
tries = 0                                                                 # initializing the number of tryal to get the UN and PWD right.
while tries <= 5:                                                         # iterating through the number of tryal
    tries += 1                                                            # incrementing tries to avoid infinite loop
    UserName = input("please enter your username here: ").lower()         # Gathering users' credentials
    PassWord = input("please enter your password here: ")                 # Gathering users' credentials
    if UserName in database and database.get(UserName) == PassWord:       # Comparing the user credentials received to those in the DB
        print("access granted")                                           # Cred valid
        break
    else:
        if tries <= 5:
            print("please try again")                                     # cred invalid
        else:
            print("ACCOUNT LOCKED, try again in 24 hours")                # Locking account after a set number of trial

 