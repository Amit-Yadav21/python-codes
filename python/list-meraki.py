# .Q....nested list convert to flattenlist ?

# nestedlist=([1, 2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12])
# flatlist=[]
# for i in nested:
# 	if type(i)==type([]):
# 		flatening(i)
# 	else:
# 		flatlist.append(i)
# print(flatlist)

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

# name print with index .

# students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
# list_length = len(students_list)
# index = 0
# while index < list_length:
#     print (students_list[index])
#     index = index + 1


#.......break particular index.
# students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
# list_length = len(students_list)
# index = 0
# while index < list_length:
#     print (students_list[index])
#     index = index + 1
#     if index==3:
#     	break
# .....................................
# ######################################################
# Q... ...total mark

#student_marks = [23, 45, 89, 90, 56, 80] 
# length = len(student_marks)
# index = 0
# total_marks = 0
# while index < len(student_marks):
#     total_marks = student_marks[index] + total_marks
#     index = index + 1
# print ("Total Marks: ",str(total_marks))

#student_marks = [23, 45, 89, 90, 56, 80] 
# s=sum(student_marks)
# print(s)


#############################################


# Q....Iterating two lists

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]

# length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
# counter = 0
# while counter < length:
#     print (students[counter] + "=",str(marks[counter]))
#     counter=counter+1

#############################################

#Q........how many number less than50,morethan50.

# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# list_length = len(student_marks)
# index = 0
# less_than50 = 0
# more_than50 = 0
# while index < list_length:
#     marks = student_marks[index]
#     if marks < 50:
#         less_than50 = less_than50 + 1
#     else:
#         more_than50 = more_than50 + 1
#     index = index + 1
# print ("Marks more than 50: ",str(more_than50))
# print ("Marks less than 50: " ,str(less_than50))
# .................................................
# ######################################################
# .(a)......count element.

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# a=len(numbers)
# count=0
# for i in range(a):
# 	count+=1
# print(count	)

# .(b)......count element.

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# count=0
# for i in numbers:
# 	count+=1
# print(count)
#..............................................

# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
# total_marks = 0
# counter = 0
# while counter < len(marks):
#     total_marks = total_marks + 1
#     counter = counter + 1
# print(total_marks)

# #######################################################

# .........list etration qoestion.
#....how many number between 20 to 40 .

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# count=0
# for i in numbers:
# 	if i>20 and i<40:
# 		count+=1
# print(count)
# #####################################################

# find 1st,2nd,3rd max number in list ?

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# numbers.sort()
# print("original number",numbers)
# print("1st largest number",numbers[-1])
# print("2nd largest number",numbers[-2])
# print("3rd largest number",numbers[-3])

# a=[]
# x=int(input("how many number are needed:"))
# for i in range(x):
#     number=int(input("Enter number-"))
#     a.append(number)
#     a.sort()
# print("original number",a)
# print("1st max number",a[-1])
# print("2nd max number",a[-2])
# print("3rd max number",a[-3])

# ########################################################

# ...Reverse Order
# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# print(places[ ::-1])

# ################################################

# ......check palindromeor yes or not.
# a=input("Enter name :")
# b=list(a)
# c=1
# for i in range(len(b)>=c):
# 	d=b[::-1]
# print(d)
# if b==d:
# 	print("palindrome")
# else:
# 	print("not palindrome")


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

# ##################################################3

# ....Nested Lists.
# magic_square = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]

# print (type(magic_square))
# print (type(magic_square[0]))
# print (type(magic_square[1]))
# print (type(magic_square[2]))

# print (sum(magic_square[0]))
# print (sum(magic_square[1]))
# print (sum(magic_square[2]))

# ########################################################3

# .....Difference

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# list3=[]
# for i in list1:
# 	if i not in list2:
# 		list3.append(i)
# print(list3)

# #################################################

# ....Report Card (1)?
#.......sum of number
# marks = [
# [78, 76, 94, 86, 88],
# [91, 71, 98, 65, 76],
# [95, 45, 78, 52, 49]
# ]
# sum=0
# for i in marks:
# 	for j in i:
# 		sum=sum+j
# print(sum)	

# ...................................

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]
# s=[]
# sum=0
# l=len(marks)
# for i in marks:
# 	s.extend(i)
# for i in s:
# 	sum=sum+i
# print(sum)

