#was to enter any number and number is prime or not
a=int(input("Enter any number:"))
n=a
c=0
i=0
for i in range(n):
    if(i%2==0):
        c=1
        break
if(c==1):
    print("The 
