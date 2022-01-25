# Q.14...print the numbers of a specified list after removing even numbers from it.

# num = [7,8, 120, 25, 44, 20, 27]
# num = [x for x in num if x%2!=0]
# print(num)              #.....output in list 

# num = [7,8, 120, 25, 44, 20, 27]
# for x in num:
# 	if x%2!=0:
# 		print(x)		  #...output not list.But vertical line

# num = [7,8, 120, 25, 44, 20, 27]
# for i in num:
# 	if i%2==0:
# 		print(i)  # odd number

######################################################
# Q.12.. print a specified list after removing the 0th, 4th and 5th elements.

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(color)

####################################################

#.Q.21.convert a list of characters into a string.
# s = ['a', 'b', 'c', 'd']
# str1 = ''.join(s)
# print(str1)

##################################################

# Q.22...find the index of an item in a specified list.
# num =[10, 30, 4, -6]
# print(num.index(-6))

#####################################

# Q.24...append a list to the second list.

# list1 = [1, 2, 3, 0]
# list2 = ['Red', 'Green', 'Black']
# final_list = list1 + list2
# print(final_list)
#-------------------
# for x in list2:
#   list1.append(x)
# print(list1)

#################################

# Q...29..unique values from a list.
# my_list = [10, 20, 30, 40, 20, 50, 60, 40]
# print("Original List : ",my_list)
# my_set = set(my_list)
# my_new_list = list(my_set)	
# my_new_list.sort()
# print("List of unique numbers : ",my_new_list)

##################################

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

##################################

# Q.36.....variable unique identification number or string
# x = 100
# print(format(id(x), 'x'))
# s = 'w3resource'
# print(format(id(s), 'x')) 

###################################

# Q.37....find common items from two lists. 

# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# print(set(color1) & set(color2))

######################################

#.Q.39......convert a list of multiple integers into a single integer.

# L = [11, 33, 50]
# print("Original List: ",L)
# x = int("".join(map(str, L)))
# print("Single Integer: ",x)

#########################################3

#.Q..create miltiple list

# obj = {}
# for i in range(1, 21):
#     obj[str(i)] = []
# print(obj)

#####################################

#. Q..45....convert a pair of values into a sorted unique array.

# L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
#  (7, 8), (9, 10)]
# print("Original List: ", L)
# print("Sorted Unique Data:",sorted(set().union(*L)))

# #.......................................................

# L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
#  (7, 8), (9, 10)]
# print("Original List: ", L)
# print("Sorted Unique Data:",sorted(set().union(L)))

#################################################

# lst1=[2,3,4]
# lst2=[4,6,7]
# u=list(set().union(lst1,lst2))
# print("\nThe union of two list is:",u)

# def Union(lst1, lst2):
#     final_list = sorted(lst1 + lst2)
#     return final_list
  
# # Driver Code
# lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
# lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
# print(Union(lst1, lst2))

########################################

# Q. 52.......compute the difference between two lists.

# from collections import Counter
# color1 = ["red", "orange", "green", "blue", "white"]
# color2 = ["black", "yellow", "green", "blue"]
# counter1 = Counter(color1)
# counter2 = Counter(color2)
# print("Color1-Color2: ",list(counter1 - counter2))
# print("Color2-Color1: ",list(counter2 - counter1))

#######################################33

# Q.54.....join in alist item 

# color = ['red', 'green', 'orange']
# print('-'.join(color))
# print(''.join(color))

#########################################

# Q.57....check if all items of a given list of strings is equal to a given string.

# color1 = ["green", "orange", "black", "white"]
# color2 = ["green", "green", "green", "green"]

# print(all(c == 'black' for c in color1))
# print(all(c == 'white' for c in color2))

################################################

# Q.58....replace the last element in a list with another list.

# num1 = [1, 3, 5, 7, 9, 10]
# num2 = [2, 4, 6, 8]
# num1[-1:] = num2
# print(num1)

####################################################

# Q.59... access items with index in last.

# x = [1, 2, 3, 4, 5, 6]
# print(x)
# n=int(input("Enter number who access items :"))
# xlen = len(x)-n         
# print(x[xlen])

##########################################
# Q.62... input name and number , remove comma and string ?

# num = [1, 2, 3, 4, 5]
# print(*num)

