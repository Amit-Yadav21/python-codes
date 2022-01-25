

# question_list = [
#     "Q.1 How many continents are there?",              
#     "Q.2 What is the capital of India?",            
#     "Q.3 NG mei kaun se course padhaya jaata hai?"
#     # "Q.4 What is the capital of Israyle?",
#     # "Q.5 What is the currency of India?",
#     # "Q.6 What is the cm of Himanchal predesh?",
#     # "Q.7 What is the first precident of ROW ?",
#     # "Q.8 How many permanent member are in UN ?",
#     # "Q.9 which following country has vito power?",
#     # "Q.10 who is prime minister of afganistan?",
#     # "Q.11 How many member are in Indian parliament?",
#     # "Q.12 How many population of HP million accourding 2021 census?",
#     # "Q.13 who is the mentor of Indian cricket team during t20 world cup 2021?"
# ]

# options_list = [
#     ["1) Four", "2) Nine", "3) Seven", "4) Eight"],
#     ["1) Chandigarh", "2) Bhopal", "3) Chennai", "4) Delhi"],
#     ["1) Software Engineering", "2) Counseling", "3) Tourism", "4) Agriculture"],
#     # ["Berlin","Pairis","jerusalam","china"],
#     # ["yen","INR","Euro","Doller"],
#     # ["J.p nadda","jayram thakur","Rahul gandhi","kejrival"],
#     # ["padit nehru","sardar patel","K.N.ROW","Endira gandhi"],
#     # ["5","9","3","6"],
#     # ["india","pakistan","france","Germany"],
#     # ["mullah baradar","stanekzai","asarullah haqqani","Hasan Akhund"],
#     # ["253","543","458","436"],
#     # ["3.4","4.9","8.2","5.2"],
#     # ["ms dhoni","Gautam gambhir","Tendulkar","Rhul darvid"]
# ]

# # har ek question ke liye, uski solution key (yeh index nahi hai)
# # solution_list = [3,4,1]

# a=0
# while a < len(question_list):
#     print(question_list[a])
#     for i in options_list[a]:
#         print(i)
#     user=int(input('enter you answer :---'))
#     if solution_list[a]==user:
#         print('sahi jawab !!!!!')
#     else:
#         print('galat  jawab !!!!!')
#         break
#     a+=1


#........................................................................
# #......................................................................

# question_list = [
#     "1) How many continents are there?",           
#     "2) What is the capital of India?",
#     "3) NG mei kaun se course padhaya jaata hai?",
#     "4) What is the capital of maharashtra?",
#     "5) What is the capital of MP?",
#     "6) What is the national language  india?"
# ]
# options_list = [
#     ["1) Four", "2) Nine", "3) Seven", "4) Eight","5) Lifeline-5050\n"],
#     ["1) Chandigarh", "2) Bhopal", "3) Chennai", "4) Delhi","5) Lifeline-5050\n"],
#     ["1) Software Engineering", "2) Counseling", "3) Tourism", "4) Agriculture","5) Lifeline-5050\n"],
#     ["1) Nagpur", "2) Mumbai", "3) Bhopal", "4) Amritsar", "5) Lifeline-5050\n"],
#     ["1) Delhi", "2) Chennai", "3) Mumbai", "4) Bhopal","5) Lifeline-5050\n"],
#     ["1) Hindi", "2) Telgu", "3) English", "4) Marathi", "5) Lifeline-5050"]
# ]
# solution_list = [ 3, 4, 1, 2, 4, 1]
# fifty50=["1) Four\n2) Sevan","1) Bhopal\n2) Delhi","1) Tourism\n2) Software Engineering","1) Amritsar\n2) Mumbai","1) Delhi\n2) Bhopal","1) English\n2) Hindi"]
# name=input("Enter Your Name :- ")
# print("\n       ✽✽✽✽✽✽✽✽--|| HeLLO MR",name,"||--✽✽✽✽✽","\n✽✽✽✽✽---|| WELCOME TO KON BANEGA KAROROATI GAME ||---✽✽✽✽✽\n             ✽✽✽✽✽✽✽✽✽✽-----KBC-----✽✽✽✽✽✽✽✽✽✽\n")
# a=0
# b=0
# c=1
# #ll=2
# cash=10000
# while a < len(question_list):
#     print("✽✽✽✽✽✽✽---|| Ye Raha Aapka Question No :-",c,"\n✽✽✽✽✽✽✽--- || RS",cash,"Ke Liye Aaka agala question yah raha ||---✽✽✽✽✽✽✽")
#     print(question_list[a],"\n")
#     ae=1
#     for i in options_list[a]:
#         print(i)
#         ae+=1
#     guess=int(input("Enter Yuor Choise :- "))
#     if guess == solution_list[a]:
#         print("✤✤✤|| SHAHI JAWAB ||✤✤✤")
#         print("✽✽✽✽✽---AAPNE RS",cash,"JIT LIYA HAI---✽✽✽✽✽\n")
#     elif guess == 5 and b < 1:
#         b+=1
#         print("Aap 5050 Lifeline Ka Use 1 Hi Bar Kar Sakte Ho")
#         print(fifty50[a])
#         fif50=int(input("ENTER YOUR ANSWER :- "))
#         if fif50 == 2:
#             print("✽✽✽✽✽---|| SAHI JAWAB ||---✽✽✽✽✽")
#     elif guess == 5 and b < 2:
#         print("✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽---|| SORRY ||---✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽")
#         print("✽✽✽--|| AAPNE 50:50 LIFELINE PAHLE HI USE KI HAI ||--✽✽✽")
#         print("✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽---|| GAME OVER ||---✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽")
#         break
#     else:
#         print("✽✽✽✽✽---|| GALA JAWAB ||---✽✽✽✽✽")
#         print("✽-|| AAP GAME SE BAHAR HO GYE HO ||-✽")
#         print("✽✽✽✽✽---|| GAME OVER ||---✽✽✽✽✽")
#         break
#     a+=1
#     #ll+=1
#     c+=1
#     cash+=10000

##################################################
