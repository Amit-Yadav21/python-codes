# Q..Guessing Game

"""This is going to be a simple guessing game where the computer will 
generate a random number between 1 to 10, and the user has 
to guess it in 5 attempts."""

# # #...guessing game use random

# import random
# for i in range(1,6):
# 	rand=int(random.randint(1,10))
# 	num=int(input("Enter number :"))
# 	print(rand)
# 	if num==rand:
# 		print("guessed")
# 		break
# 	else:
# 		print("try again")
# 		if rand<num:
# 			print("more than rand number")
# 		else:
#             print("less than number")
#         choice=input("do you want playing again ? (y/n):")
#         if choice=="y":
#             pass
#         else:
#             break      

# #############################################################################

# Rolling the dice

"""Similar to the “Guess the Number” game above, building a die roller
 can be used to play games. Or you can make one similar to a Magic 6-Ball 
 to answer your most profound questions! Skills used: Random library, print, while loops."""

# ## rolling the dice..
# import random
# print('welcome to dice rolling game: ')
# s1=0
# s2=0
# for i in range(1,7):
#     if i>1 and i<7:
#         f=input('roll again? (y/n)')   
#         if f=='y':
#             pass
#         else:
#             break
#     p1=input('roll dice player 1: ')
#     c=random.randint(1,6)
#     print(c)
#     s1+=c
#     p2=input('roll dice player 2: ')
#     d=(random.randint(1,6))
#     print(d)
#     s2+=d
# print('player 1: ',s1,'\n','player 2: ',s2)
# if s1>s2:
#     print('player 1 is winner: congrats: ')
# elif s2>s1:
#     print('player 2 is winner: congrats: ')
# else:
#     print("it's a Tie: ")

# ##################################################################################

# Text-Base Adventure Game

"""A Text-Based Adventure Game is a type of game in which a player has to make 
choices (Yes / No) in every step of the game.

Based on these choices, the storyline changes, and at last, 
we get to know that whether the player wins or loses the game."""



# print("""my name is amit and  i am 24 year old. i am from u.p which is located in jaunpur.
#  i have completed graduation in B.com.
#  In my family there are 4 members including me.""")
# p=0
# a = 0
# w=0
# while a<1:
#     print("""Q1)what is my name?
#     1)roshan 
#     2)akash
#     3)amit
#     4)amol""")
#     a1=input("enter your answer:- ")
#     if a1=="3":
#         print("congratulations, your answer is right.")
#         p+=1
#     else:
#         print("sorry,your answer is wrong")
#         w-=1
#     # a+=1    
#     print("""Q2) how old i am?
#     1)21
#     2)22
#     3)23
#     4)24""")
#     a2=input("enter your answer ;- ")
#     if a2=="4":
#         print("congratulations, your answer is right.")
#         p+=1
#     else:
#         print("sorry,your answer is wrong")
#         w-=1
#     # a+=1
#     print("""Q3)where do you living?
#     1)mumbai
#     2)delhi
#     3)utter pradesh
#     4)pune""")
#     a3=input("enter your answer :- ")
#     if a3=="3":
#             print("congratulations, your answer is right.")
#             p+=1
#     else:
#         print("sorry,your answer is wrong")
#         w-=1
#     # a+=1
#     print("""Q4) what is my qualification?
#     1)10th pass
#     2)12th pass
#     3)graduation
#     4)post graduation""")
#     a4=input("enter your number :- ")
#     if a4=="3":
#          print("congratulations, your answer is right.")
#          p+=1
#     else:
#         print("sorry,your answer is wrong")
#         w-=1
#     # a+=1
#     print("""Q5)In which subject i have bachelor degree?
#     1)Biology
#     2)math
#     3)chemestry
#     4)economics
#     5)B.com""")
#     a5=input("enter your answer :- ")
#     if a5=="5":
#          print("congratulations, your answer is right.")
#          p+=1
#     else:
#         print("sorry,your answer is wrong")
#         w-=1
#     # a+=1
#     print("you points",p)
#     print("your wrong points",w)
#     a+=1