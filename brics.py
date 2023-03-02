country=["Brazil","India","China","Russia","Srilanka"]
c=input("enter the country name")
def fun(c):
    if c in country:
        print("{} is belongs to brics".format(c))
    else:
        print("{} is not belongs to brics".format(c))
fun(c)
