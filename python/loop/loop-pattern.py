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


for row in range (5):
	for col in range (4):
		if row==0 and col in (1,2):
			print("*",end=" ")
		elif row in (1,3) and col in (0,3):
			print("*",end=" ")
		elif row==2 and col in (0,1,2):
			print("*",end=" ")
		else:
			print("",end=" ")
	print()



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