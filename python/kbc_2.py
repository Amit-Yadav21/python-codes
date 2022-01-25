# que = ["who is the prime minister of india ?","What is the limit for NDA Exam ?","what is the time spend of pricident?","Who is the father of computer ?"]

# op1 = ["1) Narendra modi","1) 17.5 years","1) 6 years","1) Morgun moly"]
# op2 = ["2) Rajnath sing","2) 18.5 years","2) 5 years","2) robrt patkins"]
# op3 = ["3) Manmohan singh","3) 20 years","3) 4 years","3) Charles babage"]
# op4 = ["4) amit shah","4) 19.5 years","4) 8 years","4) Jorj wood"]
# ans = [1, 4, 2, 3]
# Q=1
# cash=0
# print("Question.",Q,"on your computer screan.")
# for s in range(len(que)):
# 	print(que[s])
# 	print(op1[s])
# 	print(op2[s])
# 	print(op3[s])
# 	print(op4[s])
# 	a=int(input("choose your option :--"))
# 	if a==ans[s]:
# 		Q+=1
# 		cash+=1000
# 		print("congratulation! Your answer is correct.You won",cash,"rupees.\n")
# 		if s!=len(que)-1:
# 			print("Next question for Rs",cash+1000)
# 			print("Question.",Q,"on your computer screan.")
# 	else:
# 		print("Your choise answer is wrong.\nout of the Game .")
# 		break
# print("You win Total Amount =",cash)

##########################################################################

