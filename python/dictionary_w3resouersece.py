# ******************************************************* Question 1 
# ........................... Max of three numbers ?
# def max_of_two( x, y ):
#     if x > y:
#         return x
#     return y
# def max_of_three( x, y, z ):
#     return max_of_two( x, max_of_two( y, z ) )
# print(max_of_three(3, 6,8))
# ******************************************************* Question 2 
# .................... sum all the numbers in a list. ?
# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print("sum of digit is =",sum((8, 2, 3, 0, 7)))
# ******************************************************* Question 3
# ................ multiply all the numbers in a list.

# def multiply(numbers):  
#     total = 1
#     for x in numbers:
#         total *= x  
#     return total  
# print("multiply of digit is =",multiply((8, 2, 3, 1, 7)))
# ******************************************************* Question 4
# .......................... reverse a string ?
# def string_reverse(str1):
#     rstr1 = ''
#     index = len(str1)
#     while index > 0:
#         rstr1 += str1[ index - 1 ]
#         index = index - 1
#     return rstr1
# print("reverse =",string_reverse('1234abcd'))
# ******************************************************* Question 5
# ................................  calculate the factorial of a number ?
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))

# ******************************************************* Question 6
# ........................ check whether a number falls in a given range.
# def test_range(n):
#     if n in range(3,9):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(5)

# ******************************************************* Question 7

# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         # else:
#         #    pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])
# a=input("Enter name :")
# string_test(a)

# ******************************************************* Question 8
# ..................... function that takes a list and returns a new list with unique elements of the first list.

# def unique_list(l):
#   x = []
#   for a in l:
#     if a not in x:
#       x.append(a)
#   return x
# print(unique_list([4,7,7,7,2,9,1,5,1,1,1,6,7,5,3])) 

# ******************************************************* Question 10

# def is_even_num(l):
#     enum = []
#     for n in l:
#         if n % 2 == 0:
#             enum.append(n)
#     return enum
# print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# ******************************************************* Question 11
# .............................  a number is perfect or not.

# def perfect_number(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     return sum == n
# print(perfect_number(6))

# ******************************************************* Question 13
# ............................. prints out the first n rows of Pascal's triangle.

# def pascal_triangle(n):
#    trow = [1]
#    y = [0]
#    for x in range(max(n,0)):
#       print(trow)
#       trow=[l+r for l,r in zip(trow+y, y+trow)]
#    return n>=1
# pascal_triangle(6) 

# ******************************************************* Question 16
# .................... print a list where the values are square of numbers between 1 and 30 (both included).

# def printValues():
#     l = list()
#     for i in range(1,21):
#         l.append(i**2)
#     print(l)
        
# printValues()

# ******************************************************* Question 19
# ........................ access a function inside a function.

# def test(a):
#         def add(b):
#                 nonlocal a
#                 a += 1
#                 return a+b
#         return add
# func= test(4)
# print(func(4))

# ******************************************************* ?