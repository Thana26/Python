import random
G=["Rock","Paper","Scissors"]
print("Rock,Paper,Scissors....")
while(1>0):
    S=random.choice(G)
    C=input("enter your choice:")
    print("your choice:",C)
    print("My choice:",S)
    if(S=="Rock" and C=="Paper"):
        print("Paper beats Rock.....won ",end='\n')
        continue
    elif(S=="Paper" and C=="Rock"):
        print("Paper beats Rock...lose",end='\n')
        continue
    elif(S=="Scissors" and C=="Paper"):
        print("Scissor beats paper...you lost")
        continue
    elif(S=="Paper" and C=="Scissors"):
        print("Scissor beats paper...You won")
        continue
    elif(S=="Rock" and C=="Scissors"):
        print("Rock beats scissors...You lost!")
        continue
    elif(S=="Scissors" and C=="Rock"):
        print("Rock beats Scissors...You won")
    elif(S==C):
        print("Tie!")
    else:
        print("Please check your entry")
