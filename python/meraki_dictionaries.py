# Q .************************************************* Introduction to Dictionary ?.

# city_population = {
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
# }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))

#...........................................

# Dict = {
#        'ball' : 'green',
#        'Ball': 'red'
#      }

# print(Dict['ball'])

# x = Dict.get('ball')      # get mothod use output green 
# print(x)

# print(Dict['Ball'])

#............................................

# .........dict() function
# .........create a dictionary using the dict() function.

# student=dict(name= "Ravina",age= 20)
# print(student)

#........................................... dictionary with integer keys:-


# my_dict = {
#     1: 'apple', 
#     2: 'ball'
#     }
# print(my_dict)

#.......................................... dictionary with mixed keys:-

# my_dict = {
#     'name': 'John',
#      1: [2, 4, 3]
#     }

# for i in my_dict.keys():
#     print(i)

#.......................................... Nested Dictionary :-

# Dic= {
#  1: 'NAVGURUKUL',
#  2: 'IN',  
#  3:{
#      'A' : 'WELCOME',
#      'B' : 'To', 
#      'C' : 'DHARAMSALA'
#      }
# }
# print("original dictionary-",Dic)


# Q.*********************************************** Accessing Elements from a Dictionary ?.

# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation'}

# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result)

#................................

# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{
#         'organisation':'navgurukul','place':'dharamsala'
#         }
#     }
# print(person['gender'])

# print(person[4])

# result = person[4]['place']

# print(result)

# print(person["gender"])

# Q.************************************************************ Adding Elements to a Dictionary ?.

# dic= {'Name': 'RAM', 
#     'Age': 17,
#     }
    
# dic['ORGANIZATION'] = "NAV GURUKUL"
# dic['place'] = 'dharamsala'
# print(dic)

#........................................
#......... Add nested dictionary ?.

# dic= {'Name': 'RAM', 
#     'Age': 17,
#     }
# dic['student']={
#         'id':22, 
#         'place':'dharamsala'
#     }
# print(dic)

#...................................
#.............. check keys is in doctionry yes or not ?.

# car ={
#     "brand":  "ford",
#     "model":  "mustang",
#     "year":  1964
# }
# a = input("Enter key name : ")
# if a in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")

# else:
#     print("No, 'model' key dictionary mai nahi hai.")

# Q.*************************************************************** Update Dictionary ?.

# person= {'1': 'RAM', '2': 17,}
# person[3] = 'male'
# print(person) 	

# person.update({4 : "amit"})
# print(person)

# person[5] = "yadav"
# print(person)

#.................................

# details={'Name': 'RAM', 'Age': 17, 'student': {'id': 22, 'place': 'dharamsala'}}
# details['student']['id']=35
# print(details)

#.................................. copy dictionary ?.

# classes ={
#     "room1":  "6th",
#     "room2":  "7th",
#     "room3":  "8th"
#         }
# mydict=classes.copy()
# print("original dictionary - ",classes)
# print("After copy output dictionary :" ,mydict)                

# Q.********************************************** Removing Elements from a Dictionary ?.

#.........Using the pop( ) method we can remove a specified element from the dictionary.

# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)

#..................................

#...The popitem() method removes the last inserted item:

# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# person.popitem()
# print(person)

#....Using the del keyword we can remove a specified element from the dictionary ?.

person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# a = input("Enter key name : ")
# del person[a]
# print(person)

# Q.*************************************************** Iteration ?.

# states_capitals = {
#     'Gujarat' : 'Gandhinagar',
#     'Maharashtra' : 'Mumbai',
#     'Rajasthan' : 'Jaipur',
#     'Bihar' : 'Patna'
#     }
# # for state in states_capitals:
# #         print(state)

# # a = states_capitals.keys()
# # print(a)                      # output tuple in list with string .

# # for x in states_capitals.keys():
# #     print(x)

#...................................................
#.... Iterate through all values ?.

# states_capitals = {
#     'Gujarat' : 'Gandhinagar',
#     'Maharashtra' : 'Mumbai',
#     'Rajasthan' : 'Jaipur',
#     'Bihar' : 'Patna'
#     }
    
# # for state in states_capitals:
# #     print(states_capitals[state])

# for x in states_capitals.values():
#     print(x)

#.......................................................

# details ={
#     "name":  "Bijender",
#     "age":  17,
#     "class":  "10th"
#     }
# for x in details.values():
#     print(x)                  # not complited 


