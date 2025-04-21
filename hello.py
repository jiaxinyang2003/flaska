def square(z):
	print("{}的平方是{}".format(z,z*z))


x=int(input("請輸入一個數字"))
print("您輸入的是",x)

if(x<=0):
	print("您輸入的值小於等於0")
elif(x==0):
	print("您輸入的值等於0")
else:	
    for i in range(1,x+1):
	    square(i)