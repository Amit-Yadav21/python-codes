#... remove dublicate value in list
# a=[1,1,2,2,3,3,4,4,4]
# for i in a:
#   if i in a:
#     a.remove(i)
# print(a)

#---------OR--------OR--------------OR--------

# a=[9,8,7,6,3,5,5,5,4, 4]
# for i in a:
#   for j in range(a.count(i)-1):
#     a.remove(i)
# print(a)

#************************************************
#... multiply of 3 digit without using multiply oparetor ?

# a=int(input("Enter 1st number :"))
# b=int(input("Enter 2nd number :"))
# c=int(input("Enter 3rd number :"))
# c1,c2=0,0
# for i in range(a):
#   c1+=b
# for j in range(c):
#   c2+=c1
# print(c2)

#-------------------------------------------------------

# a,b,c,c1,c2=int(input("Enter 1st number :")),int(input("Enter 2nd number :")),int(input("Enter 3rd number :")),0,0
# for i in range(a):
#   c1+=b
# for j in range(c):
#   c2+=c1
# print(c2)