# details ={
#     "age":  "17",
#     "name":  "Bijender",
#     "class":  "10th"
#     }
# for x in details.values():
#     print(x)

#.......................................................

#....How to print keys and values together from a dictionary ?.

# movie ={
#     "name":  "Puli",
#     "hero":  "Vijay",
#     "rating":  7.5
#     }
# for x,y in movie.items():
#     print((x,y))            # not complited 


#........................................................

#.....Dictionary length ?.

# meal ={
#     "monday":  "Chole chawal",
#     "sunday":  "Fried rice",
#     "wednesday":  "dosa"
#     }
# print(len(meal))

#.....................................................
###########################################################

# Q.********************************************** Question.1
#...Write a program such that the below given dictionaries are into a single dictionary and add the values having same key.

# from collections import Counter
# dic1={1:10, 2:20}
# dic2={3:30, 2:40}
# dic3={5:50,6:60}
# d = Counter(dic1) + Counter(dic2) + Counter(dic3)
# print(dict(d))
# # output is - {1: 10, 2: 60, 3: 30, 5: 50, 6: 60}
#........................................................

# dict1={1:10, 2:20}
# dict2={3:30, 2:40}
# dict3={5:50,2:60}
# dict4={}
# for key in dict1:
#     if key in dict2:
#         dict1[key]=dict1[key]+dict2[key]
#     if key in dict3:
#         dict1=dict1[key]+dict3[key]
# dict4={**dict3,**dict2,**dict1}
# import operator 
# asce = dict(sorted(dict4.items(),key=operator.itemgetter(0)))
# print(asce)

# Q.********************************************* Question 2
#..print 'exists' if entered key already exists in the dictionary and print 'not exists' if the entered key does not exist.

# dict={"name":"Raju", "marks":56}
# a=input("Enter name : ")
# if a in dict:
#     print("exist")
# else:
#     print("not exist")

# Q.******************************************** Question 3
#....Ek program likhiye jo ki dictionaries ki values ka sum print kare.

# my_dict = {
#     'data1':100,
#     'data2': -54,
#     'data3': 247
#     } 

# sum=0
# for i in my_dict.values():
#     sum+=i
# print(sum)
#...................OR....OR....OR.....OR......... ?.
# sum=0
# for y in my_dict:
#   sum=sum+my_dict[y]
# print(sum)
#...................OR....OR.....OR......OR........ ?.

# sum=0
# for x,y in my_dict.items():
#   sum=sum+y
# print(sum)

# Q.******************************************** Question ?.

#.... value ka multily ?.

# my_dict = {
#     'data1':1,
#     'data2': 5,
#     'data3': 2
#     } 

# s=1
# for i in my_dict.values():
#     s = s*i
# print(s)

#......................................
# input lekar multiply karna ?.
# size=int(input("how many dictinary : "))
# a = {}
# s=1
# for i in range (size):
# 	k=input("Enter key name :")
# 	v=int(input("Enter value :"))
# 	a.update({k:v})
# 	s = s*v
# print("original dictionary : ",a)
# print("multiply of values :",s)

# Q.******************************************* Question 4
#..remove the first key value pair from a nested dictionary ?.

# Dic= {
#     1: 'NAVGURUKUL',
#     2: 'IN',  
#         3:{    
#          'A' : 'WELCOME',
#          'B' : 'To',
#          'C' : 'DHARAMSALA'
#         }
#     }
# del Dic[3]["A"]
# print(Dic)


# Q.****************************************** Question 5
#..Create a dictionary from 2 lists, where the elements of 1st list are the keys and the elements of the 2nd list are the corresponding values.


# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,] 

# dic = {}
# n = len(list1)
# for i in range(n):
#     dic[list1[i]]=list2[i]
# print(dic)

#.....OR.....OR.....OR....OR..... ?.


# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]

# list3=dict(zip (list1, list2))
# print(list3)


# Q.**************************************** Question 6
#,,,remove duplicate keys.  not complited
# dic={
#     "ball":"red",
#     "bat":4,
#     "wickets":8,
#     "ball":"green",
#     "bat":3
# }

# dic.pop(3,4)
# print(dic)

#................ OR  not complited

# dict1={}
# for i in dic:
#   if i not in dict1:
#     dict1.update({i}) 
# print(dict1)

# Q.**************************************** Question 7
#.........remove dublicate value ?.
# List=[
#     {"first":"1"}, 
#     {"second": "2"}, 
#     {"third": "1"}, 
#     {"four": "5"}, 
#     {"five":"5"}, 
#     {"six":"9"},
#     {"seven":"7"}
# ]
# a=[]
# for x in List:
#     for i in x.values():
#         if i not in a:
#             a.append(i)
# print(a)

