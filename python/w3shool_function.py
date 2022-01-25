# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# ######################################################
# No argument no return(NANR) methhod ?.

# def add():
#   a = int(input("Enter no 1st : "))
#   b = int(input("Enter no 2nd : "))
#   c = a+b
#   print("sum =",c)
# add()
# #.............................................
# No argument with return(NAWR) method ?.

# def add():
#   a = int(input("Enter 1st No. :"))
#   b = int(input("Enter 2nd No. :"))
#   c=a+b
#   return c
# x = add()
# print("Addition=",x)
# ................................................
# with argument no return(WANR) method ?.

# def add(a,b):
#   c = a+b 
#   print("additon=",c)
# x=int(input("Enter 1st no. :"))
# y=int(input("Enter 2nd no. :"))
# add(x,y)  
# ................................................
# with argument with return (WAWR) method ?.

# def add(a,b):
#   c=a+b
#   return c
# a=int(input("Enter No. 1st :"))
# b=int(input("Enter No. 2nd :"))
# z=add(a,b)
# print("Addition =",z)
# .................................................

# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# a=my_function(3)
# print(a)

# ......................
# nanr
# def my_function():
#   a=int(input("Enter 1st no. :"))
#   b=int(input("Enter 2nd no. :"))
#   c=a*b
#   print("Multiply of ",a, "*",b,"=",c)
# my_function()
# ..................
# wanr
# def my_function(a,b):
#   c= a*b
#   print("Multiply of",a,"*",b,"=",c)
# x=int(input("Enter 1st no. :"))
# y=int(input("Enter 2nd no. :"))
# my_function(x,y)
#............................ 

# def multiply(numbers):  
#     total = 1
#     for x in numbers:
#         total *= x  
#     return total  
# print(multiply((8, 2, 3, 1, 7)))

# ..............................
# NAWR

# def my_function():
#   c= a*b
#   return c
# a=int(input("Enter 1st no. :"))
# b=int(input("Enter 2nd no. :"))
# d= my_function()
# print("Multiply of",a,"*",b,"=",d)
# .............................
# WAWR

# def my_function(a,b):
#   c= a*b
#   return c
# a=int(input("Enter 1st no. :"))
# b=int(input("Enter 2nd no. :"))
# d= my_function(a,b)
# print("Multiply of",a,"*",b,"=",d)
# ................................................
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)
# ###################################################################

# ............................................ creating a function ?

# def my_function():
#   print("Hello from a function")

# ............................................ calling a function ?

# def my_function():
#   print("Hello from a function")
# my_function()

# .................................................. Argument ?

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# ..................................................  number of argujment ?

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# ................................................. Arbitrary arguments ?

# ......If the number of arguments is unknown, add a * before the parameter name:

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")          

# ................................................... keyword arguments ?

# ...You can also send arguments with the key = value syntax.
# ...This way the order of the arguments does not matter.

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")\

# .................................................... Arbitrary Keyword Arguments, **kwargs

# ...If the number of keyword arguments is unknown, add a double ** before the parameter name:

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# ................................................... Passing a List as an Argument 
# ..... You can send any data types of argument to a function (string, number, list, dictionary etc.)

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# ###################################################

# def abcd ():
# 	print("amit")
# print("kumar")
# print("yadav")

# def abcd ():
# 	print("amit")
# 	print("papa")
# print("kumar")
# abcd()
# print("yadav")

# def abcd (number):
# 	print(f"abcd{number}")
# abcd("15")

# ######################################################
# ######################################################
# ............................... Function ?
# ..................... Basic function ?

# print ("NavGurukul")

# def say_hello():
#     print ("Hello!")
#     print ("Aap kaise ho?")

# say_hello()
# print ("Python is awesome")
# say_hello()
# print ("Hello…")
# say_hello()

# .........................................

# names_list = ["Fiza", "Shivam", "Imtiyaz", "Deepanshu", "Rahman"]
# print (len(names_list))

# ........................................

# def definition_say_hello():
#     print ("NavGurukul")
#     print ("NavGurukul mei humein apni learning ki responsibility leni padti hai.")
# definition_say_hello()
# print ("NavGurukul mei hum sab logo ko ek tarah se treat karte hai.")
# definition_say_hello()

# ...........................................

# def function_say_bye():
# 	print ("Aapko mil ke maza aaya. ")
# 	print ("Bye bye")
# function_say_bye()
# function_say_bye()
# print ("Python ka istamaal bahot jagah hota hai.")
# function_say_bye()
# function_say_bye()

# ........................................... Function call ko samjhe ?
# def definition_hello_again():
#     print ("Firse Hello :)")
#     print ("Aap kaise ho?")
# definition_hello_again()

