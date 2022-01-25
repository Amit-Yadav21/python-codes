question_list = [
    "Q.1 How many continents are there?",              
    "Q.2 What is the capital of India?",            
    "Q.3 NG mei kaun se course padhaya jaata hai?",
    "Q.4 What is the capital of Israyle?",
    "Q.5 What is the currency of India?",
    "Q.6 What is the cm of Himanchal predesh?",
    "Q.7 What is the first precident of ROW ?",
    "Q.8 How many permanent member are in UN ?",
    "Q.9 which following country has vito power?",
    "Q.10 who is prime minister of afganistan?",
    "Q.11 How many member are in Indian parliament?",
    "Q.12 How many population of HP million accourding 2021 census?",
    "Q.13 who is the mentor of Indian cricket team during t20 world cup 2021?"
]

options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],
    ["Berlin","Pairis","jerusalam","china"],
    ["yen","INR","Euro","Doller"],
    ["J.p nadda","jayram thakur","Rahul gandhi","kejrival"],
    ["padit nehru","sardar patel","K.N.ROW","Endira gandhi"],
    ["5","9","3","6"],
    ["india","pakistan","france","Germany"],
    ["mullah baradar","stanekzai","asarullah haqqani","Hasan Akhund"],
    ["253","543","458","436"],
    ["3.4","4.9","8.2","5.2"],
    ["ms dhoni","Gautam gambhir","Tendulkar","Rhul darvid"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1,1,2,2,3,1,3,4,2,4,1]

