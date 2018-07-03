def perfect(num):
	sum=0
	for x in range(1,num):
		if num%x==0:
			sum=sum+x
	if sum==num:
		print(num,":is a perfect number")
for x in range(1,1001):
	perfect(x)