l=[]
def CreateList():
    #l=[]

    for i in range(5):
        s=input("Enter any string:");
        l.append(s)

def CountEven(l):
    for i in l:
            if(i%2==0):
                count+=1

    return(count)

CreateList()
print(l)






