import math

def openLocks(x,y):
    list_lockers = ["open"]*lockers
    for k in range(2,students+1):
        for i,j in enumerate(list_lockers):
            if (i+1)>=(k-1):
                if (i+1)%k==0:
                    if list_lockers[i] == "open":
                        list_lockers[i] = "close"
                    else:
                        list_lockers[i] = "open"
    return list_lockers.count("open")


print("Assigning inputs")
x=input("Enter lockers value: ")
lockers=int(x)
y=input("Enter students value: ")
students=int(y)
print("Number of open lockers are: ",openLocks(x,y))

