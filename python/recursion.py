# def amit():
# 	print("addition of the =")
# 	amit()
# amit()
# ************************************************** sum of 1 to n number ?

# def sum(n):
# 	if n==1:
# 		return 1 
# 	else:
# 		return (n+sum(n-1))
# n=int(input("Enter number :"))
# print("sum of 1 to", n  ,"number is -",sum(n))
# .............OR............... OR...............OR...............OR
# def rec(n):
# 	if n==1 :
# 		return 1    # This is a Base Case
# 	return (n+rec(n-1))
# last = int(input("Enter the upper limit :"))
# s = rec(last)
# print("Sum of series from 1 to  ", last," is :", s)

# ************************************************* print string reverce order using recursino ?
# def xyz(s,n):		# len(s) value stor of n ?
# 		if n==0:
# 			print(s[0])
# 		else:
# 			print(s[n],end="")
# 			xyz(s,n-1)
# s=input("Enter name :")
# xyz(s,len(s)-1)
# ******************************************************* find power of x,y/ x multiply y times?
# def power(x,y):
# 	if y==0:
# 		return 1
# 	else:
# 		return (x*power(x,y-1))
# x=int(input("Enter bace :"))
# y=int(input("Enter Exponent :"))
# print("power of",x,y  ,"is =",power(x,y))
# ************************************************************ find factorial ?
# def fact(n):
# 	if n==0:		# n==0/n==1/n<2
# 		return 1
# 	else:
# 		return n*fact(n-1)
# n=int(input("Enter number :"))
# print("factorial of ",n,"is",fact(n))
# .....OR.......OR........OR.......OR.........OR
# def Recur_facto(n):     
#     if (n == 0): 
#         return 1    
#     return n * Recur_facto(n-1) 
# # print the result
# print(Recur_facto(6))
# .........OR............OR..........OR...............OR
# def fact(n):
# 	if n<2:
# 		return 1
# 	# fn=fact(n-1)
# 	# fn=n*fn
# 	# return fn
# 	return n*fact(n-1)
# a=int(input("Enter number :"))
# print(fact(a))

# ************************************************************* find gcd value ?
# def gcd(p,q):
# 	if q==0:
# 		return p
# 	else:
# 		return (gcd(q,p%q))
# p=int(input("Enter 1st no. :"))
# q=int(input("Enter 2nd no. :"))
# z=gcd(p,q)
# print("Gcd value is =",z)
# ********************************************************* Fibonacci series ?
# def recursive_fibonacci(n):
#    if n <= 1:
#        return n
#    else:
#        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
   
# n_terms = 10
   
# # check if the number of terms is valid
# if n_terms <= 0:
#    print("Invalid input ! Please input a positive value")
# else:
#    print("Fibonacci series:")
#    for i in range(n_terms):
#        print(recursive_fibonacci(i))
# ...........OR..........OR..............OR...............OR
# ........................ fibonacci 0 to n(number) ?
# def fibo(n):
# 	if n==1:
# 		return 0
# 	if n==2:
# 		return 1
# 	return fibo(n-1)+fibo(n-2)
# n=int(input("Enter no. :"))
# for i in range(1,n+1):
# 	print(fibo(i))
# ...........OR..........OR..............OR...............OR
# ........................ fibonacci fix position of number ?
# def fibo(n):
# 	if n<2:
# 		return 1
# 	return fibo(n-1)+fibo(n-2)
# a=int(input("Enter nu number :"))
# print(fibo(a))

# *********************************************************************** reverse ?
# def reverse(array):
#   if len(array) == 0:
#     return []
#   elif len(array) == 1 : 
#    return array
#   return [array[len(array) - 1]] + reverse(array[:len(array) - 1])
# array = [1, 2, 3, 4]
# print(reverse(array))

# ..................................************************
# ..................................************************

# def func (i):
# 	if i==1:
# 		return "a"
# 	ans= func(i-1)
# 	return "a"+ans
# b=func(4)
# print(b)
# ..........................
# def func (i):
# 	if i==1:
# 		return "a"
# 	else:
# 		return "a"+func(i-1)
# b=func(4)
# # print(func(4))
# print(b)

# a=""
# i=5
# while i>0:
# 	a+="@"
# 	i-=1
# print(a)

