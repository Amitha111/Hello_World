def flower_list(name_flower, flower_list):
    if name_flower in flower_list:
        return "Yes"
        return "no"

    
fl1 = ["roses", "lilles", "Tulips", "lavender"]
fl2 = (input)("What's your flower choice? ")

if fl2 in fl1:
    print("you are at luck!")

if fl2 not in fl1:
    print(flower_list(fl2, fl1))
    print("sorry we dont!")

    
