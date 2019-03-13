try:
	a=int(input("enter"))
	if a==5:
		print("you have choosen equal to 5")
	else:
	
		if a<5:
			raise NameError
		else:
			raise TypeError
	
except NameError:
	print("error!!!!,You have choosen less than 5")
except TypeError:
	print("You have choosen greater than 5")
	
else:
	print("no error")
finally:
	print("execution completed")