#import random,time
# QUE=["Who Is The Prime Minister Of India ?","What Is The Age Limit For NDA Exam ?","What Is The Time Span Of Precident ?","Who Is The Father of Computer ?","How Many States Are In India ?","Which Is Largest State In India By Area ?","Which State Has Beggest Ecomony In India ?","Which State Has Biggest Sea Border ?","Which States Founded On The Basic Of Language Fristly ?","Which Is Smallest States By Area ?","How Many Artical In Our Contutution ?","Which Is Last Point Of India In South ?","Who Many Members Is Indian Parliament ?","What Is Rank Of Indian In Defence ? "]
# op1=["1) Narendra Modi","1) 20 years","1) 6 years","1) Morgun Moly","1) 27","1) Madhye Predesh","1) Maharasatra","1) Tamilanadu","1) kerla","1) Sikkim","1) 300","1) Tamilnadu","1) 300","1) 1"]
# op2=["2) Rajnath Sing","2) 18.5 years","2) 5 years","2) Robert Patricia","2) 28","2) Rajstan","2) Goa"," 2) Kerala","2) Telangana","2) Goa","2) 350","2) Andaman","2) 400","2) 2"]
# op3=["3) Manmoha Sing","3) 17.5 years","3) 4 years","3) Charles Babbage","3) 29","3) Maharasatra","3) Delhi","3) Maharasatra","3) Andraparadesh","3) Meghalya","3) 395","3) Lakshadeep","3) 555","3) 3"]
# op4=["4) Amit Shah","4) 19.5 years","4) 8 years","4) Darma Saty","4) 30","4) Uttar Pradesh","4) Panjab","4) Gujrat","4) Tamilnadu","4) Nagaland","4) 400","4)Indira Point","4) 545","4) 4"]
# ans=[1,4,2,3,2,2,1,4,3,2,3,4,4,4]
# coin,fifty,flip, call, pole, gochi,total,o1, o2, o3, o4=0,0,0,0,0,0,0,0,0,0,0
# for s in range(len(QUE)):
#     print()
#     print("\x1b[31m",f'{s+1}]',QUE[s])
#     print("\x1b[32m",op1[s])
#     print("\x1b[32m",op2[s])
#     print("\x1b[32m",op3[s])
#     print("\x1b[32m",op4[s])
#     print("\x1b[33m","5) Use Lifeline .""\x1b[0m")
#     a=int(input("\x1b[34m""enter your option number:--  ""\x1b[0m"))
#     if a==5:
#         while True:
#             b=int(input("\x1b[33m""* your can use this lifelines only ones.\n   (1) 50-50 Lifeline \n   (2) Phone of friend\n   (3) Audience Pole\n   (4) Flip the Question \n   (5) Gochi \n :=""\x1b[0m"))
#             if b==1:
#                 fifty+=1
#                 if fifty > 1:
#                     print("\x1b[32m""you have used this so you cant use this again.\n you somthing different lifeline.""\x1b[0m")
#                     continue
#                 else:
#                     answers = [op1[s], op2[s], op3[s], op4[s]]
#                     realans = answers.pop(ans[s]-1)
#                     shuf = [realans, random.choice(answers)]
#                     random.shuffle(shuf)
#                     print("\x1b[32m""your fifty-fifty lifeline is.\n", shuf[0],"\n", shuf[1])
#                     a=int(input("\x1b[34m""enter your opption number:--  ""\x1b[0m"))
#                     break
#             elif b==2:
#                 call+=1
#                 if call>1:
#                     print("\x1b[32m""you have used this one time you cant use this again.\n use something different lifeline""\x1b[0m")
#                     continue
#                 else:
#                     print("\x1b[32m""your friend suggested option no.",ans[s])
#                     a=int(input("\x1b[34m""enter your opption number:--  ""\x1b[0m"))
#                     break
#             elif b==3:
#                 pole+=1
#                 if pole>1:
#                     print("\x1b[32m""you have used this so you cant use this again.\n use something different lifeline""\x1b[0m")
#                     continue
#                 for v in range(100):
#                     e=random.randint(1,4)
#                     if e==1:
#                         o1+=1
#                     elif e==2:
#                         o2+=1
#                     elif e==3:
#                         o3+=1
#                     elif e==4:
#                         o4+=1
#                 print("\x1b[32m","option 1 :",o1,"%")
#                 print("\x1b[32m","option 2 :",o2,"%")
#                 print("\x1b[32m","option 3 :",o3,"%")
#                 print("\x1b[32m","option 4 :",o4,"%")
#                 a=int(input("\x1b[34m""enter your option number:--  ""\x1b[0m"))
#                 break   
#             elif b==4:
#                 flip+=1
#                 if flip>1:
#                     print("\x1b[32m""you have used this one time you cant use this again.\n use something different lifeline""\x1b[0m")
#                     continue
#                 if flip==1:
#                     que2=["Who is the prime minister of israel ?","How many contries veto power ?","which is the smallest nation in world by area ?","when was Himachal pradesh established","where is horn of Africa ?"]
#                     Op1=["1) Neftali Benet","1) 6","1) Italy ","1) 1972 ","1) Easr africa"]
#                     Op2=["2) Berjamin netnyhay",'2) 7',"2) vetican city","2) 1971","2) west africa"]
#                     Op3=['3) Yasle leaweli','3) 5',"3) mexico ","3) 1975","3) central africa"]
#                     Op4=["4) Nareadra medi","4) 8", '4) panama',"4) 1980","4) south africa."]
#                     Ans=[1,3,2,2,1]
#                     c=random.randint(0,4)
#                     print()
#                     print("\x1b[31m",que2[c])
#                     print("\x1b[32m",Op1[c])
#                     print("\x1b[32m",Op2[c])
#                     print("\x1b[32m",Op3[c])
#                     print("\x1b[32m",Op4[c])
#                     d=int(input("\x1b[34m""enter your option nunbere:-- ""\x1b[0m"))
#                     if d==Ans[c]:
#                         coin+=10000
#                         print("\x1b[35m""Congratulation! your answer is correct.\n you won",coin,"rupees.""\x1b[0m")
#                     else:
#                         print("Wooo... your answer is wrong , So you are  out of Game.")
#                     break   
#             # elif b==5:
#             #     print("Welcome to gochi lifeline :)")
#             #     print("Close your eyes for 10 seconds and then type your answer then it will be correct :)")
#             #     time.sleep(10)
#             #     a = int(input("Good Luck enter your answer:-- "))
#     if a==ans[s]:
#         coin+=10000
#         print("\x1b[35m""Congratulation! your answer is correct.\n you won",coin,"rupees.""\x1b[0m")
#         if s!=len(QUE)-1:
#             total+=coin
#             print()
#             print("This is your question no",s+2,"for",coin,"rupees")
#     else:
#         if a!=5:
#             print("Wooo... your answer is wrong , So you are  out of Game.")
#             break
# print("\x1b[34m""Now your are going out of game \n so totaly you won",coin,"rupis from our KBC.""\x1b[0m")