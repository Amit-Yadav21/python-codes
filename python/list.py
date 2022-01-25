#............list esxtra question?....................?

# find the item use of index in pop method .
# A=["AMIT","YADAV","BANANA"]
# k=A.pop(1)
# print(k)
#.........................................
#......convert string in list.
# a="amit"
# b=a.split()
# print(b)
#......convert string in list seorated by commas.
# a="amit"
# b=list(a)
# print(b)

#........................................
#.check ascending or not.

# list1 = [1, 2, 3, 5, 4, 8, 7, 9]
# temp_list = list1
# list1.sort()
# if temp_list == list1:
#     print("Given List is in Ascending Order")
# else:
#     print("Given List is not in Ascending Order")
#.....................................................

#find odd and even number .

# list2 = [2, 3, 7, 5, 10, 17, 12, 4, 1, 13]
# for i in list2:
#     if i % 2 == 0:
#         print("even number is=",i)
#     elif i%2!=0:
#     	print("odd number is=",i)

# . odd number.

# x = [1,2,3,4,5,1,3,3,4]
# l1 = []
# for i in x:
#     if x.count(i) % 2 != 0:
#         if i not in l1:
#             l1.append(i)
# print(l1)

#......................................................

#. 
# list5 = [1, 29, 51, 9, 17, 6, 7, 23]
# list5[0], list5[-1] = list5[-1], list5[0]
# print(list5)
#...........................................

# subtract 1 list to 2 list item .

# a = [1, 2, 3, 5]
# b = [1, 2]
# l1 = []
# for i in a:
#     if i not in b:
#         l1.append(i)
# print(l1)
#...............................................

# find 1st,2nd,3rd largest number ?

# mylist=[10,22,78,55,1]
# mylist.sort()
# print("original number",mylist)
# print("1st largest number",mylist[-1])
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
#.............................................

#...................remove dublicate number.
# a=[1,2,2,3,5,8,2,6,4,6,1]
# b=[]
# for i in (a):
# 	if i not in b:
# 		b.append(i)
# print("original list=",a)
# b.sort()
# print("remove dublicate item=",b)

#................remove dublicate number/string.
# a=[]
# size=int(input("how many number are needed:"))
# for i in range(size):
#     number=input("Enter number-")
#     a.append(number)
# print(a)
# b=[]
# for i in a:
# 	if i not in b:
# 		b.append(i)
# print(b)		



#.................................................

# remove dublicate string.
# a=[]
# b=["a","b","a","c","a","d","a","c"]
# for i in (b):
# 	if i not in a:
# 		a.append(i)
# 		a.sort()
# print(a)



#............................................
#.........student name and marks highest and lowest. 

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
#...................................................

# adding in list number .

# items=[1,2,3,4]
# sum_numbers = 0
# for x in items:
#   sum_numbers += x
# print(sum_numbers)
#.............................................

#mixed list
# mixed_list = ["rahul", 12, 9.0, "kaavay", "shivam", 1]
# print (type(mixed_list))

#.......................................

# names_list = ["rahul", "shivam", "kavay", "ashish", "rohit"]
# print (names_list)
# print (type(names_list))
#........................................
########################################################


