
def WSJF_S(a, b, c, d):
    bv = int(a)                                                     ## bv = Business Value of the User Story
    tc = int(b)                                                  ## tc = Time Criticality
    rr = int(c)                                                    ## rr/oe = Risk Reduction/ Oportunity enablement
    js = int(d)                                                   ## js = Job Size                                                               
    cod = (bv + tc + rr)                                                   ## cod = Cost of Delay
    print(cod)
    print ("This is your Cost of Dealay")
    y = (cod//int(js) )
    print(y)
    return "This is WSJF for our current user story! "

a = input("What's the Business Value on this user story? ")
b = input("What is te Time Criticality Value? ")
c = input("What is the Risk Reduction Value? ")
d = input("What is the Job Size here? ")
print(a)
print(b)
e = WSJF_S(a, b, c, d)
print (e)