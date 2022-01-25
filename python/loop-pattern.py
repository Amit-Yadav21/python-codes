# Q...................................square pattern

#n=int(input("enter the no. "))
#for i in range(n):
#	print("*" * n)

#n=int(input("enter the no. "))
#for i in range(n):
#	print((str(n)+" ")*n)


#n=int(input("enter the no. "))
#for i in range(n):
#	print((str(i+1)+" ")*n)


#n=int(input("enter the no. "))
#for i in range(n):
#	print(" A "*n)


#n=int(input("enter the no. "))
#for i in range(n):
#	print((chr(65+i)+" ")*n)


# Q..................................Right angal triangal pattern

"""n=int(input("enter the no. "))
for i in range(n):
	print((chr(65+i)+" ")*(i+1))"""

"""n=int(input("enter the no. "))
for i in range(n):
	print("* "*(n-i))"""


# n=int(input("enter the no. "))         # 1 2 3 
# for i in range(n):                     # 1 2 3
# 	for j in range(n-1):               #  1 2 3
# 		print(j+1,end=" ")             # output
# 	print()


# num=int(input("Enter the number :"))
# for i in range(num):
# 	for j in range(1,num-i):
# 		print(" ",end="")
# 	for k in range(i+1):
# 		print(chr(65+i),end=" ")
# 	print()

#.....................................................
# num1=int(input("Enter number :"))
# num2=int(input("Enter number :"))
# product=0
# for i in range(1,num2+1):
# 	product=product+num1
# print("Multification of number",product)    # multiply of two digit, without using multilpy symble

# a=1
# product=" "
# while a<=2:
# 	user=input("Enter number :")
# 	a=a+1	
# 	product+=user
# print(product)

#......................................................

##### A to Z pattern ##############
# Q...............................A
# for row in range (5):
# 	for col in range (4):
# 		if row==0 and col in (1,2):
# 			print("*",end=" ")
# 		elif row in (1,3,4) and col in (0,3):
# 			print("*",end=" ")
# 		elif row==2:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()


# for row in range (5):
# 	for col in range (4):
# 		if row==0 and col in (1,2):
# 			print("*",end=" ")
# 		elif row in (1,3) and col in (0,3):
# 			print("*",end=" ")
# 		elif row==2 and col in (0,1,2):
# 			print("*",end=" ")
# 		else:
# 			print("",end=" ")
# 	print()



# for row in range (5):
# 	for col in range (4):
# 		if row in (0,2) and col in (0,1,2,3):
# 			print("*",end=" ")
# 		elif row in (1,3,4) and col in (0,3):                #  
# 			print("*",end=" ")
# 		elif row==2:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()


#.................................................

# Q.2.....................B

# for row in range(7):
# 	for col in range(5):
# 		if row in(0,3,6) and col in(1,2,3):
# 			print("*",end=" ")
# 		elif row in(0,1,2,3,4,5,6) and col==0:
# 			print("*",end=" ")
# 		elif row in(1,2,4,5) and col==4:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# .........................................................

# Q.3.................................C

# for row in range(7):
# 	for col in range(5):
# 		if row in(0,6) and col in(1,2,3):
# 			print("*",end=" ")
# 		elif row in(1,5)and col==4:
# 			print("*",end=" ")
# 		elif row in(1,2,3,4,5) and col==0:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# Q 4.............................D

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

# Q.5.......................E
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

# Q.6.............................F

# for row in range(7):
# 	for col in range(5):
# 		if row in(0,1,2,3,4,5,6) and col==0:
# 			print("*",end=" ")
# 		elif row==0 and col in (0,1,2,3,4):
# 			print("*",end=" ")
# 		elif row==3 and col in(0,1,2,3):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# Q.7........................G

# for row in range(7):
# 	for col in range(5):
# 		if (row in {0,6}) and (col in {1,2,3}):
# 			print("*",end=" ")
# 		elif (row in {1,4,5}) and (col in{0,4}):
# 			print("*",end=" ")
# 		elif (row==2) and (col==0):
# 			print("*",end=" ")
# 		elif (row==3) and (col!=1):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# .....................................................

# Q.8.................................H

# for row in range(7):
# 	for col in range(5):
# 		if row in (0,1,2,3,4,5,6) and col in(0,4):
# 			print("*",end=" ")
# 		elif row==2 and col in(1,3):
# 			print("*",end=" ")
# 		elif row==2 and col==2:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# .....................................................

# Q.9..................................I

# for row in range(7):
# 	for col in range(5):
# 		if row in(0,6) and col in(0,1,2,3,4):
# 			print("*",end=" ")
# 		elif row in(0,1,2,3,4,5,6) and col==2:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# ......................................................

# Q.10................................J

# for row in range(7):
# 	for col in range(5):
# 		if row==0 and col in(0,1,2,3,4):
# 			print("*",end=" ")
# 		elif row in(0,1,2,3,4,5,6) and col==2:
# 			print("*",end=" ")
# 		elif row==5 and col==0:
# 			print("*",end=" ")
# 		elif row==6 and col in(0,1):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# ......................................................


# Q.................................K

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

# Q.12...............................L

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

# Q.13...............................M

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

# Q 14..........................................N

# for row in range(7):
# 	for col in range(7):
# 		if row in(0,1,2,3,4,5,6) and col in(0,6):
# 			print("*",end=" ")
# 		elif row==1 and col==1:
# 			print("*",end=" ")
# 		elif row==2 and col==2:
# 			print("*",end=" ")
# 		elif row==3 and col==3:
# 			print("*",end=" ")
# 		elif row==4 and col==4:
# 			print("*",end=" ")
# 		elif row==5 and col==5:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# ..................................................

# Q 15........................................o

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

# Q 16..........................p

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

# Q.17...............................Q

# for row in range(8):
# 	for col in range(5):
# 		if row in(0,6) and col in(1,2,3):
# 			print("*",end=" ")
# 		elif row in(1,2,3,4,5) and col in(0,4):
# 			print("*",end=" ")
# 		elif row==8 and col==4:
# 			print("*",end=" ")
# 		elif row==5 and col in (2,3):
# 			print("*",end=" ")
# 		elif row==7 and col==4:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# Q 18.............................R

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

# Q.19..............................S

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

# Q.20................................T

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

# Q.21...........................U

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

# Q.22...............................V

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

# Q.22...................W

# for row in range(7):
# 	for col in range(7):
# 		if row in(0,1,2,3,4,5,6) and col in(0,6):
# 			print("*",end=" ")
# 		elif row==3 and col==3:
# 			print("*",end=" ")
# 		elif row==4 and col in(2,4):
# 			print("*",end=" ")
# 		elif row==5 and col in(1,5):
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()

# Q. 23................................X

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

# Q.24...................................Y

# for row in range(7):
# 	for col in range(5):
# 		if row==0 and col in(0,4):
# 			print("*",end=" ")
# 		elif row==1 and col in(1,3):
# 			print("*",end=" ")
# 		elif row in(2,3,4,5,6) and col==2:
# 			print("*",end=" ")
# 		else:
# 			print(" ",end=" ")
# 	print()												

# Q.25...............................z

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


a,b,c=16,17,16
if a and c:
	print(b)
if b==c:
	print(c)
else:
	print("amit")