# ARN 
# arn = "arn:aws:iam::123456789012:user/Development/product_1234/*"
# # EXTRACTING THE ACCOUNT ID FROM THE ARN
# print(f"the aws account id is: {arn[13:25]}")


        # OR 
# arn = "arn:aws:iam::123456789012:user/Development/product_1234/*"
# #FIND THE INDEX OF 123456789012
# accountid = arn.index("123456789012") # OR   accountid = arn.find("123456789012")  # THE ANSWER IS 13
# #FIND THE LENGHT OF 123456789012
# len("123456789012")  # ANSWER IS 12
# # SO THE FIRST INDEX OF 123456789012 is 13 and the last one is 25 (13+12)
# # EXTRACTING THE ACCOUNT ID FROM THE ARN
# print(f"the aws account id is: {arn[13:25]}")