# ##############################################
# ........... Globle and local variable ?
# l = 10
# def function1(n):
#   l = 5
#   m = 8
#   print(l,m)
#   print(n,"yes i'm printed")
# function1("This is me ")
# # print(m)    # m is not define
# print(l) 
# ........................................

# l = 10
# def function1(n):
#   #l = 5
#   m = 8
#   global l
#   l = l + 45
#   print(l,m)
#   print(n,"i have")
# function1("this is my pen") 

# l = 10
# def function1(n):
#   #l = 5
#   m = 8
#   l = l + 45
#   print(l,m)
#   print(n,"i have")
# function1("this is my pen") 

# ...........................................
# x=89
# def amit():
#   x=20
#   def yadav():
#     global x
#     x=88
#   print("Before calling yadav",x)
#   yadav()
#   print("After calling yadav",x)
# amit()
# print(x)



# ###############################################

# ..................... question 1

# def ask_question():
# 	print("who is the founder of facebook ?\na)Mark Zuckerberg\nb)Bill Gates\nc)Steve Jobs\nd)Larry Page")
# ask_question()
# ask_question()
# ask_question()
# ask_question()
# ask_question()

# def ask_question():
#   i=1
#   while i<=100:
#     print("""Who is the founder of Facebook?

# - Mark Zuckerberg
# - Bill Gates
# - Steve Jobs
# - Larry Page""")
#     i +=1
# ask_question()
# ******************************************** Pre-defined Functions Question ?

# ... Q1 . Aapko max function ka use krke di hue list me se sbse bada value print krvani hai.

# numbers = [3, 5, 7, 34, 2, 89, 2, 5]
# print(max(numbers))

# ... Q2. Aapko sum function ka use krke di hue list ke element ka sum print krvana hai.

# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))

# ... Q3. Aapko sort function ka use kr ke di hue list ko sort krna hai.

# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# unorder_list.sort()
# print(unorder_list)

# ... Q4. reverse function ka use kr ke aapko di hue list ka revrse print krna hai.

# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# reverse_list.reverse()
# print(reverse_list)

# ... Q5. Aapko min function ka use krke di hue list me se sbse chhoti value print krvani hai.

# list = [8, 6, 4, 8, 4, 50, 2, 7]
# print(min(list))

# ********************************************************** Debug the Code ?
# .................. Question 1 
# def sum():
#     print(12+13)
# sum()

# .................. Question 2

# def welcome():
#     print("Welcome to function")
# welcome()

# .................. Question 3

# def isEven():
#   a = int(input("Enter number : "))
#   if(a%2==0):
#     print("Even Number")
#   else:
#     print("Old Number")
# isEven()

# *************************************** Function Arguments ?

# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print (max(numbers_list))

# ...................................................

# a=[1,2,3,4,5,6]
# print(len(a))

# .......................................

# def say_hello(name):
#     print ("Hello ", name)
#     print ("Aap kaise ho?")
# say_hello("Aatif")

# ............................. Multiple Function Arguments ?

# def add_numbers(number1, number2):
#     print ("Main do numbers ko add karunga.")
#     print (number1 + number2)
# add_numbers(120, 50)
# num_x = 134
# name = "Rinki"
# add_numbers(num_x, name)

# ......................................

# def say_hello_language(name, language):
#     if language == "hindi":
#         print ("Namaste ", name)
#         print ("Aap kaise ho?")
#     elif language == "punjabi":
#         print ("Sat sri akaal ", name)
#         print ("Tuhada ki haal hai?")
#     else:
#         print ("Hello ", name)
#         print ("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# say_hello_language("Kavay", "hindi")

# ................................................

# def say_hello_people(name_x, name_y, name_z, name_a):
#     print ("Namaste ", name_x) # hindi mein
#     print ("Alah hafiz ", name_y) # urdu mein
#     print ("Bonjour ", name_z) # french mein
#     print ("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")

# ............................................ Python Arbitrary Arguments ?

# def icecream(*flavours):
#  for flavour in flavours:
#     print("i love"+flavour)
#     #print("i love",flavour)
# icecream("chocolate", "butterscotch","vanilla","strawberry")

# ........................................... Default parameter value ?

# def attendance(name,status="absent"):
#     print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh")

# ********************************************* Debug the Code ?
# .............. Question 1
# def greet(*names):      #.....bug- def greet(names)
#     for name in names:
#         print("Welcome", name)
# greet("Rinki", "Vishal", "Kartik", "Bijender")

# .............. Question 2

# def info(name, age ):   # bug...def info(name, age= ):
#    print(name + " is " + age + " years old")