# avg=sum/l
# print("avg of num=",avg)
# ........................................

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78],
#     [87, 67, 49, 68, 88]
# ]
# nmarks=marks[0]+marks[1]+marks[2]+marks[3]
# print(nmarks)
# sum=0
# for i in nmarks:
# 	sum=sum+i
# print(sum)
#...............average.

# l=len(marks)
# print(l)
# avg=sum/l
# print(avg)

# ##############################################

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]
# s=marks[0]+marks[1]+marks[2]
# print(s)
# sum=0
# l=len(marks)
# for i in s:
# 	sum=sum+i
# print(sum)
# Avg=s/l
# print("Average of given number in marks=",Avg)

# ####################################################

# #..Q..Report Card - Part II

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]

# a=sum(marks[0])
# al=len(marks[0])
# aavg=a/al

# b=sum(marks[1])
# bl=len(marks[1])
# bavg=b/bl

# c=sum(marks[2])
# cl=len(marks[2])
# cavg=c/cl

# # print("Average of 1 year","-",int(aavg))
# # print("Average of 2 year","-",int(bavg))
# # print("Average of 3 year","-",int(cavg))

# print("Average of 1 year","-",int(aavg),"Average of 2 year","-",int(bavg),"Average of 3 year","-",int(cavg))


# .......................................................

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]

# a=sum(marks[0])
# al=len(marks[0])
# aavg=a/al

# b=sum(marks[1])
# bl=len(marks[1])
# bavg=b/bl

# c=sum(marks[2])
# cl=len(marks[2])
# cavg=c/cl

# print("Average of 1 year","-",int(aavg))
# print("Average of 2 year","-",int(bavg))
# print("Average of 3 year","-",int(cavg))
# #..............................................

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78],
#     [87, 67, 49, 68, 88]
# ]

# a=sum(marks[0])
# al=len(marks[0])
# aavg=a/al

# b=sum(marks[1])
# bl=len(marks[1])
# bavg=b/bl

# c=sum(marks[2])
# cl=len(marks[2])
# cavg=c/cl

# d=sum(marks[3])
# dl=len(marks[3])
# davg=d/dl

# print("Average of 1 year","-",int(aavg))
# print("Average of 2 year","-",int(bavg))
# print("Average of 3 year","-",int(cavg))
# print("Average of 4 year","-",int(davg))


################################################################

# .............How to iterate on two lists together?

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]

# print (len(students))
# print (len(marks))

# length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
# counter = 0
# while counter < length:
# 	print (students[counter] + str(marks[counter]))
#.................................................................
#........................or

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# for i in range(len(marks)):
# 	print(students[i],marks[i])


# #####################################################

# ......kitne-aadmi-the
# Q...how many odd numbers and how many even numbers are there in a given list.

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# even=0
# odd=0
# for i in elements:
# 	if i%2==0:
# 		even+=1
# 	else:
# 		odd+=1
# print("even numbers in list=",even)
# print("odd numbers in list=",odd)

# ............................................

#.Q...sum of even and odd number.

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# even=0
# odd=0
# for i in elements:
# 	if i%2==0:
# 		even+=i
# 	else:
# 		odd+=i

# print("sum of even numbers in list=",even)
# print("sum of odd numbers in list=",odd)
# ..............................................

# .Q..avg kitana hai even and odd number.

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# even=ecount=0
# odd=ocount=0
# for i in elements:
# 	if i%2==0:
# 		even+=i
# 		ecount+=1
# 	else:
# 		odd+=i
# 		ocount+=1
# print("Avg of even numbers in list=",int(even/ecount))
# print("Avg of odd numbers in list=",int(odd/ocount))

########################################################

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

#########################################################

# Q.........How many Crorepati?

# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# corodpati=lakhpati=dilwale=0
# for i in kitna_paisa_hai:
# 	if i>=10000000:
# 		corodpati+=1
# 	elif i>=100000:
# 		lakhpati+=1
# 	else:
# 		dilwale+=1
# print(corodpati,"corodpati")
# print(lakhpati,"lakhpati")
# print(dilwale,"dilwale")

################################################
# #.....Count Occurences

# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# a=char_list.count("a")
# n=char_list.count("n")
# t=char_list.count("t")
# x=char_list.count("x")
# u=char_list.count("u")
# g=char_list.count("g")

# print("a","-",a,"times")
# print("n","-",n,"times")
# print("t","-",t,"times")
# print("x","-",x,"times")
# print("u","-",u,"times")
# print("g","-",g,"times")


##################################

# .....Duplicates submission_type: Duplicates
# ...remove Dublicates 

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# a=[]
# for i in (n):
# 	if i not in a:
# 		a.append(i)
# print("original list=",n)
# a.sort()
# print("remove dublicate item=",a)
#..........................................

# .....Duplicates submission_type: Duplicates
#..input lekar

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
#...........................................................

# max number

# a=[]
# x=int(input("how many number are needed:"))
# for i in range(x):
#     number=int(input("Enter number-"))
#     a.append(number)
#     a.sort()
# print("original number",a)
# print("1st max number",a[-1])
# print("2nd max number",a[-2])
# print("3rd max number",a[-3])

#...................................................

# Q. remove dublicate using take new list and append method?

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13,17,17, 11,17,33,17]
# for s in n:
#     b=n.count(s)
#     if b>1:
#         n.remove(s)
# for s in n:
#     b=n.count(s)
#     if b>1:
#         n.remove(s)
# print(n)

###############################################

# # ....Debugging Part 2
# # ...Question 1

# marks = [10,32,42,65,67,89,76,38,67]
# total_marks = 0
# counter = 0
# while counter < len(marks):
#     total_marks = total_marks + 1
#     counter = counter + 1
# print(total_marks)
#....................................................

# #..Question 2

# name = ["Savitri", "Phule", "26"]
# # Ab hum iss list ko use karke poora naam (full name) print karna chaste hai
# print (name[0]+name[1])
# # Code mei dekhiye naam theek se print kyu nahi ho raha

###################################################

# Q....magic_square

# magic_square = [
#     [5, 3, 7],
#     [1, 8, 9],
#     [6, 4, 2]
# ]
# for i in magic_square:
# 	if i in magic_square:
# 		row0=sum(magic_square[0])
# 		row1=sum(magic_square[1])
# 		row2=sum(magic_square[2])
# 		print(row0,row1,row2)
# 		break
# 	 elif i in magic_square:
# 	 	col=sum(,magic_square[0][0])

####################################################3

# Q....Iterating two lists

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]

# length = len(students) # kyunki dono ki same length hai toh jiski bhi length le sakte ho
# counter = 0
# while counter < length:
#     print (students[counter] + str(marks[counter]))
#     counter=counter+1
#####################################################

# Q..How many Crorepati?
# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
# corodpati=lakhpati=dilwale=0
# for i in kitna_paisa_hai:
# 	if i>=10000000:
# 		corodpati+=1
# 	elif i>=100000:
# 		lakhpati+=1
# 	else:
# 		dilwale+=1
# print(corodpati,"corodpati")
# print(lakhpati,"lakhpati")
# print(dilwale,"dilwale")

#################################################

# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# subStr = "over"
# mainStr.remove("over")
# print(mainStr)


#########################################################################################


 #................Bubble sort 

# size=int(input("Enter sze of sort list :"))
# a=[]
# for i in range(size):
# 	val=int(input("Enter number :"))
# 	a.append(val)
# for i in range(size):
# 	for j in range(0,size-i-1):
# 		if a[j]>a[j+1]:
# 			t=a[j]
# 			a[j]=a[j+1]
# 			a[j+1]=t
# print("sorted array is=",a)

######################################

# Q..input name and number , remove comma and string ?

# a=[]
# size=int(input("how many number are needed:"))
# for i in range(size):
#     num=input("Enter number-")
#     a.append(num)
# print(a)
# print(*a)

#############################################


# a=int(input("Enter no. of rows :"))
# for i in range(a):
# 	b=1
# 	for j in range(1,a-i):
# 		print(end="")
# 	for k in range(i+1):
# 		print(b,end="")
# 		b=int(b*(i-k)/(k+1))
# 	print()



a=int(input("Enter no. of rows :"))
for i in range(a):
	b=1
	for j in range(1,a-i):
		print(end="")
	for k in range(i+1):
		print(b,end="")
		b=int(b*(i-k)/(k+1))
	print()