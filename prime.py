n=int(input("enter the number"))
sum=0
temp=n
while(temp!=0):
    rem=temp%10
    sum=sum+rem**3
    temp=temp//10
if(sum==n):
    print("Armstrong number")
else:
    print("not a Armstrong")
    

