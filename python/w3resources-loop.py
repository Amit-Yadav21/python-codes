# Q..1

# for i in range(1500,2700):
# 	if (i%7==0 and i%5==0):
# 		print(i)


# i=1500
# while i<=2700:
# 	if i%5==0 and i%7==0:
# 		print(i)
# 	i=i+1
# ----------------------------------------------

# Q........3

# a=5
# i=0
# n=int(input("Enter number between 1 to 9:"))

# while n>0:
# 	if n==a:
# 		print("geuss")
# 	else:
# 		print("not geuss")
# 	break

# b=5
# i=1
# while i<=5:
# 	num=int(input("Enter number between 1 to 10 :"))
# 	i=i+1
# 	if num<b:
# 		print("aapka number chota hai")
# 	elif num>b:
# 		print("aapka number bada hai")
# 	else:
# 		print("aapne sahi geuss kiya")
# 		break


# a=7
# n=int(input("Enter number between 1 to 10 :"))
# for i in range (n>0):
# 	if n==a:
# 		print("geuss number")
# 	else:
# 		print("not geuss")


# Q....4

# n=int(input("Enter number of rows:"))
# for i in range(n):
# 	for j in range(i+1):
# 		print("*",end=" ")
# 	print()
# for i in range(n,0,-1):
# 	for j in range(i-1):
# 		print("*",end=" ")
# 	print()

# n=int(input("Enter number of rows:"))
# i=1
# while i<=n:
# 	j=1

# 	while j<=i:
# 		print("*",end=" ")
# 		j=j+1
# 	print()
# 	i=i+1


# Q.........................5

# a=input("Enter name -")
# b=a[ :: -1]
# for i in  b:
# 	print("revers srtinge-",b)
# 	break


# Q.................................6

# ........find odd and even.
# number=(1,2,3,4,5,6,7,8,9)
# odd=0
# even=0
# for i in number:
# 	if i%2==0:
# 		even=even+1
# 	else:
# 		odd=odd+1
# print("even number",even)
# print("odd number",odd)

# .....find sum of odd and even.
# number=(1,2,3,4,5,6,7,8,9)
# odd=0
# even=0
# for i in number:
# 	if i%2==0:
# 		even=even+i
# 	else:
# 		odd=odd+i
# print("even number",even)
# print("odd number",odd)


# number=int(input("Enter number:"))
# odd=0
# even=0
# for i in range(1,number+1):
# 	if i%2==0:
# 		even=even+1
# 	else:
# 		odd=odd+1
# print("even number",even)
# print("odd number",odd)


# n=int(input("Enter number:"))
# odd=0
# even=0
# i=1
# while i<=n:
# 	if i%2==0:
# 		even=even+1
# 	else:
# 		odd=odd+1
# 	i=i+1
# print("even number-",even)
# print("odd number-",odd)


# number=int(input("Enter number:"))
# odd=0
# even=0
# for i in range(1,number+1):
# 	if i%2==0:
# 		print("even",i)
# 	else:
# 		print("odd",i)


# Q.......................8

# for i in range(6):
# 	if (i==3 or i==6):
# 		continue
# 	print(i,end=" ")
# print()


# Q........................9

# n=int(input("Enter number-"))
# x=0
# y=1
# z=0
# while z<=n:
# 	print(z)
# 	x=y
# 	y=z
# 	z=x+y

# Q.............................10

# i=0
# num=int(input("Enter number-"))
# while i<=num:
# 	i=i+1
# 	if i%3==0 and i%5==0:
# 		print("fizzbuzz")
# 	elif i%3==0:
# 		print("fizz")
# 	elif i%5==0:
# 		print("buzz")
# 	else:
# 		print(i)

# Q...............................14

# s=input("Enter a string-")
# d=0
# l=0
# for c in s:
# 	if c.digit():
# 		d=d+1
# 	elif c.alpha():
# 		l=l+1
# 	else:
# 		pass
# print("letter-",l)
# print("digit-",d)


# Q 18.............................D

# for row in range(7):
#  	for col in range(5):
#  		if row in {0,6} and col in {0,1,2,3}:
#  			print("*",end=" ")
#  		elif row in {1,2,3,4,5} and col in {0,4}:
#  			print("*",end=" ")
#  		else:
#  			print(" ",end=" ")
#  	print()

# .......................................................

# Q 19.......................E
# for row in range(7):
# 	for col in range(5):
# 		if row in {0,3,6} and col in {0,1,2,3,4}:
# 			print("*",end=" ")
# 		elif row in {1,2,4,5} and col in {0}:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# ....................................................

# Q 20........................G

# for row in range(7):
# 	for col in range(5):
# 		if row in(0,6) and col in(1,2,3):
# 			print("*",end=" ")
# 		elif row in(1,5)and col==4:
# 			print("*",end=" ")
# 		elif row in(1,2,3,4,5) and col==0:
# 			print("*",end=" ")
# 		elif row in(3,4) and col==4:
# 			print("*",end=" ")
# 		elif row==3 and col in(2,3,4):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# .....................................................

