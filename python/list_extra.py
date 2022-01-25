#.......w3resources_list........................

# find the item use of index in pop method .


# A=["AMIT","YADAV","BANANA"]
# k=A.pop(1)
# print(k)
# .........................................
# ......convert string in list.
# a="amit"
# b=a.split()
# print(b)
# ......convert string in list seorated by commas.

# a="amit"
# b=list(a)
# print(b)

# ........................................
# .check ascending or not.

# list1 = [1, 2, 3, 5, 4, 8, 7, 9]
# temp_list = list1
# print("original list=",temp_list)
# list1.sort()
# print("sorting list=",list1)
# if temp_list == list1:
#     print("Given List is in Ascending Order")
# else:
#     print("Given List is not in Ascending Order")
# .....................................................

# find odd and even number .

# list2 = [2, 3, 7, 5, 10, 17, 12, 4, 1, 13]
# for i in list2:
#     if i % 2 == 0:
#         print("even number is=",i)
#     elif i%2!=0:
#     	print("odd number is=",i)

# ................................

# count odd and even.

# number=[1,2,3,4,5,6,7,8,9]
# odd=0
# even=0
# for i in number:
# 	if i%2==0:
# 		even=even+1
# 	else:
# 		odd=odd+1
# print("even number",even)
# print("odd number",odd)

# ...........................................

# . sum of even and odd number.
# number=[1,2,3,4,5,6,7,8,9]
# odd=0
# even=0
# for i in number:
# 	if i%2==0:
# 		even=even+i
# 	else:
# 		odd=odd+i
# print("even number",even)
# print("odd number",odd)
# ..........................................

# . odd number.

# x = [1,2,3,4,5,1,3,3,4]
# l1 = []
# for i in x:
#     if x.count(i) % 2 != 0:
#         if i not in l1:
#             l1.append(i)
# print(l1)

#.........evan number

# x = [1,2,3,4,5,1,3,3,4]
# l1 = []
# for i in x:
#     if x.count(i) % 2== 0:
#         if i not in l1:
#             l1.append(i)
# print(l1)

# #############################################
# ......................................................

# . 
# list5 = [1, 29, 51, 9, 17, 6, 7, 23]
# list5[0], list5[-1] = list5[-1], list5[0]
# print(list5)
# ...........................................

# subtract 1 list to 2 list item .

# a = [1, 2, 3, 5]
# b = [1, 2]
# l1 = []
# for i in a:
#     if i not in b:
#         l1.append(i)
# print(l1)
#.........................................

# a = [1, 2, 3, 5]
# b = [1, 2, 3, 5, 6]
# l1 = []
# for i in b:
#     if i not in a:
#         l1.append(i)
# print(l1)


# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# list3=[]
# for i in list1:
# 	if i not in list2:
# 		list3.append(i)
# print(list3)

# ...............................................

# find 1st,2nd,3rd largest number ?

# mylist=[10,22,78,55,1]
# mylist.sort()
# print("original number",mylist)
# print("1st largest number",mylist[-1])
# print("1st smaallest number",mylist[0])
# print("2nd largest number",mylist[-2])
# print("3rd largest number",mylist[-3])

# a=[]
# x=int(input("how many number are needed:"))
# for i in range(x):
#     number=input("Enter number-")
#     a.append(number)
#     a.sort()
# print("original number",a)
# print("1st max number",a[-1])
# print("2nd max number",a[-2])
# print("3rd max number",a[-3])
# .............................................

# ...................remove dublicate number.
# a=[1,2,2,3,5,8,2,6,4,6,1]
# b=[]
# for i in (a):
# 	if i not in b:
# 		b.append(i)
# print("original list=",a)
# b.sort()
# print("remove dublicate item=",b)

# ................remove dublicate number/string.
# a=[]
# size=int(input("how many number are needed:"))
# for i in range(size):
#     number=input("Enter number-")
#     a.append(number)
# print("oridinal list",a)
# b=[]
# for i in a:
# 	if i not in b:
# 		b.append(i)
#       b.sort()
# print("remove dublicates",b)		