# Q.************************************** question 8

#...Take input of name and marks of 10 students and store to a dictionary.
 
# size=int(input('enter size of dictionary :'))
# name_marks={}
# for i in range(size):
#   k=input('enter the key :')
#   v=int(input('enter the values: '))
#   name_marks.update({k:v})
# print(name_marks)
# Q.************************************* Question 9

'''Store the unique letters and their frequency of the letters 
from the word "MISSISSIPPI" to a dictionary, were the letters 
are the keys and their frequencies are the values'''


# s = "MISSISSIPPI"
# s = list(s)
# emp = {}
# for i in s:
#     count = s.count(i)
#     if count>1:
#         for j in range(count-1):
#             emp[i] = count
#             s.remove(i)
#     else:
#         emp[i] = count
# print(emp)

# Q.*************************************** Question 10

#...Count the total number of items from the values of the dictionary which are in the form of a list.

# dict =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# sum=0
# for i in list(dict.values()):
#     if type(i)== list:
#         for j in i:
#             sum+=1
#     else:
#         sum+=1
# print(sum)

# Q.****************************************** Question 11
#..... the top 3 highest values of a given dictionary. 

# my_dict = {
#     'a':50, 
#     'b':58,
#     'c':56,
#     'd':40,
#     'e':100, 
#     'f':20
#     }
# a=[]
# for i in my_dict.values():
#     a.append(i)
#     from heapq import nlargest
#     three_largest=nlargest(3,a)
# print(three_largest)
#.............................. OR
# from collections import Counter
# k = Counter(my_dict)
# high = k.most_common(3)
# print("dictionary 3 highest values:\nkeys:values")
# for i in high:
# 	print(i[1])

# Q.************************************* Question 12

##Write a program to create a dictionary with all numbers from 1 to 15 
##as the keys and their squares as the corresponding values.

# size=int(input('enter size of dic: '))   #solved
# dict1={}
# for i in range(1,size+1):
# 	dict1.update({i:i*i})
# print('dictionary of num and their square',dict1)

# Q.*************************************** Question 13
# ..... the top 3 highest keys of a given dictionary. 
# my_dict = {
#     'a':50, 
#     'b':58,
#     'c':56,
#     'd':40,
#     'e':100, 
#     'f':20
#     }
# from heapq import nlargest
# three_largest=nlargest(3,my_dict,key=my_dict.get)
# print(three_largest)

# Q.************************************* Question 14

#a = {'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}

# print("original dictionary :",a)
# b=sorted(a.items(),key=lambda x:x[1])
# c=dict(b)
# print("Assending order :",c)      # Assending order by value

# print("original dictionary :",a)
# b=sorted(a.items(),key=lambda x:x[1],reverse=True)
# c=dict(b)
# print("Dissending order :",c)           # Dissending order by value

#..................................

# import operator
# a = {'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# print('Original dictionary : ',a)
# sort = dict(sorted(a.items(), key=operator.itemgetter(1)))
# print('Dictionary in ascending order by value : ',sort)
# sorted_d = dict( sorted(a.items(), key=operator.itemgetter(1),reverse=True))
# print('Dictionary in descending order by value : ',sorted_d)


#...................................

# print("original dictionary :",a)
# Ass_order = sorted(a.items())
# print("dictionary in Assending order :",Ass_order)
# Diss_order = sorted(a.items(),reverse=True)
# print("dictionary in Dissending order :",Diss_order)

########################################################

# Q.*********************************************** Code Output ?.
#................................. Question 1
# a = {(1,2):1,(2,3):2}
# print(a[1.2])

# Options :- b is corect 

# A. Key Error

# B. 1

# C. {(2,3):2}

# D. {(1,2):1}


#................................. Question 2

# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])

# Options :-  A is a correct  

# A. Key Error

# B. [1,2]

# C. {‘a’:1,’b’:2}

# D. (1,2)

#................................. Question 3

# fruit = {}

# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
        
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')

# print (len(fruit))
# print(fruit)

##output- 3
##        {'Apple': 2, 'Banana': 1, 'apple': 1}


#................................. Question 4

# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print (len(Details["Student"])) 

## output :- 1

#................................. Question 5

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]

# print (sum)
# print(my_dict)

## output:-30
##         {(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12}

#................................. Question 6

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))

