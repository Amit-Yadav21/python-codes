#  Q.................................Add tow number

# a=int(input("Enter number 1st:"))
# b=int(input("Enter number 2nd :"))
# result=a+b
# print("sum of two number",result)
#  ............................................................
#  Q........print first 10 natural using while loop.

# i=1
# while i<=10:
# 	print(i)
# 	i=i+1
# ...........................................................
# Q........print pattern.

# row = 5
# for i in range(1, row + 1):
#     # Run inner loop i+1 times
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     # empty line after each row
#     print("")


# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# .........................................................

# Q.....calculat the sum of all naturl from 1 to given number.

# a=int(input("Enter number-"))
# i=0
# sum=0
# while i<=a:
# 	sum=sum+i
# 	i=i+1
# 	print(i)
# print("Total=",sum)


# a=int(input("Enter number-"))
# sum=0
# for i in range(1,a+1):
# 	sum=sum+i
# 	print(i)
# print("Total=",sum)
# ..............................................................

# Q...Write a program to print multiplication table of a given number.

# a=int(input("Enter number-"))
# for i in range(1,11):
# 	product=a*i
# 	print(product)

# a=int(input("Enter num number-"))
# for i in range(1,11):
# 	print(a*i)
# ........................................................................

# Q........Count the total number of digits in a number.

# a=input("Enter number-")
# d=0
# for i in (a):
# 	if i.isdigit():
# 		d=d+1
# print("Digit=",d)


# num=int(input("Enter number-"))
# count = 0
# while num != 0:
#     num = num // 10
#     count = count + 1
# print("Total digits are:", count)
# .............................................................................

# Q..... Print the following pattern.

# a=5
# for i in range(a,0,-1):
#     for j in range(1,i + 1):
#         print(j,end=" ")
#     print()

# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1

# ...........q.

# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=' ')
#     print()

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
# ....................................................................

# Q.....Display numbers from -10 to -1 using for loop.

# a=int(input("Enter number-"))
# for num in range(-a, 0, 1):
#     print(num)

# ........................................................................
# Q....Write a program to display all prime numbers within a range.

# a=int(input("Enter number-"))
# count=0
# for i in range(1,a+1):
# 	if a%i==0:
# 		count=count+1
# if count==2:
# 	print("prime  number")
# else:
# 	print("not prime number")



# start =int(input("Enter 1st number-"))
# end =int(input("Enter 2nd number-"))
# print("Prime numbers between", start, "and", end, "are:")
# for num in range(start, end + 1):
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

# .....................................................................

# Q...........fibnoccis series number.

# a, b = 0, 1
# c=int(input("Enter number-"))
# print("Fibonacci sequence:")
# # run loop 10 times
# for i in range(c):
#     # print next number of a series
#     print(a)
#     # add last two numbers to get next number
#     res = a + b

#     # update values
#     a = b
#     b= res


# n=int(input("Enter number-"))
# x=0
# y=1
# z=0
# while z<=n:
#     print(z)
#     x=y
#     y=z
#     z=x+y

# ........................................................................

# Q..............Find the factorial of a given number.

# fac=1
# a=int(input("Enter number-"))
# for i in range(1,a+1):
#   fac=fac*i
#   print(i)
# print("total=",fac)

# .................................................................

# Q........Calculate the cube of all numbers from 1 to a given number.

# input_number = 6
# for i in range(1, input_number + 1):
#     print("Current Number is :", i, " and the cube is", (i * i * i))

# ....................................................................

# ...................Q

#  for i in "Myblog":
#          print (i, '?')
# M ?
# y  ?
# b ?
# l  ?
# o ?
# g ?    
# ......................................................................

#  for i in range(5):
#         print(i)
# output.
# 0
# 1
# 2
# 3
# 4
# ..............................................................

# for i in range(10,15):
#         print(i)
# output.
# 10
# 11
# 12
# 13
# 14
# ........................................................