# .................................................

# remove dublicate string.
# a=[]
# b=["a","b","a","c","a","d","a","c"]
# for i in (b):
# 	if i not in a:
# 		a.append(i)
# 		a.sort()
# print(a)



# ............................................
# .........student name and marks highest and lowest. 

# names=[]
# marks=[]
# size=int(input("Enter number-"))
# for i in range(size):
# 	n=input("Enter names-")
# 	m=int(input("Enter marks-"))
# 	names.append(n)
# 	marks.append(m)
# h=max(marks)
# l=min(marks)
# #print("highest marks",h)
# #print("lowest marks",l)
# for i in range(size):
# 	if h==marks[i]:
# 		print("stu having higtest marks is=",names[i],h)
# 	if l==marks[i]:
# 		print("stu having lowest marks is=",names[i],l)
# ...................................................

# adding in list number .

# items=[1,2,3,4]
# sum_numbers = 0
# for x in items:
#   sum_numbers += x
# print(sum_numbers)
# .............................................

# mixed list
# mixed_list = ["rahul", 12, 9.0, "kaavay", "shivam", 1]
# print (type(mixed_list))

# .......................................

# names_list = ["rahul", "shivam", "kavay", "ashish", "rohit"]
# print (names_list)
# print (type(names_list))
# ........................................

# .....all method use in this qurstion.

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# # access item pop
# # specifi index access
# # by defalt last item access
# print(len(names_list))
# print(names_list)
# c=names_list.pop()
# b=names_list.pop(3)
# print(c)
# print(b)
# print(names_list)
# print(len(names_list))

# print(names_list[1])
# print (names_list[:-1]) # access with index (-1) last item.
# print (names_list[ 0:]) # access with index start to end.
# print (names_list[ ::-1]) # reverce item with index.
# names_list[1]="amit" # # change with index
# print(names_list)
# names_list[1:3]=["yavav","kumar"] # # change with index
# print(names_list)
# names_list[-1]="mama" # change with index
# print(names_list)
# names_list.insert(4,"nayan") # add(insert with index) 
# print(names_list)
# name=names_list # copy list
# print(name)

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# names_list.append("dhruv")
# print ("length of the list is ", len(names_list))
# print (names_list)

# ......................................................
# ..remove item with index and find length.

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# print(names_list)
# print ("length of the list is ", len(names_list))
# names_list.pop(2)
# print(names_list)
# print ("length of the list is ", len(names_list))
# names_list.pop(2)
# print(names_list)
# print ("length of the list is ", len(names_list))
# .......................................................

# check name in list yes or not.

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# name=input("Enter name check : ")
# for i in names_list:
# 	if name in names_list:
# 		print (name,"ka naam names_list mei hai")
# 	else:
# 		print (name,"ka naam names_list mei nahi hai.")
# 	break
# .......................................................

# ...find average,min,max,sum ?

# n=int(input("Enter number-"))
# a=list()
# for i in range(n):
# 	elem=int(input("Enter number-"))
# 	a.append(elem)
# s=sum(a)
# Avg=s/len(a)
# mi=min(a)
# ma=max(a)
# print("min number is=",mi) 		# find min number
# print("max number is=",ma) 		# find max number
# print("second max is=",a[-2])	# find 2nd max number
# print("sum of number is=",s)	# find sum of number
# print("Average number is=",Avg)	# find Average of number

# ##############################################

# #...input nested list all list same value

# t=[]
# n=int(input("Enter size :"))
# for a in range(n):
# 	ta=[]
# 	for b in range(n):
# 		va=int(input("Enter value :"))
# 		ta.append(va)
# 	t.append(ta)
# print(t)

# #############################################################

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# s=sum(elements)
# print("sum of num",s)
# print("len of num=",len(elements))
# print("Average=",s/len(elements))

