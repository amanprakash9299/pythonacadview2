print("1unit=100")
unit=int(input("enter number of unit you want to buy:"))
price=unit*100

if price>1000:
	price=price-price/10
	print("total cost of purchasing:",price)
else:
	print("total cost of purchasing:",price)