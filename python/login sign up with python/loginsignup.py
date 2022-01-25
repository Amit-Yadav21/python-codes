import json ,os
print('''
1.sign up
2.sign in
3.delete account
4.update account ''')

def signup():
    # b=[]
    
    c={}
    c["name"]=input("Enter name :")
    c["Email"]=input("Enter Email:")
    c["Password"]=input("Enter Password:")
    if (os.path.exists("database.json")):
        aa=open("database.json","r")
        b=json.load(aa)
        for i in b:
            if i["Email"]==c["Email"]:
                print("dublicate Entry")
                return
    else:
        b=[]

    b.append(c)
    d=open("database.json","w")
    json.dump(b,d,indent=4)
    print(d)

def signin():
    a=input("Enter Email :")
    b=input("Enter password :")
    c=open("database.json","r")
    d=json.load(c)
    for i in d:
        if i["Email"]==a and i["Password"]==b :
            return "welcome "+i["name"]
    return("you are not register")

def delete():
    a=input("Enter Email :")
    b=input("Enter password :")
    c=open("database.json","r")
    d=json.load(c)
    for i in d:
        if i["Email"]==a and i["Password"]==b :
            d.remove(i)
            print("data delete")
            e=open("database.json","w")
            json.dump(d,e,indent=4)
            return
    print("data not find")

def update():
    a=open("database.json","r")
    b=json.load(a)
    a1=input("Enter Email :")
    b1=input("Enter password :")
    cc=0
    for i in b:
        if i["Email"]==a1 and i["Password"]==b1 :
            a11=input("Enter name :")
            b11=input("Enter password :")
            b.remove(i)
            b.append({"name":a11,"Email":i["Email"],"Password":b11})
            d=open("database.json","w")
            json.dump(b,d,indent=4)
            return
        cc+=1

a=int(input("choose your option :"))
if a==1:
    signup()
elif a==2:
    print(signin())
elif a==3:
    delete()
elif a==4:
    update()
