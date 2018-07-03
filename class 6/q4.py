l=[1,'a',2,3,3.2,5,8.2]
li=[]
lf=[]
ls=[]

for x in l:
	if type(x)==int:
		li.append(x)
	elif type(x)==float:
		lf.append(x)
	elif type(x)==str:
		ls.append(x)
print(li)
print(lf)
print(ls)	