

# Q...........0
# i=1
# while (i<=100):
# 	print(i)
# 	i=i+1

# for i in range(1,101):
# 	print(i)

# Q........number print(1,100)
# index = 1;  
# while 1:  
#     print(index," ",end = ""),  
#     index=index+1;  
#     if index == 101:  
#         break;  
# print( )

# ...1.to..100...number print.......
# for i in range(1,11):
# 	while (i<=100):
# 		print(i," ",end=" ")
# 		i+=10
# 	print()


# Q................1
# x=7
# while (x<=100):
# 		print(x)
# 		x=x+7


# Q..................2
# n=int(input("Enter your sum number  :"))
# i=0
# sum=0
# while (i<=n):
# 	sum=sum+i
# 	i=i+1
# 	print(i)
# print("the sum is:-",sum)


# Q..........................3

# i=1
# sum=0
# while (i<=10):
# 	a=int(input("enter number: "))
# 	i+=1
# 	sum=sum+a
# print("total-",sum)


# Q................................4
# a=0
# while a<100:
# 	a+=1
# 	if a%2==0:
# 		print(-a)
# 	else:
# 		print(a)				

# ###########################

# #............counter example...  .........###
# #Q.....................Example(1)
# 1 se 40 ke beech ke saare 3 ke multiples print karne hain. Code likhte waqt yeh dhyan rakhe ki aapka counter 891 se shuru hona chahiye.
# i = 891
# while i < 931:
#   z = i - 890
#   if z % 3 == 0:
#     print(z)
#   i = i + 1

# #Q..................... . ........Example(2)
# 1 se 50 ke beech ke saare 5 ke multiples print karo. Lekin aapko % (modulus operator) ka use nahi karna hai. Uske bina karo.
# i = 0
# while i <= 50:
#   if i != 0:
#     print(i)
#   i = i + 5

# #Q.............................Example(3)
# 50 se 100 ke beech ke saare odd numbers ka sum print karo.
# i = 49
# while i <= 98:
#   i = i + 2
#   print(i)

# #Q...........................Example(3(a))
# i = 50
# while i <= 100:
#   if i % 2 != 0:
#     print(i)
#   i = i + 1

# #Q……………….............Example(3(b))
# i = 400
# while i >= 350:
#   z = i - 300
#   if z % 2 != 0:
#       print(z)
#   i = i - 1

# #Q..............................Example(4)
# 1 se 10 tak number print karne hai .incriment ka use nahi karna hai .
# a = -1
# while a >= (-10):
#     print (-a)
#     a = a -1

# #Q.................................Example(4(a))
# a = 1 
# while a <= 10:
#     print (a)
#     a = a-(-1)

# #Q............................................Example(4(b))
# a = 1
# while a !=11:
#     print (a)
#     a-=-1

# #.................Question set 2...............####
# #Q............................................1
# i=800
# while i<900:
# 	z=i-799
# 	if z%7==0:
# 		print(z)
# 	i=i+1


# #Q........................    ..........Solution

# i=1
# while i<=7:
# 	print("#"*i)
# 	i=i+1

# #Q……………………….2
# i=0
# num=int(input("How to take print number:-"))
# while i<num:
# 	i=i+1
# 	if i%3==0 and i%7==0:
# 		print("NavGurukul")
# 	elif i%3==0:
# 		print("Nav")
# 	elif i%7==0:
# 		print("Gurukul")
# 	else:
# 		print(i)


# #Q............................................3

# i=1
# sum=0
# while (i<=10):
# 	a=int(input("enter number: "))
# 	i+=1
# 	sum=sum+a
# print("total-",sum)

																		
# #Q.........................,,.....,......4							

# i=156
# while i<166:
# 	z=i-155
# 	if z%1==0:
# 		print(z)
# 	i=i+1


# #Q..................................5
# i=1
# sum=0
# while (i<=6):
# 	a=int(input("enter number: "))
# 	i+=1
# 	sum=sum+a
# print("total-",sum)

# #Q………………………….5(a)

# i=1
# sum=0
# a=int(input("How to take print number:-: "))
# while (i<=a):
# 	b=int(input("enter number: "))
# 	i+=1
# 	sum=sum+b
# print("total-",sum)

# #Q........... .........................6

# num=int(input("Enter the number"))
# if num>=1:
# 	for i in range(2, num):
# 		if (num%i)==0:
# 			print(num," is not a prime number")
# 			break
# 	else:
# 		print(num, "is a prime number")
# else:
# 	print(num," is not a prime number")

# #Q………………………….7

# i=5
# while i>=1:
# 	print(str(i)*5)
# 	i=i-1

# i=1
# while i<=5:
# 	print(str(i)*5)
# 	i=i+1


# for i in range (5,0,-1):
# 	print(str(i)*5)

# for i in range (1,5):
# 	print(str(i)*5)

# for i in range (5,0,-1):
# 	print(str(i)*5, end=" ")	


# ##№####################

