def magic(N):
    if N<9:
        return(-1)
    else:
        if N&1==0:
            while N>9:
                last_dig=N%10
                last_but_one=(N//10)%10
                if last_dig<last_but_one:
                    return("No")
                N=N//10
        else:
            while N>9:
                last_dig=N%10
                last_but_one=(N//10)%10
                if last_dig>last_but_one:
                    return("No")
                N=N//10

N=int(input("enter the number"))
magic(1234)