# Write a program to print first 10 natural number.
# output.
# for i in range(1,11):
#       print(i)

# ............................................

# Write a program to print first 10 even numbers.

# output.
# for i in range(2,22,2):
#      print(i)
# ...............................................

# Write a program to print first 10 odd numbers.

# output.
# for i in range(1,21,2):
#       print(i)
# ..............................................

# Write a program to print first 10 even numbers in reverse order.

# output.
# for i in range(20,0,-2):
#       print(i)
# .............................................

# Q....Write a program to print table of a number accepted from user.
# output.
# num = int(input("Enter any number")
# for i in range(1,11):
#       print(num*i)

# .................................................

#  Q........Write a program to display product of the digits of a number accepted from the user.
# .....output.
# num=int(input("Enter any number"))
# p=1
# while(num):
#    r=num%10
#    p=p*r
#    num=num//10
# print("Product of digits is",p)
# ...........................................................
# Q...Write a program to find the factorial of a number.
# ....output.
# num=int(input("Enter any number"))
# f=1
# for i in range(1,num+1):
#     f=f*i
# print("Factorial is",f)
# .........................................................
# ...Write a program to find the sum of the digits of a number accepted from user
# ....output.
# num=int(input("Enter any number"))
# s=0
# while(num):
#    r=num%10
#    s=s+r
#    num=num//10
# print("Sum of digits is",s)
# ...........................................................
# ...Write the output of the following
# # Q...................1
# for i in (1,10)
#     print(i)
# output-(1,10)
# .............................................................
# Q...................2
#  for i in range(2,7):
#       - print(i)
# output-
# 2
# 3
# 4
# 5
# 6
# ..........................................................
#  Q ..........................3
#  for i in "python":
#        print(i, end=' ')
# output-
# p y t h o n

#  for i in "python":
#        print(i)
# output-
# p
# y
# t
# h
# o
# n

# for i in "python":
#         print(i, '?$')
# output-
# p?$y?$t?$h?$o?$n?$

#  for i in "python":
#       print(i, end=='?')
# output-
# p?y?t?h?o?n?


# ........................................................

# for i in range(2,10,2):
#     print(i)
# output-
# 2
# 4
# 6
# 8
# ......................................................
# x=5
# while(x<15):
#   print(x**2)
#   x+=3
# output-
# 25
# 64
# 121
# 196
# ......................................................
# b=5
# while(b<9):
#   print("H")
#   b+=1
# output-
# H
# H
# H
# H
# .....................................................

# b=15
# while(b>9):
#   print("Hello")
#   b=b-2
# output-
# Hello
# Hello
# Hello
# ......................................................
# x=15
# while(x==15):
#   print("Hello")
#   x=x-3
# outut-
# Hello
# ...................................................

# x = "123"
# for i in x:
#   print("a")
# output-
# a
# a
# a
# ......................................

# i=9
# while True:
#   if i%3==0:
#     break
#   print("A")
# output-
# Loop will not execute
# .....................................

# i=0
# while i<3:
#   print(i)
#   i=i+1
# else:
#   print(7)
# output-
# 0
# 1
# 2
# 7
# ...............................

# i=0
# while i<3:
#   print(i)
#   i=i+1
#   print(0)
# output-
# 0
# 0
# 1
# 0
# 2
# 0
# ..............................

# i=2
# for x in range(i):
#   i+=1
#   print(i)
#   print(i)
# output-
# 3
# 3
# 4
# 4
# ............................
# i=2
# for x in range(i):
#   x+=1
#   print(x)
# print(x)
# output-
# 1
# 2
# 2
# .................................

# i=2
# for x in range(i):
#   x+=1
#   print(x)
#   print("x")
# output-
# 1
# x
# 2
# x
# ....................................

# i=100
# while i<57:
#   print(i)
#   i+=5
# output-
# Loop will run infinite times
# ........................................
# Accept 10 numbers from the user and display their average.