# ****************************************** convert str to int ?
# def str_to_int(s,n):
# 	if not s:
# 		return n
# 	n=n*10+int(s[0])
# 	return str_to_int(s[1:],n)
# print(str_to_int("1112225544566",0))

# ****************************************************** facttorial

# def fact(n):
# 	if n<2:
# 		return 1
# 	fn=fact(n-1)
# 	fn=n*fn
# 	return fn
# 	# return n*fact(n-1)
# a=int(input("Enter number :"))
# print(fact(a))

# ******************************************* pattern star ?

# def f(n,i):
# 	if n<i:
# 		return
# 	print("*"*i)
# 	f(n,i+1)
# f(5,1)
# ............... output 

# *
# **
# ***
# ****
# *****

# ........................................................
# .......OR ........OR .....OR ..... reverse order ?
# def f(n,i):
# 	if n<i:
# 		return
# 	f(n,i+1)
# 	print("*"*i)
# f(5,1)
# ................... output ?

# *****
# ****
# ***
# **
# *

# ..............................................
# .....OR.........OR.........OR ?
# def f(n,i):
# 	if n<i:
# 		return
# 	print("*"*i)
# 	f(n,i+1)
# f(5,1)
# def f(n,i):
# 	if n<i:
# 		return
# 	f(n,i+1)
# 	print("*"*i)
# f(5,1)
# ............................. output ?

# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *

# ******************************* star pattern given 1 argument ?
# def f(n):
# 	if n==1:
# 		print("*")
# 		return
# 	f(n-1)
# 	print("*"*n)
# f(5)
# ...................... output ?

# *
# **
# ***
# ****
# *****



# def mergeSort(myList):
#     if len(myList) > 1:
#         mid = len(myList) // 2
#         left = myList[:mid]
#         right = myList[mid:]

#         # Recursive call on each half
#         mergeSort(left)
#         mergeSort(right)

#         # Two iterators for traversing the two halves
#         i = 0
#         j = 0
        
#         # Iterator for the main list
#         k = 0
        
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#               # The value from the left half has been used
#               myList[k] = left[i]
#               # Move the iterator forward
#               i += 1
#             else:
#                 myList[k] = right[j]
#                 j += 1
#             # Move to the next slot
#             k += 1

#         # For all the remaining values
#         while i < len(left):
#             myList[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             myList[k]=right[j]
#             j += 1
#             k += 1

# myList = [54,26,93,17,77,31,44,55,20]
# print("original list is here = ",myList)
# mergeSort(myList)
# print("marge sort list =",myList)

# *************************************************************************
# ************************************************************************* Meraki Quedstion
# *********************************** introduction ?

# def twopowers(number):
# 	if number==1:
# 		return 1
# 	return 2 * twopowers(number-1)
# index=1
# while(index<10):
# 	print(twopowers(index))
# 	index+=1
# ********************************** simple-series ?
# def pattern(number):
# 	if (number == -1 or number == -2):
# 		return  
# 	else:
# 		pattern(number-3)		
# 		print(number)
# pattern(10)				#output is - 1,1+3=4,4+3=7,7+3=10
# *********************************************** alternative-series-2 ?
# def pattern(number):
# 	if number == 1:
# 		return 10
# 	elif number % 2 == 0:
# 		return pattern(number - 1) + 1
# 	else:
# 		return pattern(number - 1) * 10
# for i in range(1,10):
# 	print(pattern(i))
# *********************************************** factorial number?
# def factorial(number):
# 	if number==1:
# 		return 1
# 	return number * factorial(number - 1)
# n=int(input("Enter number :"))
# print (factorial(n))
# ********************************************** sum-of-a-list ?
# def sum_list(lis):
# 	if len(lis)==1:
# 		return lis[0]
# 	return lis[0] + sum_list(lis[1:])