## output ;- typeerror  unhashable type

#................................. Question 7

#rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec

# rec = {
#     "Name" : "Python", 
#     "Age":"20", 
#     "Addr" : "NJ", 
#     "Country" : "USA"
#     }
# id2 = id(rec)
# print(id1 == id2)

## output:-True

# Q.************************************** Debug Code ?.
#.............................. Question 1

# details={
#     "name":"Shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org",
#     }

# print(details["name"])
# print(details["email"])
# print(details["age"])

#.............................. Question 2

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+1        #............sum=sum+i is correct 
# print(sum)

#.............................. Question 3

# c=dict()
# for i in range(1,16):
#     c.update({i:i*i})
# print(c)

## me c=(i*i) with c.update({i:i*i})

#.............................. Question 4

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#   c.update(i)
# print(c)

## me update update(i) with c.update(i) this was bug in this questions

#.........................................

##  2nd method   ## 3rd method using {*,*}

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}

# s.update(a)
# print(s)

# c={*s,*a}
# print(c)

############################################################################
#.... value ka multily ?.

# my_dict = {
#     'data1':1,
#     'data2': 5,
#     'data3': 2
#     } 

# s=1
# for i in my_dict.values():
#     s = s*i
# print(s)

#......................................
# input lekar multiply karna ?.

# size=int(input("how many dictinary : "))
# a = {}
# s=1
# for i in range (size):
# 	k=input("Enter key name :")
# 	v=int(input("Enter value :"))
# 	a.update({k:v})
# 	s = s*v
# print("original dictionary : ",a,"\nmultiply of values :",s)

###################################################################

# Roman numer ?.

# def roman_numbers(num):
# 	if num>1000:
# 		print("enter number, less than 1000 : ")
# 	value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
# 	symbel = ["M","CM","D","CD","C","XC","L","LX","X","IX","V","IV","I"]

# 	roman = ""
# 	i=0
# 	while num > 0:
# 		div = num//value[i]
# 		num = num%value[i]
# 		while div:
# 			roman+=symbel[i]
# 			div = div-1
# 		i += 1
# 	return roman
# num = int(input("Enter number :"))
# print("roman number of",num,"is",roman_numbers(num))

#..............................................

#roman number 1 too 1000

# number= [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
# roman = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
# 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
# given_number = int(input("Enter a number: "))
# if given_number<=1000:
#     for i in number:
#         if given_number != 0:
#             q= given_number//i
#             given_number = given_number%i
#             if q != 0:
#                 for y in range(q):
#                     print(roman[i], end="")
# else:
#     print("NO more than 1000")

#########################################################

# my_dict = {}
# size = int(input("Enter number dictionary :"))
# for i in range(size):
# 	k = int(input("Enter key name :"))
# 	v = input("Enter key value : ")
# 	my_dict.update({k:v})
# print(my_dict)

##################################

# roman number ?.
# def roman_numbers(num):
#   if num>1000:
#     print("enter number, less than 1000 : ")
#   value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
#   symbel = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

#   roman = ""
#   i=0
#   while num > 0:
#     div = num//value[i]
#     num = num%value[i]
#     while div:
#       roman+=symbel[i]
#       div = div-1
#     i += 1
#   return roman
# num = int(input("Enter number :"))
# print("roman number of",num,"is",roman_numbers(num))
0#...........................................................

# value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
# symbel = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
# num = int(input("Enter number :"))
# roman = ""
# i=0
# while num > 0:
#   div = num//value[i]
#   num = num%value[i]
#   while div:
#     roman+=symbel[i]
#     div = div-1
#   i += 1
# print("roman number is = ",roman)

#..............................................
#roman number 1 too 1000

# number= [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
# roman = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
# 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
# given_number = int(input("Enter a number: "))
# if given_number<=1000:
#     for i in number:
#         if given_number != 0:
#             q= given_number//i
#             given_number = given_number%i
#             if q != 0:
#                 for y in range(q):
#                     print(roman[i], end="")
# else:
#     print("NO more than 1000")


###########################################################





#.... check value how many keys in dictionary

# d = {"a":(1,2,3,4),"b":(6,7,8,2),"c":(9,10,2,3)}
# dic = []
# for i in d:
# 	for j in d[i]:
# 		if j not in dic:
# 			dic.append(j)
# dic1 = {}
# for i in dic:
# 	lis = []
# 	for k in d:
# 		if i in d[k]:
# 			lis.append(k)
# 	dic1[i]=lis
# print(dic1)

