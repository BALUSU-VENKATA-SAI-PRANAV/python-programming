n=int(input("enter number: "))
sum=0
rem=0
while (n>0):
	rem=n%10
	sum+=rem
	n=n//10
print("sum is: ",sum)
