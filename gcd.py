A=int(input("Enter A value::"))
print(A)
B=int(input("Enter B value::"))
print(B)
def GCD(A,B):
 if(B==0):
  return A 
 else: 
  return GCD(B,A%B)
print("The GCD of given two numbers is:")
print(GCD(A,B)) 