# #################################################

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[-3:-1] = ["watermelon","blackcurrant"]
# print(thislist)

# ####################################################

# #.Q. simple output
# # count(odd & even & all numner)
# # sum(odd & even& all numner)
# # average(odd & even & all numner)

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# even=ecount=evcount=0
# odd=ocount=odcount=0
# for i in elements:
# 	if i%2==0:
# 		even+=i   		# sum of even number
# 		ecount+=1 		# cout of even number
# 		evcount+=1      # avg of even number
# 	else:
# 		odd+=i          # sum of odd number
# 		ocount+=1       # count of odd number
# 		odcount+=1      # avg of odd number
# count=0               
# for i in elements:    
# 	count+=1            # count of all number

# a=sum(elements)       # sum of all numbeer
# l=len(elements)       # len of all number
# avg=a/l

# # print("count of odd numbers=",odcount)
# # print("count of even numbers=",evcount)
# # print("count of all number=",count)
# # print("sum of odd numbers=",odd)
# # print("sum of even numbers=",even)
# # print("sum of all number",a)
# # print("Avg of odd numbers in list=",int(odd/ocount))
# # print("Avg of even numbers in list=",int(even/ecount))
# # print("average of all number=",int(avg))


# print("count of odd numbers=",odcount,"..count of even numbers=",evcount,"...count of all number=",count,"...sum of odd numbers=",odd,"...sum of even numbers=",even,"...sum of all number",a,"...Avg of odd numbers in list=",int(odd/ocount),"...Avg of even numbers in list=",int(even/ecount),"...average of all number=",int(avg))

# #######################################################

# Q...How to input Nested list ?

# t=[]
# n=int(input("Enter size :"))
# for a in range(n):
# 	ta=[]
# 	for b in range(n):
# 		va=int(input("Enter value :"))
# 		ta.append(va)
# 	t.append(ta)
# print(t)

# ###########################################################



# # kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# # corodpati=lakhpati=dilwale=0
# # for i in kitna_paisa_hai:
# # 	if i>=10000000:
# # 		corodpati+=1
# # 	elif i>=100000:
# # 		lakhpati+=1
# # 	else:
# # 		dilwale+=1
# # print(corodpati,"corodpati")
# # print(lakhpati,"lakhpati")
# # print(dilwale,"dilwale")




# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# # # print(thislist[2:])
# # # print(thislist[:4])
# # # print(thislist[2:5:2])

# print(thislist[-1:-3])
# note slicing do not work from right to left. work only left to right.
# # print(thislist[:-1])
# # print(thislist[-2:])


# # thislist = ["apple", "banana", "cherry"]
# # del (thislist)
# # print(thislist)


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(thislist)
# print(mylist)

# #List method () - 

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# list1 = [True,bool(1),bool(0),bool(),()]
# print(list1)

##############################################################

#.Q..Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

# def printValues():
# 	l = list()
# 	for i in range(1,21):
# 		l.append(i**2)
# 	print(l[:])
# printValues()

#############################################################

#.Q.22...find the index of an item in a specified list.

# num =[10, 30, 4, -6]
# print(num.index(30))

#######################################

#.Q.23....nested list convert into simple list

# import itertools
# original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# new_merged_list = list(itertools.chain(*original_list))
# print(new_merged_list)


######################################


#.Q.24...........add tow list
# list1 = [1, 2, 3, 0]
# list2 = ['Red', 'Green', 'Black']
# final_list = list1 + list2
# print(final_list)


# list1=[1,2,3,0]
# list2 = ['Red', 'Green', 'Black']
# list1.extend(list2)
# print(list1)

# list1 = [1, 2, 3, 0]
# list2 = ['Red', 'Green', 'Black']
# for x in list2:
#   list1.append(x)

# print(list1)


# list1 = [1, 2, 3, 0]
# list2 = ['Red', 'Green', 'Black']
# list1.append(list2)