# info("Sonu","25")  #  info("Sonu")
# info("Sana", "17")
# info("Umesh", "18") 

# .............. Question 3

# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
# studentDetails("Nilam","loop","Amit")

# *************************************** Question 2

# def function_print_lines():
#   print("Mera naam Rishabh hai.")
#   print("Main NavGurukul ka co-Founder hun." )
# function_print_lines()

# *************************************** Question 3
# .....Part 1
# def students(list_of_students):

# .....Part 2
# def isGreaterThen20(b,a=20):
#   c= a+b
#   print("Addition of two digit is =",c)
# isGreaterThen20(10)

# *************************************** Question 4
# ..... part 1
# def add_numbers(num1,num2):
#   num3=num1+num2
#   print("Addition of two number is =",num3)
# num1=56
# num2=12
# add_numbers(num1,num2)

# ...... part 2

# def add_numbers_list(a,b):
#   sum = 0
#   for i in range(len(a)):
#     sum = a[i]+b[i]
#     print("Addition of two number is =",sum)
# a=[50, 60, 10]
# b=[10, 20, 13]
# add_numbers_list(a,b)
# .................................
# a=[50, 60, 10]
# b=[10, 20, 13]
# sum =0 
# for i in range(len(a)):
#   sum = a[i] + b[i]
#   print(sum)

# ******************************************* Question 5
# ...... part 1
# a=[2, 6, 18, 10, 3, 75]
# b=[6, 19, 24, 12, 3, 87]
# def check_numbers(a,b):     
#   for i in range(len(a)):
#     if a[i]%2==0 and b[i]%2==0:
#       print("Dono Even number hai ")
#     else:
#       print("Dono Even number nahi hai")
# check_numbers(a,b)

# *********************************************** Return Values ?
# ............ How to return a value from a function?

# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum

# sum1 = add_numbers(20, 40)
# print (sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print (sum2)
# print (sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print (number_a)

# ........................................................
# .... Hum same function ko return value ke bina likhte hain ?

# def add_numbers_print(number_x, number_y):
#     number_sum = number_x + number_y
#     print (number_sum)
# sum4 = add_numbers_print(4, 5)
# print (sum4)
# print (type(sum4))

# ..........................................................

# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print ("Hello from NavGurukul ;)")
#     return number_sum
#     number_sum = number_x + number_x
#     print ("Kya main yahan tak pahunchunga?")
#     return number_sum

# sum6 = add_numbers_more(100, 20)

# ......................................................

# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"

#     print ("Kya main print ho payungi? :-(")

# mon_menu = menu("monday")
# print (mon_menu)
# tues_menu = menu("tuesday")
# print (tues_menu)
# fri_menu = menu("friday")
# print (fri_menu)

# ..........................................................

# def menu(day):
#     if day == "monday":
#         food = "Butter Chicken"
#     elif day == "tuesday":
#         food = "Mutton Chaap"
#     else:
#         food = "Chole Bhature"
#     print ("Kya main print ho payungi? :-(")
#     return food
#     print ("Lekin main toh pakka nahi print hounga :'(")
# print(menu("monday"))

# *************************************************************** Question 6

# def calculator(number_x, number_y):
#   number_sum = number_x + number_y
#   return number_sum
# a=int(input("Enter No. 1st :"))
# b=int(input("Enter No. 2nd :"))
# sum1 = calculator(a,b)
# print ("sum of two number if =",sum1)

# ................................................ part 1
# def calculator(number_x,number_y,operation):
#   if operation=="add":
#     print(number_x+number_y)
#   elif operation=="subtract":
#     print(number_x-number_y)
#   elif operation=="multiply":
#     print(number_x*number_y)
#   elif operation=="divide":
#     print(number_x/number_y)
# a=int(input("Enter No. 1st :"))
# operation=input("Enter operation name :")
# b=int(input("Enter No. 2nd :"))
# # print ("sum of two number if =",sum1)
# calculator(a,b,operation)

# ................................................ part 2


# def calculator(x,y):
#   number_1 = x+y

#   print("add=",number_1)
# calculator(20,24)
# def calculator(x,y):
#   number_2=x*y
#   print("multipy=",number_2)
# calculator(50,60)

# def calculator(x,y):
#   number_3=x/y
#   print("divide=",number_3)
# calculator(120,80)

# def calculator(x,y):
#   number_4=x-y
#   print("subtraction =",number_4)
# calculator(90,23)

# ...................................................

# a=int(input("Enter 1st no, :"))
# b=int(input("Enter 2nd no, :"))
# def calculator(x,y):
#   number_1 = x+y
#   return number_1
# add_result=calculator(a,b)