# output-
# s=0
# for i in range(10):
# n=int(input("Enter number"))
# s=s+n
# print("Average of 10 numbers is ",s/10)

# .................................................
# Q........................half capital and half small.
# a=input("Enter srtinge-")
# b=len(a)
# c=len(a)//2
# d=a[:c]
# e=a[c:]
# print(d.upper()+e.lower())
# output-AMit

# ...................................................

# Q....Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)

# so=0
# se=0
# for i in range(1,10):
#    if i % 2==0:
#       se=se+i
#    else:
#       so=so+i
# print("Sum of all even numbers is ",se)
# print("Sum of all odd numbers is ",so)

# .................................................

# Q..Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.

# for i in range(100,500):
#    if i%11==0 and i%2!=0:
#       print(i)

# .....................................................

# Q.......Write the output of the following.

# c = -9
# while c < 20:
#   c += 3
#   print(c)

# output-
# -6
# -3
# 0
# 3
# 6
# 9
# 12
# 15
# 18
# 21

# .....................................................

# Q.....Write a program to print numbers from 1 to 20 except multiple of 2 & 3.

# for i in range(1,21):
#    if i%2!=0 and i%3!=0:
#        print(i)

# .......................................................

# Q....Write a program that keep on accepting number from the user until user enters Zero. Display the sum and average of all the numbers.
# unlimited input when pess (0) stop take input? 
# num=1
# i=-1
# s=0
# while(num!=0):
#    num=int(input("Enter any number : "))
#    s=s+num
#    i=i+1
# print("Average of numbers entered by you is ",s/i)


# s=0
# for i in range(10):
#     n=int(input("Enter number"))
#     s=s+n
# print("Average of 10 numbers is ",s/10)

# .......................................................

# Q.......Find errors in the following code:

# a = int(“Enter any number”)
# for i in Range[2,6]
#     if a=i
#       print(“A”)
#     else
#       print(“B”)

# output-

# a = int(input(“Enter any number”))
# for i in range(2,6):
#     if a==i:
#       print(“A”)
#     else:
#       print(“B”)


# Q........Find errors in the following code:

# x = input(“Enter value”)
# for k in range[0,20]
#     if x=k
#         print(x+k)
#    else:
#        Print(x-k)

# output-
# x = input("Enter value")
# for k in range(0,20):
#     if x==k:
#        print(x+k)
#     else:
#        print(x-k)

# .............................................

# Q...Write the output of the following.

# a=5
# while a>0:
#    print(a)
#    a=a-1

# output-
# 5
# 4
# 3
# 2
# 1

# ....................................................

# Q......Convert the following loop into for loop :
# x = 4
# while(x<=8):
#     print(x*10)
#     x+=2

# ##output-
# for x in range(4,9,2):
#     print(x*10)

# .........................................................

# Q...........Write the output of the following:

# x=10
# y=1
# while x>y:
#     x=x-4
#     y=y+3
#     print(x)

# output-

# 6
# 2
# .......................................................

# find remainder without using modulus?

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
#   pro=pro+a
# print("multiply is=",pro)


# a=int(input("Enter number-"))
# b=int(input("Enter number-"))
# c=1
# d=0
# while c<=b:
#     d+=a
#     c+=1
# print("multification of number",d)
#.........................................

 
# a=int(input("Enter number-"))
# x=0
# y=1
# z=0
# for i in range(1,a+1):
#     print(z)
#     x=y
#     y=z
#     z=x+y


# for a in range(10): 
#     count=0
#     for i in range(1,a+1):
#         if a%i==0:
#             count=count+1
#     if count==2:
#         print(i, end='')
# print()


# sum=0
# a=int(input("Enter number-"))
# n=a
# while n>0:
#     rem=n%10
#     sum=sum+rem
#     n=n//10
# if a%sum==0:
#     print(a,"is a harshad number")
# else:
#     print(a,"is not a harshad number")