# a=[]
# size=int(input("how many number are needed:"))
# for i in range(size):
#     num=input("Enter number-")
#     a.append(num)
# print(a)
# print(*a)

##########################################

# Q.64...iterate over two lists simultaneously.

# num = [1, 2, 3]
# color = ['red', 'white', 'black']
# for (a,b) in zip(num, color):
#      print(a, b)

###########################################

# Q.66 find max nestesd list 

# num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# print(max(num, key=sum))

# output-- [10, 11, 12 ]

#..............................................

# t=[]
# n=int(input("Enter size : "))
# for a in range (n):
# 	ta=[]
# 	for b in range (n):
# 		va = int(input("Enter value : "))
# 		ta.append(va)
# 	t.append(ta)
# print(t)
# print("max nested list in sum=",max(t, key=sum))

#33333333333333333333333333333333333333333333333

# Q.202 find the indexes of all None items in a given list.

# def relative_order(lst):
#     result = [i for i in range(len(lst)) if lst[i] == None]
#     return result

# nums = [1, None, 5, 4,None, 0, None, None]
# print("Original list:")
# print(nums)
# print("\nIndexes of all None items of the list:")
# print(relative_order(nums))

#######################################################

# Q..203  join adjacent members of a given list.


# def test(lst):
#     result = [x + y for x, y in zip(lst[::2],lst[1::2])]
#     return result

# nums = ['1','2','3','4','5','6','7','8']
# print("Original list:")
# print(nums)
# print("\nJoin adjacent members of a given list:")
# print(test(nums))

#######################################################

# Q.211 remove an element from a given list.

# student = ['Ricky Rivera', 98, 'Math', 90, 'Science']
# print("Original list:")
# print(student)
# print("\nAfter deleting an element:, using index of the element:")
# del(student[3])
# print(student)

#######################################################

# Q.67  find all the values in a list are greater than a specified number.

# list1 = [220, 330, 500]
# list2 = [12, 17, 21]
# print(all(x >= 200 for x in list1))
# print(all(x >= 25 for x in list2))

###########################################################

# Q.68 extend a list without append.

# x = [10, 20, 30]
# y = [40, 50, 60]
# x[:0] =y
# print(x)

# y.extend(x)
# print(y)			# output : [40, 50, 60, 10, 20, 30]

#################################################

# Q.69 remove dunlicate 

# num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# a=[]
# for i in num:
# 	if i not in a:
# 		a.append(i)
# print("original list=",num)
# a.sort()
# print("remove dublicate item=",a)

#.............................................

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13,17,17, 11,17,33,17]
# print("original list-",n)
# for s in n:
#     b=n.count(s)
#     if b>1:
#         n.remove(s)
# for s in n:
#     b=n.count(s)
#     if b>1:
#         n.remove(s)
# print("remove items in list=",n)

##################333333333################3

# Q.86 create a n times number  with numbers.

# a=int(input("Enter how many times : "))
# b=int(input("Enter numbers : "))
# nums = []
# for i in range(a):
#     nums.append([])
#     for j in range(1, b):
#         nums[i].append(j)
# print("n times numbers with numbers =",nums)

##############################################

# the = ["apple", "banana", "cherry"]
# a=the.pop(1)
# print(a)

###############################

# number print ( zero to n-tn input) take input ?.

# a = int(input("Enter number- "))
# new = [x for x in range(a)]
# print(new)
##################################3

# print the caital letter list

# name = ["apple", "amit", "kumar", "yadav", "mama"]
# newname = [x.upper() for x in name]
# print(newname)	

######################################

# Q.85.create a multidimensional list (lists of lists) with zeros.

# nums = []
# for i in range(3):
#     nums.append([])
#     for j in range(2):
#         nums[i].append(0)
# print("Multidimensional list:")
# print(nums)

######################################
# Q. 90   count number of lists in a given list of lists.

# def count_list(input_list): 
#     return len(input_list) 
      
# list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]] 
# list2 = [[2, 4], [[6,8], [4,5,8]], [10, 12, 14]]   
# print("Original list:")
# print(list1)
# print("\nNumber of lists in said list of lists:")
# print(count_list(list1))
# print("\nOriginal list:")
# print(list2)
# print("\nNumber of lists in said list of lists:")
# print(count_list(list2))