# print("add_result =",add_result)

# def calculator(x,y):
#   number_2=x*y
#   return number_2
# multiply_result=calculator(a,b)
# print("multiply_result =",multiply_result)

# def calculator(x,y):
#   number_3=x/y
#   return number_3
# divide_result=calculator(a,b)
# print("divide_result =",divide_result)

# def calculator(x,y):
#   number_4=x-y
#   return number_4
# subtract_result=calculator(a,b)
# print("subtract_result =",subtract_result)

# .................................................... part 3
# ... without append method.
# def list_change(a,b):
#   s=0
#   for i in range(len(a)):
#     s=a[i]*b[i]
#     b[i]=s
#   print(b)
# a=[5, 10, 50, 20]
# b=[2, 20, 3, 5]
# list_change(a,b)
# ............................. using append method .
# def list_change(a,b):
#   s=0
#   p=[]
#   for i in range(len(a)):
#     s=a[i]*b[i]
#     p.append(s)
#   print(p)
# a=[5, 10, 50, 20]
# b=[2, 20, 3, 5]
# list_change(a,b)

# ************************************************* Inner Function ?

# def f1():
#    s = "I Love Navgurukul"
#    def f2():
#        print(s)
#    f2()
# f1()
# ........................................

# def first_function():
#     s = 'I love India'
#     def second_function():
#         print(s)     
#     second_function()
# first_function()
# .........................................

# def first_function():
#     s = 'I love India'
#     def second_function():
#         s = "MY NAME IS JACK"
#         print(s)     
#     second_function()
#     print(s)    
# first_function()

# def first_function():
#     s = 'I love India'
#     def second_function():
#         b = "MY NAME IS JACK"
#         print(b)     
#     second_function()
#     print(s)    
# first_function()

# ********************************************************* Question 1 
# a=int(input("Enter eligible age :"))
# def eligible_for_vote():
#   if a<18:
#     print("not eligible")
#   elif a>=18:
#     print("you are eligible")
# #a=int(input("Enter eligible age :"))
# eligible_for_vote()

# ******************************************************* Question 2
# .... check perfect yes or not ? 
# def perfect():
#   s=0
#   n=int(input("Enter number :"))
#   for k in range(1,n):
#     if n%k==0:
#       s=s+k
#   if s==n:
#     print(n,"is perfect number")
#   else:
#     print(n,"not perfect number")
# perfect()
# ......................................... perfect number 1 to 1000 ?

# def perfect():
#   for inp in range(1,1001):
#     ls=[]
#     for i in range(1,inp):
#       if inp%i==0:
#         ls.append(i)
#     sum=0
#     for i in ls:
#       sum=sum+i
#     if sum==inp:
#       print(inp)
# perfect()

# ******************************************************* Question 3

# def sum_of_three():
#   i=1
#   sum=0
#   while (i<=a):
#     b=int(input("enter number: "))
#     i+=1
#     sum=sum+b
#   print("total-",sum,"\nAverage of digit =",sum/a)
# a=int(input("How to take print number:-: "))
# sum_of_three()


# def amol():
#   sum=0
#   for i in range(a):
#     d=int(input('enter number '))
#     sum=sum+d
#   print("\nTotal sum = ",sum,"\nAverage of digit = ",sum/a)
# a=int(input('enter number how many numbers you have :'))
# amol()


# ******************************************************* Question 4
# def showNumbers():
#   n=int(input("Enter number :"))
#   a=0
#   while a<n:
#     a+=1
#     if a%2==0:
#       print(a,"even")
#     else:
#       print(a,"odd")
# showNumbers()

# ********************************************************** Question 5

# def function_likhiye(): 
#   s=1
#   for i in range(1,a):
#     if i%3==0:
#       # print(i)
#       s=s+i
#     elif i%5==0:
#       # print(i)
#       s=s+i
#   s = s+i
#   print("Total sum =",s)
# a=int(input("Enter number :"))
# function_likhiye()

# ********************************************************** Question 6

# def check_speed(km):
# 	count=0
# 	if speed<70:
# 		print("ok")
# 	elif speed>70 and speed <=75:
# 		count +=1
# 	elif speed>75 and speed<=80:
# 		count +=2
# 	elif speed>80 and speed <=85:
# 		count +=3
# 	elif speed>85 and speed<=90:
# 		count +=4
# 	elif speed>90 and speed<=95:
# 		count +=5
# 	elif speed>95 and speed <=100:
# 		count +=6
# 	elif speed>100 and speed<=105:
# 		count +=7
# 	elif speed>105 and speed <=110:
# 		count +=8
# 	elif speed>110 and speed<=115:
# 		count +=9
# 	elif speed>115 and speed <=120:
# 		count +=10
# 	elif speed>120 and speed<=125:
# 		count +=11
# 	elif speed>125 and speed <=130:
# 		count += 12
# 	elif speed>130 and speed<=135:
# 		count +=13
# 		print("License suspended")
# 	print("point :",count)

