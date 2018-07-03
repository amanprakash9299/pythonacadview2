num=int(input("enter a number between 1 to 200:"))
if num>1 and num<51:
	print("Sorry! No prize this time.")
elif num>50 and num<151:
	print("Congratulations! You won a [wooden dog]!")
elif num>150 and num<181:
	print("Congratulations! You won a [books]!")
elif num>180 and num<201:
	print("Congratulations! You won a [chocolates]!")
else:
	print("please enter a number between 1 to 200")