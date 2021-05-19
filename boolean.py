## Hiking weather app for a wooden hiking trail ##
def cold_or_hot(a):
    x = int(a)
    if x > 67:
        return("Great day! for a hike! ")
    else:
         return("It might get Chilly in the woods.")

x = input("Enter todays temperature: ")
print(cold_or_hot(x))
