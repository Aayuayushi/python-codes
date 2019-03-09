def max(a,b,c):
	if a>b and a>c:
		print ("maximum is :",a)
	elif b>a and b>c:
		print ("maximum is :",b)
	else:
		print("maximum is :",c) 

numbers=max(4,8,2)

from modules import multipy
y=multipy(5,6)
print(y)

def even():
if (num % 2) == 0:
   print("{0} is Even")
else:
   print("{0} is Odd")
   num = int(input("Enter a number: "))