def CreateList():
    count==0
    l=[]
    for i in range(5):
        s=input("Enter any string:");
        l.append(s)

def CountEven(l):
    for i in l:
        for j in i:
            if(i%2==0):
                count+=1

    return(count)

CreateList()
Lenght(l)
ans=CountEven(l)
print(ans)
print("Lenght of {} is {}".format(l,ans)