# .....................Introduction to Loops

# i = 1
# while i < 100:
#   print(i)
#   i = i + 1

# i = 1
# while i <= 10:
#   print(i)    #output vertical line-  print(i, " ",end = ""))
#   i = i + 1

# i = 1
# while i != 10:
#   print(i)
#   i = i + 1
  
# for i in range (1, 10):
# 	print(i)
# ########################

# #..........…..........Break Statement

# index = 0;  
# while 1:  
#     print(index," ",end = "")
#     index=index+1
#     if index == 10:  
#         break 
# print("Found at",index,"location")

# ######################
# .. .........................continue
# counter = 0
# string = "navgurukul"
# while (counter < len(string)):
#     counter += 1

#     if string[counter] == "a":
#         continue

#     if string[counter] == "u":
#         continue
    
#     print(string[counter])

# print("The end", string[counter])

# #########################
# #......Course - Loops 101 (Using Python)
# #.... ................Question Set 3..........###

# Q............................................1

# a=20
# while a<=100:
# 	a+=1
# 	if a%2==0:
# 		print(a)

# Q.............................................2	

# i=7
# while i<=100:
# 	if i%7==0:
# 		print (i)
# 		i=i+7
		
# Q..............................................3

# i=12
# sum=0
# while i<=421:
# 	sum=sum+i
# 	print(i)
# 	i+=1
# print(" Total sum-",sum)

# Q...............................................4

# i=30
# sum=0
# while i<=420:
# 	if i%8==0:
# 		#print(i)
# 		sum=sum+i
# 		print(i)
# 	i=i+1
# print("total-", sum)

# Q...........................5

# i=1
# sum=0
# while i<11:
# 	a=int(input("Enter your no-"))
# 	sum=sum+a
# 	i+=1
# print("Average weight -",sum/5)
# if sum%5==0:
# 	print("yes")
# else:
# 	print("no")
#         #....................or........................#

# num=int(input("How many number"))
# total_sum=0
# for n in range(num):
# 	numbers=int(input("enter any number"))
# 	total_sum+=numbers
# avg=total_sum/num
# print("Average is -",avg)
# if avg%5==0:
# 	print("avg is divide")
# else:
# 	print("avg no divide")

# Q....................................6

# a=0
# while a<100:
# 	a+=1
# 	if a%2==0:
# 		print(-a)
# 	else:
# 		print(a)

# Q.7......................loop guessing game

# b=5
# i=1
# while i<=5:
# 	num=int(input("enter your number between 1 to 10 :-"))
# 	if num!=5:
# 		print("no")
# 	else:
# 		print("yes")

# Q..............................8

# b=5
# i=1
# while i<=5:
# 	num=int(input("enter your number between 1 to 10 :-"))
# 	i=i+1
# 	if num<b:
# 		print("aapka number chhota hai ! Ek aur baar try karo ")
# 	elif num>b:
# 		print("aapka number bada hai ! Ek aur baar try karo")
# 	else:
# 		print("waah ! aapne number guess kar liya")
# 		break

# Q.............................8(a)

# b=5
# i=1
# num=int(input("How many times to take input :-"))
# for i in range(num):
# 	num=int(input("enter your number between 1 to 10 :-"))
# 	if num<b:
# 		print("aapka number chhota hai ! Ek aur baar try karo ")
# 	elif num>b:
# 		print("aapka number bada hai ! Ek aur baar try karo")
# 	else:
# 		print("waah ! aapne number guess kar liya")
# 		break


# #......................................Code Output
# Q...................................1
# c = 0
# d = 1
# while c < 3:
#     c = c + 1
#     d = d * c
#     print("Loop Ke Andar", c, d)
# else:
#     print ("Loop Ke Bahar", c, d)

# Q........................................................2
# n = 6
# s = 0
# i = 1
# while i <= n:
#     s = s + i
#     i = i + 1
#     print(i)
# print("total-",s)

# Q................................................3
# i = 2
# num=int(input("Enter the number"))
# while (i<num):
#     if (num%i == 0):
#         print(num, 'is not a prime number')
#         break
#     i = i + 1
# else:
# 	print(num, 'is a prime number')


# a##.....................Debug the Code
# Q......................................1
# index =1
# while (index<=10):
#     print(index)
#     index = index + 1

# Q........................................2
# i = 0
# sum=0
# while(i <= 140):
#     if(i % 3 == 0):
#     	sum=sum+i
#     	i +=3
#     	print(i)
# print("total-",sum)

# Q...........................................3
# i=0
# while(i<10):
#    print(i)
#    i = i + 1
# j = 0
# while(j<=5):
#     	print(j)
#     	j = j + 1

# Q............................................4
# i = 0
# num = int(input("Enter your number:- "))
# while(i >= num) or (i<=num):
#     if(num > 0):
#         print("it is positive")
#     elif(num < 0):
#         print("it is negative")
#     else :
#         print("zero")
#     i = i + 1
#     break		
