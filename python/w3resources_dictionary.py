# Q.****************************Question 1
#......Write a Python script to sort (ascending and descending) a dictionary by value.

# import operator
#d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print('Original dictionary : ',d)
# sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
# print('Dictionary in ascending order by value : ',sorted_d)
# sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
# print('Dictionary in descending order by value : ',sorted_d)

#..................................

# def sort_dict_by_value(d, reverse = False):
#   return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
# print("Original dictionary elements:")
# colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}
# print(colors)
# print("\nSort (ascending) the said dictionary elements by value:")
# print(sort_dict_by_value(colors))
# print("\nSort (descending) the said dictionary elements by value:")
# print(sort_dict_by_value(colors, True))

# Q.*********************************************************** Qurstion 2
# ...... Write a Python program to add a key to a dictionary.

# d = {0:10, 1:20}
# print("Original dictionry =",d)
# d.update({2:30})
# print("Add item in dictionry =",d)	# Expected Result : {0: 10, 1: 20, 2: 30}

# #....OR....OR.......OR....... ?.

# d[3]=20
# print("Add item in dictionry =",d)

# Q.*************************************************************** Question 3
#...... Write a Python program to concatenate following dictionaries to create a new one.

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# # code - Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}  
# dic4 = {}
# for d in (dic1, dic2, dic3): dic4.update(d)
# print(dic4)

# Q.********************************************************************* Question 4
#... check whether a given key already exists in a dictionary.

# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_present(x):
#   if x in d:
#       print('Key is present in the dictionary')
#   else:
#       print('Key is not present in the dictionary')
# a = int(input("Enter your check number in a dictionary :"))
# is_key_present(a)

#....................................... ?.

# def key_in_dict(d, key):
#   return (key in d) 
# students = {
#   'Theodore': 19,
#   'Roxanne': 22,
#   'Mathew': 21,
#   'Betty': 20
# }
# print("\nOriginal dictionary elements:")
# print(students)
# print(key_in_dict(students, 'Roxanne'))
# print(key_in_dict(students, 'Gina'))

# Q.************************************************************************  Question 5
#..... Write a Python program to iterate over dictionaries using for loops.

# d = {'x': 10, 'y': 20, 'z': 30} 
# for dict_key, dict_value in d.items():
#     print(dict_key,'=',dict_value)

#....................................... ?.
# ...  iterate over dictionaries using for loops.

# d = {'Red': 1, 'Green': 2, 'Blue': 3} 
# for color_key, value in d.items():
#      print(color_key, 'corresponds to ', d[color_key]) 


# Q.******************************************************************************Qurstion  6
#... Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# n=int(input("Input a number "))
# d = dict()
# for x in range(1,n+1):
#     d[x]=x*x

# print(d)

#......OR.......OR........OR.......OR...... ?.

# d=dict()
# for x in range(1,16):
#     d[x]=x**2
# print(d) 

# Q.**************************************************************** Qurstion 8
# .... merge two dictionaries in one dictionary ?.

# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d = d1.copy()
# d.update(d2)
# print(d)

# Q.************************************************************** Qurstion 10
#.... sum all the items in a dictionary from value .

# my_dict = {'data1':100,'data2':-54,'data3':247}
# print(sum(my_dict.values()))

# s = 0
# for i in my_dict.values():
# 	s+=i
# print(s)

# Q.************************************************************************Qurstion 11

#.... multiply all the items in a dictionary.

# my_dict = {'data1':10,'data2':5,'data3':2}
# result=1
# for i in my_dict:    
#     result=result * my_dict[i]
# print(result)

# Q.*************************************************************Qurstion 12
#.... remove a key from a dictionary.

# myDict = {'a':1,'b':2,'c':3,'d':4}
# print("original dictionary =",myDict)
# if "a" in myDict:
# 	remove = input("remove dictionary in keys : ")
# 	del myDict[remove]
# print("After remove dictionary =",myDict)

# Q.*************************************************************************Qurstion 13
#.... map two lists into a dictionary.

# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# color_dictionary = dict(zip(keys, values))
# print(color_dictionary)

# Q.**************************************************************************Qurstion 14
#........ sort a given dictionary by key

# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}

# for key in sorted(color_dict):
#     print("%s: %s" % (key, color_dict[key]))

#................................................

# def sort_dict_by_key(d, reverse = False):
#   return dict(sorted(d.items(), reverse = reverse))
# students = { 'name1': 'Theodore', 'name2': 'Mathew', 'name4': 'Roxanne', 'name3': 'David' }
# print("Original dictionary:",students)
# print("\nSort the said dictionary by key (Ascending order):")
# print(sort_dict_by_key(students))
# print("\nSort the said dictionary by key (Descending order):")
# print(sort_dict_by_key(students, True))

# Q.*******************************************************************************Qurstion 15
#....... maximum and minimum value in a dictionary.

# my_dict = {'x':500, 'y':5874, 'z': 560}

# key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
# key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

# print('Maximum Value: ',my_dict[key_max])
# print('Minimum Value: ',my_dict[key_min])

# q.*****************************************************************************Qurstion 17

#....... remove duplicates from Dictionary.

# student_data = {'id1': 
#    {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id2': 
#   {'name': ['David'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id3': 
#     {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id4': 
#    {'name': ['Surya'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
# }

# result = {}

# for key,value in student_data.items():
#     if value not in result.values():
#         result[key] = value

# print(result)

# Q.***********************************************************************Qurstion 18
#............... check a dictionary is empty or not.

# my_dict = {}

# if not bool(my_dict):
#     print("Dictionary is empty")

# Q.***********************************************************************Qurstion 19
#................  combine two dictionary adding values for common keys.

# from collections import Counter
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d = Counter(d1) + Counter(d2)
# print(dict(d))
#..............................................

# from collections import Counter
# dic1={1:10, 2:20}
# dic2={3:30, 2:40}
# dic3={5:50,6:60}
# d = Counter(dic1) + Counter(dic2) + Counter(dic3)
# print(dict(d))
# # output is - {1: 10, 2: 60, 3: 30, 5: 50, 6: 60}

# Q.***********************************************************************Qurstion 20
#..... print all unique values in a dictionary.

# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print("Original List: ",L)
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)

# Q.***********************************************************************Qurstion 22
#.........  find the highest 3 values of corresponding keys in a dictionary.

# from heapq import nlargest
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
# three_largest = nlargest(3, my_dict, key=my_dict.get)
# print(three_largest) 

#....................................

# from heapq import nlargest
# from operator import itemgetter
# items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# for name, value in nlargest(3, items.items(), key=itemgetter(1)):
#     print(name, value)


# Q.***********************************************************************Qurstion 23
#........ combine values in python list of dictionaries.

# from collections import Counter
# item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# result = Counter()
# for d in item_list:
#     result[d['item']] += d['amount']
# print(dict(result))

# Q.***********************************************************************Qurstion 24
#...... create a dictionary from a string.
#......Note: Track the count of the letters from the string.

# from collections import defaultdict, Counter
# str1 = 'w3resource' 
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)

# Q.***********************************************************************Qurstion 25
#..... print a dictionary in table format.

# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
#     print(*row)

# Q.***********************************************************************Qurstion 26
#.....count the values associated with key in a dictionary.

# student = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# print(sum(d['id'] for d in student))
# print(sum(d['success'] for d in student))

# Q.***********************************************************************Qurstion 27
#....convert a list into a nested dictionary of keys.

# num_list = [1, 2, 3, 4]
# new_dict = current = {}
# for name in num_list:
#     current[name] = {}
#     current = current[name]
# print(new_dict)

# Q.***********************************************************************Qurstion 28
#....  sort a list alphabetically in a dictionary.

# num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# sorted_dict = {x: sorted(y) for x, y in num.items()}
# print(sorted_dict)

# Q.***********************************************************************Qurstion 31
#..... get the key, value and item in a dictionary.

# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("key  value  count")
# for count, (key, value) in enumerate(dict_num.items(), 1):
#     print(key,'   ',value,'    ', count)

# Q.***********************************************************************Qurstion 32
#.... print a dictionary line by line.

# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# for a in students:
#     print(a)
#     for b in students[a]:
#         print (b,':',students[a][b])

# Q.***********************************************************************Qurstion 33
#.... check multiple keys exists in a dictionary.

# student = {
#   'name': 'Alex',
#   'class': 'V',
#   'roll_id': '2'
# }
# print(student.keys() >= {'class', 'name'})
# print(student.keys() >= {'name', 'Alex'})
# print(student.keys() >= {'roll_id', 'name'})

# Q.***********************************************************************Qurstion 34
#.....count number of items in a dictionary value that is a list.

# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# ctr = sum(map(len, dict.values()))
# print(ctr)

# Q.********************************************************************** 35
#...... sort Counter by value.
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# code - 
# from collections import Counter
# x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
# print(x.most_common())		# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

# Q.********************************************************* 36
#........ create a dictionary from two lists without losing duplicate values.

# from collections import defaultdict
# class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# id_list = [1, 2, 2, 3]
# temp = defaultdict(set)
# for c, i in zip(class_list, id_list):
#     temp[c].add(i)
# print(temp)

# Q.*********************************************************** 38
#........... match key values in two dictionaries ?.

# x = {'key1': 1, 'key2': 3, 'key3': 2}
# y = {'key1': 1, 'key2': 2}
# for (key, value) in set(x.items()) & set(y.items()):
#     print('%s: %s is present in both x and y' % (key, value))

# Q.************************************************************* 

# a = ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
# b = "bug"
# c = {}
# for i in a:
#   count = 0
#   for j in i.split():
#     if j == b:
#       count = count+1
#   c[count]=i
# d = []
# for s in sorted(c):
#   d.append(c[s])
# d.reverse()
# print (d)			# output is - ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']

# Q.*********************************************************** 41
#.... drop empty Items from a given Dictionary ?.
# dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}
# print("Original Dictionary:")
# print(dict1)
# print("New Dictionary after dropping empty items:")
# dict1 = {key:value for (key, value) in dict1.items() if value is not None}
# print(dict1)

# dict1.pop("c3")
# print(dict1)

# Q.************************************************************** 42
# .... filter a dictionary based on values ?.
# marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# print("Original Dictionary:")
# print(marks)
# print("Marks greater than 170:")
# result = {key:value for (key, value) in marks.items() if value >= 170}
# print(result)

#................................

# marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# print("Original Dictionary:")
# print(marks)
# print("Marks greater than 170:")
# for (x,y) in marks.items():
# 	if y >= 170:
# 		print(x,":",y)

# Q.************************************************************ 50
# .... clear the list values in the said dictionary. 

# def test(dictionary):
#     for key in dictionary:
#         dictionary[key].clear()
#     return dictionary

# dictionary = { 
#                'C1' : [10,20,30], 
#                'C2' : [20,30,40],
#                'C3' : [12,34]
#              }
# print("\nOriginal Dictionary:")
# print(dictionary)
# print("\nClear the list values in the said dictionary:")
# print(test(dictionary)) 
#..................................................................

# dictionary = { 
#                'C1' : [10,20,30], 
#                'C2' : [20,30,40],
#                'C3' : [12,34]
#              }
# for key in dictionary:
# 	dictionary[key].clear()
# print(dictionary)

# Q.************************************************* 57
#.... filter even numbers from a given dictionary values ?.
# def test(dictt):
#     result = {key: [idx for idx in val if not idx % 2]  
#           for key, val in dictt.items()}   
#     return result    

# students = {'V' : [1, 4, 6, 10], 'VI' : [1, 4, 12], 'VII' : [1, 3, 8]} 
# print("\nOriginal Dictionary:")
# print(students)
# print("Filter even numbers from said dictionary values:")
# print(test(students))



