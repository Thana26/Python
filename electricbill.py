age=int(input("enter the age of person : "))
rate=int(input("enter the slab rate : "))
if   ((rate>=  0) and (rate<= 50)) :
   cost=1.45
elif ((rate>= 51) and (rate<=100)) :
   cost=2.7
elif ((rate>=101) and (rate<=200)) :
   cost=4.5
elif ((rate>=201) and (rate<=500)) :
   cost=7.4
else  :
   cost=9.8
print("the slab cost per one unit = ",cost)
power=rate*cost
if(age>60) :
   power=power*0.76
else :
   power=power
print("the power cost",power)
