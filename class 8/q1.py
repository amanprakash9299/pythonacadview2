#As we know, We can represent time in a way that�s easy for us to understand. However, Python stores it in tuples. 
These python tuples are made of nine numbers.

Index	Field			Domain of Values
0		Year 			(4 digits)	Ex.- 1995
1		Month			1 to 12
2		Day				1 to 31
3		Hour			0 to 23
4		Minute			0 to 59
5		Second			0 to 61 (60/61 are leap seconds)
6		Day of Week		0 to 6 (Monday to Sunday)
7		Day of Year		1 to 366 (Julian day)
8		DST				-1,0,1

Leap seconds are added to make up to Earth�s slowing rotation. When DST is 0, it isn�t applied. 
When it�s 1, it is applied. However, when it is -1, it is up to the library to determine that.

This tuple has an equivalent struct_time structure.