# print(list1)

####################

#.Q.25....select an item randomly from a list.
#Use random.choice() to get a random element from a given list.

# import random
# color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
# print(random.choice(color_list))

#################

# a=input("Enter name :")
# b=list(a)
# c=b[::-1]
# for i in c:
# 	print("reverce string",c)
# 	if b==c:
# 		print("palindrome")
# 	else:
# 		print("not palindrome")
# 	break

#############################

#.Q.29....get unique values from a list.

# my_list = [10, 20, 30, 40, 20, 50, 60, 40]
# print("Original List : ",my_list)
# my_set = set(my_list)
# my_new_list = list(my_set)
# my_new_list.sort()
# print("List of unique numbers : ",my_new_list)

###############################

#.Q.34...prime number

# def prime_eratosthenes(n):
#     prime_list = []
#     for i in range(2, n+1):
#         if i not in prime_list:
#             print (i)
#             for j in range(i*i, n+1, i):
#                 prime_list.append(j)

# print(prime_eratosthenes(100));

##################################

#.Q....letter you want to world

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "e" in x:			
#     newlist.append(x)

# print(newlist)

#####################################3

#.Q...convert Decimal to binary number

# n=int(input('Enter Decilmle number-'))
# l=[]
# while (n!=0):
# 	a=n%2
# 	l.append(a)
# 	n=n//2
# l.reverse()
# print(l)

#.................................
#.Q....convert binary to Decimal number


# n=int(input('Enter Binary  number-'))
# final=0
# l=0
# while (n!=0):
# 	a=n%10
# 	a=a*2**l
# 	l+=1
# 	final+=a
# 	n=n//10
# print(final)

##################################

#. Q.....output is (1,3)

# n = [1,2,2,3]
# a=[]
# for i in (n):
# 	if i not in a:
# 		a.append(i)
# print("original list=",n)
# a.sort()
# print("remove dublicate item=",a)

# a=[1,2,2,3]
# a.remove(2)
# a.remove(2)
# print(a)


# n = [1,2,2,3]
# n[1:3]=[]
# print(n)

#.............................

# Q.remove dublicate with input

# a=[]
# size=int(input("how many number are needed:"))
# for i in range(size):
#     number=int(input("Enter number-"))
#     a.append(number)
# print("oridinal list",a)
# b=[]
# for i in a:
# 	if i not in b:
# 		b.append(i)
# 		b.sort()
# print("remove dublicates",b)	

##################################

# Q...How to input Nested list ?

# t=[]
# n=int(input("Enter size :"))
# for a in range(n):
# 	ta=[]
# 	for b in range(n):
# 		va=int(input("Enter value :"))
# 		ta.append(va)
# 	t.append(ta)
# print(t)

#################################

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# list3=[]
# for i in list1:
# 	if i not in list2:
# 		list3.append(i)
# print(list3)


#######################################################

# Q....fibonacci numbwer

# x=0
# y=1
# z=0
# while z<100:
# 	print(z)
# 	x=y
# 	y=z
# 	z=x+y

#.....................................

#.... check if it's fibnacci number ?
# 	#.Q...input=8
# 	#.....output=yes
# 	#.Q...input=34
# 	#....output=yes
# 	#.Q...input=41
# 	#...output= no

# b=int(input("Enter fibonacci number-"))
# x=0
# y=1
# z=0
# while z<b:
# 	x=y
# 	y=z
# 	z=x+y
# if z==b:
# 	print("yes")
# else:
# 	print("no")



#.....................................


# x=0
# y=1
# z=0
# d=0
# count=0
# n=int(input("Enter number-"))
# m=int(input("Enter number-"))
# while True:
# 	count+=1
# 	x=y
# 	y=z
# 	z=x+y
# 	if z%n==0:
# 		d+=1
# 	if d==m:
# 		break
# print(count)

#.............................................................