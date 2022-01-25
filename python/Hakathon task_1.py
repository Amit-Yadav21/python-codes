import random
rand=random.randit(1,10)
for i in range(1,6):
	num=int(input("Enter number :"))
	print(rand)
	if num==rand:
		print("guessed")
		break
	else:
		print("try again")

