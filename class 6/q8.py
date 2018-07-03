l=[]
flag=0
for x in range(9):
	l.append(int(input("enter a number")))
print(l)

s=int(input("enter a number you want to search:"))

for x in l:
	if x==s:
		l.remove(x)
		flag=1
print(l)
if flag==0:
	print("number not found")