n=int(input("enter the number: "))
num=n
rev=0
while (n>0):
	rem=n%10
	rev=rev*10+rem
	n=n//10
if(rev==num):
	print("it is a palindrome")
else:
	print("it is not a palindrome")
