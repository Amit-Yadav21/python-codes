# i=eval(input("Enter the number "))
# print(i)
# rev=0
# if i.isdigit():
# 	# while i>0:
# 	# 	rev=(rev*10)+i%10
# 	# 	i=i//10

# 		print("palindrome number")
# else:
# 	print("Not palindrome number")



question_list = [
    "1) who is the prime minister of india ?",           
    "2) What is the limit for NDA Exam ?",
    "3) what is the time spend of pricident?",
    "4) Who is the father of computer ?",
]
options_list = [
    ["1) Narendra modi", "2) Rajnath sing", "3) Manmohan singh", "4) amit shah","5) Lifeline-5050","6) Phone of friend\n"],
    ["1) 17.5 years", "2) 18.5 years", "3) 19.5 years", "4) 20 years","5) Lifeline-5050\n"],
    ["1) 6 years", "2) 5 years", "3) 4 years", "4) 8 years","5) Lifeline-5050\n"],
    ["1) MOrgun moly", "2) robrt patkins", "3) Charles babage", "4) Jorj wood", "5) Lifeline-5050\n"],
]
solution_list = [ 1 , 2 , 2 , 3 ]

fifty50=["1) Four\n4) Amit shah","2) 18.5 years\n3) 19.5 years","1) 6 years\n2) 5 years","1) Morgun moly\n3) Charles babage"]
name=input("Enter Your Name :- ")
Age=int(input("Enter Yuor Age :-"))
print("\nHeLLO MR-",name,"\nWELCOME TO KAUN BANEGA KAROROATI\n")
a=0
b=0
c=1
cash=10000
while a < len(question_list):
    print("Ye Raha Aapka Question No :-",c,"\nRS",cash,"Ke Liye Aaka agala question yah raha")
    print(question_list[a],"\n")
    for i in options_list[a]:
        print(i)
    guess=int(input("Enter Yuor Choise :- "))
    if guess == solution_list[a]:
        print("SHAHI JAWAB")
        print("Aapne RS",cash,"Jit Liya Hai\n")
    elif guess == 5 and b < 1:
        b+=1
        print("Aap 5050 Lifeline Ka Use 1 Hi Bar Kar Sakte Ho")
        print(fifty50[a])
        fif50=int(input("Enter Your Answer :- "))
        if fif50 == 2:
            print("Aapka javab sahi hai")
    elif guess == 5 and b < 2:
        print("SORRY ")
        print("AAPNE 50:50 LIFELINE PAHLE HI USE KI HAI")
        print("GAME OVER")
        break
    else:
        print("Aapka javab Galat hai")
        print("AAP GAME SE BAHAR HO GYE HO")
        print("GAME OVER")
        break
    a+=1
    c+=1
    cash+=10000