# print(sum_list([1, 4, 7, 10]))
# ************************************************ palindrome-string ?
# def ifPalindrome(string):
# 	if string == "": # BASE CASE CONDITION
# 		return True
# 	elif len(string) == 1: # BASE CASE CONDITION
# 		return True
# 	elif string[0] == string[len(string)-1]: # RECURSION
# 		return ifPalindrome(string[1:][:-1])
# 	else:
# 		return False
# n=input("Enter name :")
# print(n)
# print(ifPalindrome(n))
# **************************************************** fibonacci-series ?
# def fibo(n):
# 	if n==1:
# 		return 0
# 	if n==2:
# 		return 1
# 	return fibo(n-1)+fibo(n-2)
# n=int(input("Enter no. :"))
# for i in range(1,n+1):
# 	print(fibo(i))
# ************************************************* fibonacci-advanced ?

# def fib(number):
# 	if number == 1:
# 		return 0
# 	elif number == 2:
# 		return 1
# 	else:
# 		return fib(number-1) + fib(number-2)
# def getFibList(number):
# 	fib_list = []
# 	key = 1
# 	while (key < number + 1):
# 		fib_list.append(fib(key))
# 		key += 1
# 	return fib_list
# print(getFibList(10))

# ******************************************** binary-search ?

# def is_present_in_list(number_to_search, list_to_search):
# 	length_of_list = len(list_to_search)
# 	if length_of_list == 0:
# 		return False
# 	if length_of_list == 1:
# 		# list_to_search[0] is the only element left in this list
# 		if number_to_search == list_to_search[0]:
# 			return True
# 	else:
# 		return False
# first_half_of_list = list_to_search[:length_of_list/2]
# second_half_of_list = list_to_search[length_of_list/2:]
# 	return is_present_in_list(number_to_search, first_half_of_list) or is_present_in_list(number_to_search, second_half_of_list)
# print (is_present_in_list(3, [3, 5, 7, 8, 4, 6, 2, 1, 9]))
# print (is_present_in_list(10, [3, 5, 7, 8, 4, 6, 2, 1, 9]))

# ***************************************************** calculate ?

# def operate(num1, operator, num2):
# 	if operator=='+':
# 		return num1 + num2
# 	elif operator=='-':
# 		return num1 - num2
# 	elif operator=='*':
# 		return num1 * num2
# 	else:
# 		return num1 / num20
# num1=int(input("Enter 1st number :"))
# operator=input("Enter operator name :")
# num2=int(input("Enter 2nd number :"))
# print(operate(num1,operator,num2))
#...................................................

# def solve(question_list):
# 	if len(question_list)==1:
# 		return int(question_list[0])
# 	elif len(question_list)==3:
# 		return operate(int(question_list[0]), question_list[1], int(question_list[2]))
# 	else:
# 		return operate(solve(question_list[:-2]), question_list[-2], int(question_list[-1]))

# print(solve(['3', '+', '5', '-', '2', '*', '4', '/', '2', '+', '8', '-', '10', '*', '9', '/', '3']))

# ******************************************************** nested-lists ?

# def flatening(nested):
# 	for i in nested:
# 		if type(i)==type([]):
# 			flatening(i)
# 		else:
# 			flatlist.append(i)
# nestedlist=([1, 2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12])
# flatlist=[]
# flatening(nestedlist)
# print(flatlist)



# ************************************************************* nested-lists-grammar ?

# import random
# rules = [ "[INTEGER]", "[NESTED_LIST, INTEGER]", "[INTEGER, NESTED_LIST]", "NESTED_LIST + NESTED_LIST"]
# def generateRandomNumber():
# 	return random.randrange(1, 20)
# def generateRandomNestedList():
# 	random_rule = random.randrange(4)
# 	if random_rule == 0:
# 		return [generateRandomNumber()]
# 	elif random_rule == 1:
# 		return [generateRandomNestedList(), generateRandomNumber()]
# 	elif random_rule == 2:
# 		return [generateRandomNumber(), generateRandomNestedList()]
# 	elif random_rule == 3:
# 		return generateRandomNestedList() + generateRandomNestedList()
# print (generateRandomNestedList())

#....................................................

#**************************** pattern ?
#.....output ?
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

#........ use loop ?
# k=1
# for i in range(1,5+1):
# 	for j in range(i):
# 		print(k,end=" ")
# 		k=k+1
# 	print()
#....................... recursion ?
# def f(n,i):	# not complite 
# 	if n<i:
# 		return
# 	print("1"*i)
# 	f(n,i+1)
# n=int(input("Enter number :"))
# f(n,1)
