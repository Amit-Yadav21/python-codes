num=int(input("Enter number :"))
count=0
for i in range(1,num+1):
	if (num%i==0):
		count=count+1
if count==2:
	print(num,"is  a prime number")
else:
	print(num,"is not a prime number")

# n=int(input("Enter number :"))
# count=0
# i=1
# while(i<=n):
# 	if n%i==0:
# 		count=count+1
# 	i=i+1
# if count==2:
# 	print("prime number")
# else:
# 	print("not prime number")