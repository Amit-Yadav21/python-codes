#.......print half capital and half small charector

# a=input('Enter strpng :')
# b=len(a)
# c=len(a)//2
# d=a[:c]
# e=a[c:]
# print(d.upper()+e.lower())

#......................................

#......print one capital and one small input string/

# num=int(input("Enter number-"))
# b=num//1000
# c=b//100
# if num<100:
# 	print("Enter number greater than 100")
# elif c%2==0:
# 	print("100 place of",num,"is",c,"divisible by 2")
# elif c%2!=0:
# 	print("100 place of",num,"is",c," not divisible by 2")

#...............................................................
#...print revars srting 

# a=input("enter your name :")
# b=""
# for i in a[::-1]:
# 	b+=i
# print(b)

#...........................................
#......print srting sepreted by comma.

# i=input()
# a=i.replace("",",")
# print(a.strip(","))

#.......................................

#......string value divide even and odd,string sepreted by comma

# a=input("Enter srtinge-")
# b=len(a)
# c=len(a)//2
# d=a[:c]
# e=a[c:]
# print(d)
# print(e)

#...........................///////////////

#.........count alphabet and digit

# a=input("Enter name:")
# l=0
# for i in (a):
# 	if i.isalpha():
# 		l=l+1
# print("latter",l)


# a=input("Enter number:")
# d=0
# for i in (a):
# 	if i.isdigit():
# 		d=d+1
# print("Digit",d)

#..................................................

#.....2nd max find.

# a = int(input("Input first number: "))
# b = int(input("Input second number: "))
# c = int(input("Input third number: "))
# if a > b:
#     if a < c:
#         maximum = a
#     elif b > c:
#         maximum = b
#     else:
#         maximum= c
# else:
#     if a > c:
#         maximum= a
#     elif b < c:
#         maximum= b
#     else:
#         maximum= c