# Q 21...............................L

# for row in range(7):
# 	for col in range(5):
# 		if row in(0,1,2,3,4,5,6) and col==0:
# 			print("*",end=" ")
# 		elif row==6 and col in (0,1,2,3,4):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print() 

# ....................................................

# Q 22...............................M

# for row in range(7):
# 	for col in range(5):
# 		if row in (0,1,2,3,4,5,6) and col in(0,4):
# 			print("*",end=" ")
# 		elif row==2 and col in(1,3):
# 			print("*",end=" ")
# 		elif row==3 and col==2:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# ......................................................

# Q 23........................................o

# for row in range(7):
# 	for col in range(5):
# 		if row in(0,6) and col in (1,2,3):
# 			print("*",end=" ") 
# 		elif row in(1,2,3,4,5) and col in (0,4):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# ....................................................

# Q 24..........................p

# for row in range(7):
# 	for col in range(5):
# 		if row in(0,3) and col in (0,1,2,3):
# 			print("*",end=" ")
# 		elif row in(1,2) and col==4:
# 			print("*",end=" ")
# 		elif row in(0,1,2,3,4,5,6) and col==0:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# .......................................................

# Q 25.............................R

# for row in range(7):
# 	for col in range(5):
# 		if row in (0,3) and col in(0,1,2,3):
# 			print("*",end=" ")
# 		elif row in(1,2,6) and col==4:
# 			print("*",end=" ")
# 		elif row==4 and col==2:
# 			print("*",end=" ")
# 		elif row==5 and col==3:
# 			print("*",end=" ")
# 		elif row in(0,1,2,3,4,5,6) and col==0:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# .............................................................

# Q 26..............................S

# for row in range(7):
# 	for col in range(5):
# 		if row==0 and col in(1,2,3,4):
# 			print("*",end=" ")
# 		elif row in(1,2) and col==0:
# 			print("*",end=" ")
# 		elif row==3 and col in(1,2,3):
# 			print("*",end=" ")
# 		elif row in(4,5) and col==4:
# 			print("*",end=" ")
# 		elif row==6 and col in(0,1,2,3):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# .............................................................

# Q 27................................T

# for row in range(7):
# 	for col in range(5):
# 		if row==0:
# 			print("*",end=" ")
# 		elif row in(1,2,3,4,5,6) and col==2:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# .............................................................

# Q.28...........................U

# for row in range(7):
# 	for col in range(5):
# 		if row in(0,1,2,3,4,5) and col in(0,4):
# 			print("*",end=" ")
# 		elif row==6 and col in(1,2,3):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# ...................................................................

# Q. 29................................X

# for row in range(7):
# 	for col in range(5):
# 		if row in(0,1,5,6) and col in(0,4):
# 			print("*",end=" ")
# 		elif row in(2,4) and col in(1,3):
# 			print("*",end=" ")
# 		elif row==3 and col==2:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# ....................................................................

# Q. 30...............................z

# for row in range(7):
# 	for col in range(7):
# 		if row in(0,6) and col in(0,1,2,3,4,5,6):
# 			print("*",end=" ")
# 		elif row==1 and col==5:
# 			print("*",end=" ")
# 		elif row==2 and col==4:
# 			print("*",end=" ")
# 		elif row==3 and col==3:
# 			print("*",end=" ")
# 		elif row==4 and col==2:
# 			print("*",end=" ")
# 		elif row==5 and col==1:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# ..............................................................

# Q.............33

# a=input("Enter month name and find day in the month:")
# for i in(a):
# 	if a=="Febuary":
# 		print("no of days: 28/29")
# 	elif a in ("April","June"," September","November"):
# 		print("no of days : 30")
# 	elif a in ("jaunary","March","May","July","August","October","December"):
# 		print("no of days: 31")
# 	else:
# 		print("Wrong name")
# 	break

# ....................................................................

# Q..............32

# a=input("Enter alphabet name check vowel & consonent:")
# for i in (a): 
# 	if a in ("a","e","i","o","u"):
# 		print("vowel name is =",a)
# 	elif a in ("b","d","c","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"):
# 		print("consonent name is =",a)
# 	else:
# 		print("no alphabet name") 

# ......................................................................

# Q.....................43

# n=int(input("Enter number-"))
# for i in range(1,11):
# 	print(n,'x',i,'=',n*i)

# ..........................................................................
# Q............44
# a=int(input("Enter number"))
# for i in range(a):
#     print(str(i) * i)


# a = int(input("Input first number: "))
# b = int(input("Input second number: "))
# c = int(input("Input third number: "))
# if a > b:
#     if a < c:
#         maximum = a
#     elif b > c:
#         maximum = b
#     else:
#         maximum= c
# else:
#     if a > c:
#         maximum= a
#     elif b < c:
#         maximum= b
#     else:
#         maximum= c

