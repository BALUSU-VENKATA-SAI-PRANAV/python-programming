n=int(input("enter number: "))
num=n
sum=0
rem=0
while(n>0):
	rem=n%10
	sum=sum+(rem**3)
	n=n//10
if(num==sum):
	print("it is armstrong")
else:
	print("it is not armstrong")