# speed=int(input("Enter speed :"))
# check_speed(speed)




# ********************************************************** Question 7

# def function_name(name1,name2):
#   if len(name1)==len(name2):
#     print("name1 and name2 both same = ",name1,"\nname1 and name2 both same = ",name2)
#   else:
#     if len(name1)>len(name2):
#       print("greater name1 =",name1)
#     else:
#       print("greater name2 = ",name2)
# name1=input("Enter 1st name :")
# name2=input("Enter 2nd name :")
# function_name(name1,name2)

# ********************************************************** Question 8

# def squar():
#   size=int(input('enter size of dic: '))   
#   dict1={}
#   for i in range(1,size+1):
#     dict1.update({i:i*i})
#   print('dictionary of num and their square',dict1)
# squar()
#....
# def printValues():
#     l = list()
#     for i in range(1,21):
#         l.append(i**2)
#     print(l)
        
# printValues()


# ********************************************************** Code Output ?
# ***************************************** Question 1

# def employee(name,salary=20000):
#         print(name,"your salary is:-",salary)

# employee("kartik",30000)
# employee("deepak")

# ..... output is - kartik your salary is:- 30000
#                   deepak your salary is:- 20000
# ***************************************** Question 2
# def primeorNot(num):     
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")

#     else:
#            print(num,"is not a prime number")
# primeorNot(406)

# ...... output is - 406 is not a prime number
#                    2 times 203 is 406

# ***************************************** Question 3

# def greet(*names):
#     for name in names:
#                print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")

# ..... output is - 
# Hello sonu
# Hello kartik
# Hello umesh
# Hello bijender

# ***************************************** Question 4

# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#     return sum
# print(sumofdigits(123))

# .... output is - 6.666666666666668

# ***************************************** Question 5

# def  meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :
#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "aloo rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner"    :
#             return "veg-chapati"
#         else :
#             return "time not found"
            
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))

# ...... output is - dal rice
#                    chhole bhature

# ************************************************** Debug the Code ?
# **************************************** Question 1
# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# # sum(4,5)      # bug 
# calculate_sum(4,5)    # debug 

# **************************************** Question 2

# function multi(a,b):    # Bug 
# def multi(a,b):           # debug 
#     multiply=a*b
#     return multiply
# print(multi(3,4))

# **************************************** Question 3

# Def Avg(number1,number2,number3):   # bug
#     avg=number1+number2+number3/3
#     print(sum)
# Avg(1,3,2)

# def Avg(number1,number2,number3):   # debug 
#     avg1=number1+number2+number3/3
#     print(avg1)
# Avg(1,3,2)

# **************************************** Question 4

# def voter(age):       #............ BUG 
# if age < 18:
#     print("eligible")
# else:
#     print("not eligible")
#     voter(20)

# def voter(age):       #........... Debug 
#   if age < 18:
#       print("eligible")
#   else:
#       print("not eligible")
# voter(20)

# **************************************** Question 5

# def distance(kms):            # Bug 
#         if kms < 20:
#             print("close")
#         elif kms < 50:
#             print(median)
#         else:
#             Print(far)
#     distance(20,30)

# def distance(kms):          # debug
#         if kms < 20:
#             print("close")
#         elif kms < 50:
#             print("median")
#         else:
#             print("far")
# a=int(input("Enter number :"))
# distance(a)




# inp=int(input("enter num:"))
# def perfect():
#   ls=[]
#   for inp in (1,1001):
  
#     for i in range(1,inp):
#       if inp%i==0:
#         ls.append(i)
#         # print(ls)
#   sum=0
#   for i in ls:
#     sum=sum+i
#   # print(sum)
#   if sum==inp:

#     print(inp)
#   else:
#     print("no")
# perfect()
# # def fun(1000):


# def calc(a,b):
# 	sum=a+b
# 	sub=a-b
# 	mul=a*b
# 	div=a/b
# 	return sum,sub,mul,div
# t=calc(100,50)
# print("The um of=",t)

# def amol(a,b):
# 	c=a+b
# 	print("addition of two number is=",c)
# 	return c
# a=int(input("Enter 1st name :"))
# b=int(input("Enter 2nd name :"))
# print(amol(a,b))