print("Aapka question yaha hai :")
print(question_list[0])
for i in options_list:
    print("Aapka option yah hai :")
    print("1.Four\n2.nine\n3.Seven\n4.Eight")
    option=int(input("chose your option :"))
    if option==solution_list[0]:
        print("congratulation !\nAaka answer sahi hai:\nyou win=1000\n")
        print("Aapka agala question yaha hai :")
        print(question_list[1])
        for i in question_list:
            print("Aapka option yah hai :")
            print("1.Chandigarh\n2.Bhopal\n3.Chennai\n4.Delhi")
            option=int(input("chose your option :"))
            if option==solution_list[1]:
                print("congratulation !\nAaka answer sahi hai:\nyou win=2000\n")
                print("Aapka agala question yaha hai :")
                print(question_list[2])
                for i in question_list:
                    print("Aapka option yaha hai :")
                    print("1.Software Engineering\n2.Counseling\n3.Tourism\n4.Agriculture")
                    option=int(input("chose your option :"))
                    if option==solution_list[2]:
                        print("congratulation !\nAaka answer sahi hai:\nyou win=4000\n")
                        print("Aapka agala question yaha hai :")
                        print(question_list[3])
                        for i in question_list:
                            print("Aapka option yah hai :")
                            print("1.jerusalam\n2.Berlin\n3.Pairis\n4.china")
                            option=int(input("chose your option:"))
                            if option==solution_list[3]:
                                print("congratulation !\nAaka answer sahi hai:\nyou win=8000\n")
                                print("Aapka agala question yaha hai:")
                                print(question_list[4])
                                for i in question_list:
                                    print("Aapka option yah hai :")
                                    print("1.yen\n2.INR\n3.Euro\n4.Doller")
                                    option=int(input("chose your option:"))
                                    if option==solution_list[4]:
                                        print("congratulation !\nAaka answer sahi hai:\nyou win=16000\n")
                                        print("Aapka agala question yaha hai :")
                                        print(question_list[5])
                                        for i in question_list:
                                            print("Aapka agala question yaha hai :")
                                            print("1.J.P.nadda\n2.jayram thakur\n3.Rahul gandhi\n4.kejrival")
                                            option=int(input("chose your option:"))
                                            if option==solution_list[5]:
                                                print("congratulation !\nAaka answer sahi hai:\nyou win=32000\n")
                                                print("Aapka agala question yaha hai :")
                                                print(question_list[6])
                                                for i in question_list:
                                                    print("Aapka ooption yaha hai :")
                                                    print("1.padit nehru\n2.sardar patel\n3.K.N.ROW\n4.Endira gandhi")
                                                    option=int(input("chose your option :"))
                                                    if option==solution_list[6]:
                                                        print("congratulation !\nAaka answer sahi hai:\nyou win=64000\n")
                                                        print("Aapka agala question yaha hai :")
                                                        print(question_list[7])
                                                        for i in question_list:
                                                            print("Aapka option yaha hai :")
                                                            print("1.5\n2.9\n3.3\n4.6")
                                                            option=int(input("chose your option:"))
                                                            if option==solution_list[7]:
                                                                print("congratulation !\nAaka answer sahi hai:\nyou win=128000\n")
                                                                print("Aapka agala question yaha hai :")
                                                                print(question_list[8])
                                                                for i in question_list:
                                                                    print("Aapka option yah hai:")
                                                                    print("1.india\n2.pakistan\n3.france\n4.Germany")
                                                                    option=int(input("chose your option:"))
                                                                    if option==solution_list[8]:
                                                                        print("congratulation !\nAaka answer sahi hai:\nyou win=256000\n")
                                                                        print("Aapka agala question yaha hai :")
                                                                        print(question_list[9])
                                                                        for i in question_list:
                                                                            print("Aapka option yah hai:")
                                                                            print("1.mullah baradar\n2.stanekzai\n3.asarullah haqqani\n4.Hasan Akhund")
                                                                            option=int(input("chose your option:"))
                                                                            if option==solution_list[9]:
                                                                                print("congratulation !\nAaka answer sahi hai:\nyou win=512000\n")
                                                                                print("Aapka agala question yaha hai :")
                                                                                print(question_list[10])
                                                                                for i in question_list:
                                                                                    print("Aapka option yah hai:")
                                                                                    print("1.553\n2.543\n3.458\n4.436")
                                                                                    option=int(input("chose your option:"))
                                                                                    if option==solution_list[10]:
                                                                                        print("congratulation !\nAaka answer sahi hai:\nyou win=1024000\n")
                                                                                        print("Aapka agala question yaha hai :")
                                                                                        print(question_list[11])
                                                                                        option=int(input("chose your option:"))
                                                                                        for i in question_list:
                                                                                            print("Aapka option yah hai:")
                                                                                            print("1.553\n2.543\n3.458\n4.436")
                                                                                            option=int(input("chose your option:"))
                                                                                            if option==solution_list[11]:
                                                                                                print("congratulation !\nAaka answer sahi hai:\nyou win=2048000\n")
                                                                                                print("Aapka agala question yaha hai :")
                                                                                                print(question_list[12])
                                                                                                for i in question_list:
                                                                                                    print("Aapka option yah hai:")
                                                                                                    print("1.3.4\n2.4.9\n3.8.2\n4.5.2")
                                                                                                    option=int(input("chose your option:"))
                                                                                                    if option==solution_list[12]:
                                                                                                        print("congratulation !\nAaka answer sahi hai:\nyou win=4098000\n")
                                                                                                        print("aap carodpati ban gaye hai\nthank you:")
                                                                                                    else:
                                                                                                        print("Aapka answer galat hai:")
                                                                                                    break    
                                                                                            else:
                                                                                                print("Aapka answer galat hai:")
                                                                                            break
                                                                                    else:
                                                                                        print("Aapka answer galat hai:")
                                                                                    break
                                                                            else:
                                                                                print("Aapka answer galat hai:")
                                                                            break
                                                                    else:
                                                                        print("Aapka answer galat hai:")
                                                                    break
                                                            else:
                                                                print("Aapka answer galat hai:")
                                                            break
                                                    else:
                                                        print("Aapka answer galat hai:")
                                                    break
                                            else:
                                                print("Aapka answer galat hai:")
                                            break
                                    else:
                                        print("Aapka answer galat hai:")
                                    break
                            else:
                                print("Aapka answer galat hai:")
                            break
                    else:
                        print("Aapka answer galat hai")
                    break
            else:
                print("Aapka answer galat hai :")
            break
    else:
        print("Aapka answer galat hai")
    break