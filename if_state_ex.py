## code for qualifying customers downpayment based on credit score. if credit score is more than 800 \
## they qualify for 10% downpayment 

import math


def downpayment(a):

    x = int(a)
    if  x > 700:
        print("You Qualify for 10 percent downpayment! ")                                      
        return (10)

    else:
        print("Your downpayment is 20 perecnt on loan amount")
        return (20)
        
## calculating downpayment for both credit scores

cs = input("Enter customer's credit score here: ")       ## cs = customers credit score
dp = downpayment(cs)
z = int(dp)


loan_amount = input("Enter requested loan amount: ")
x = int(loan_amount)
amt_dwn = ((x * z)/100 )
print(amt_dwn)