# print("The  2nd maximum is", maximum)


# for row in range(7):
# 	for col in range(4):
# 		if row in (0,1,2,3,4,5,6) and col==0:
# 			print("*",end=" ")
# 		elif row in (0,6) and col==3:
# 			print("*",end=" ")
# 		elif row in (1,5) and col==2:
# 			print("*",end=" ")
# 		elif row in(2,4) and col==1:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()


# for row in range(5):
# 	for col in range(9):
# 		if row==0 and col in(0,8):
# 			print("*",end=" ")
# 		elif row==1 and col in(1,7):
# 			print("*",end=" ")
# 		elif row==2 and col in(2,6):
# 			print("*",end=" ")
# 		elif row==3 and col in(3,5):
# 			print("*",end=" ")
# 		elif row==4 and col==4:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()


# a=input("Enter name or number-")
# for i in(a):
# 	print(len(a))
# 	break


# a=input("Enter name:")
# l=0
# for i in (a):
# 	if i.isalpha():
# 		l=l+1
# print("latter",l)


# a=input("Enter number:")
# d=0
# for i in (a):
# 	if i.isdigit():
# 		d=d+1
# print("Digit",d)

# ---------------------------------------------------

# a=input("Enter srtinge-")
# b=len(a)
# c=len(a)//2
# d=a[:c]
# e=a[c:]
# print(d)
# print(e)


# for i in range(1,5):
# 	print("*"*i)

# i=input()
# a=i.replace("",",")
# print(a.strip(","))



# a=input("enter your name :")
# b=""
# for i in a[::-1]:
# 	b+=i
# print(b)

# ..................................................................

# print("geuss number-1,2,3,4,5,6,7,8,9,0")
# a=input("Enter your name : ")
# b=int(input("Enter number-"))
# geuss=1
# if geuss==b:
# 	print("congartulation! you win-",a)
# else:
# 	print("sorry! you wrong geuss-",a)


# q..............3 times run.

# print("Geuss number-0,1,2,3,4,5,6,7,8,9")
# a=input("Enter your name-")
# b=int(input("Enter number-"))
# geuss=3
# if geuss==b:
# 	print("congratulation! " ,a ,"you win.")
# else:
# 	print("sorry",a, "you wrong geuss.")
# c=int(input("Enter number-"))
# if c==geuss:
# 	print("congratulation! " ,a ,"you win.")
# ....................................................................

# Q.................................Add two number

# a=input("Enter number")
# b=input("Enter number")
# result=a+b
# print("sum of two number",result)

# .........................................................

# Q.....max of tow number

# a=int(input("Enter number- "))
# b=int(input("Enter number- "))
# if a>b:
# 	print(a,"is amax number")
# elif b>a:
# 	print(b,"is max number")


# .................................

# Q................find factorial number

# a=int(input("Enter number-"))
# fac=1
# i=0
# while i<=a:
# 	fac*=1
# 	i=i+1
# print("factorial of",a)      # Not complited

# fac=1
# a=int(input("Enter number-"))
# for i in range(1,a+1):
# 	fac=fac*i
# print(fac)

# ............................................

# # Q..................simple interst

# amount=int(input("Enter amt-"))
# rate=int(input("Enter rate of persentage-"))
# time=int(input("time in year-"))
# print((amount*rate*time)/100)



# a="navgukul"
# n=len(a)
# for i in range(n):
# 	print(a[i],"=",i)

# ......................................................

# for name in range(5):
#     # 3 column
#     for j in range(5):
#         print('*', end='')
#     print()

# ............................................

# find remainder without using mosulus?

# a=int(input("Enter 1st number-"))
# b=int(input("Enter 2nd number-"))
# q=int(a/b)
# r=a-(b*q)
# print("remainder is=",r)

# a=int(input("Enter 1st number-"))
# b=int(input("Enter 2nd number-"))
# r=a-b*(a//b)
# print("remainder=",r)
# ..........................................

# find product without using multiply symble?

# a=int(input("Enter number:"))
# b=int(input("Enter 2nd number:"))
# pro=0
# for i in range(1,b+1):
# 	pro=pro+a
# print("multiply is=",pro)
# ...........................................
# find last number divisible by 2 and not.

# num=int(input("Enter number-"))
# b=num%1000
# c=b//100
# if c%2==0:
# 	print("number divisible by 2")
# else:
# 	print("number not divisible by 2")
# ..........................................

# even=0
# odd=0
# n=int(input("Enetr number-"))
# for i in range(1,n+1):
# 	if i%2==0:
# 		even+=f"{i}\n"
# 	elif i%2!=0:
# 		odd+=f"{i}\n"
# print(even)
# print()
# print(odd)
#............................................
