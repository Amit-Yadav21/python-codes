

# a={"a":1,"b":2,"c":2}
# for k in a:
#   print({a[k]:k})

###########################################
#.......Employee_details

# from pprint import pprint
# a = ["emp1","emp2","emp3","emp4"]
# b = ["Amit","Satyam","Pavan","Ankit"]
# c = [20,23,25,28]
# d = ["NodeJS_dev.","google_dev.","mobile_dev","Java_dev."]
# f={}
# for j,k,l,m  in zip(a,b,c,d):
#   g={}  
#   g["name"]=k
#   g["age"]=l
#   g["job"]=m
#   f[j]=g
# pprint([f])

#............... OR......OR............ ?

# a = ["emp1","emp2","emp3","emp4"]
# b = ["Amit","Satyam","Pavan","Ankit"]
# c = [20,23,25,28]
# d = ["NodeJS_dev.","google_dev.","mobile_dev","Java_dev."]
# f={}
# for j,k,l,m  in zip(a,b,c,d):
#   g={}  
#   g["name"]=k
#   g["age"]=l
#   g["job"]=m
#   f[j]=g
# print(f)

#.......Employee_details

# a = ["Name","Age","Job"]
# b = [["Ankit","Satyam","Amit","Pavan"],[20,21,22,21],["developer","google","mobile_dev","frontaint"]]
# c = ["emp1","emp2","emp3","emp4"]
# n =len(c)
# dic = {}
# for i in range(n):
#   dic1={}
#   for j in range(len(a)):
#     dic1[a[j]]=b[j][i]
#   dic[c[i]]=dic1
# print(dic)

#######################################################3

# dict1 = {"a":20,"c":40,"b":60}    # correct
# dict2 = {"a":40,"b":20,"d":10}
# for i in dict1:
#   for j in dict2:
#     if i==j:
#       dict1[i]=dict1[i]+dict2[j]
# print(dict1)
     
 

# dict1 = {"a":20,"c":40,"b":60}    # not correct
# dict2 = {"a":40,"b":20,"d":10}
# for i in dict1:
#   for j in dict2:
#     dict1[i]=dict1[i]+dict2[j]
#     if j not in dict1:
#       # print(j)
#       # dict1[j]=dict2[j]
#       dict1.update(dict2)
# print(dict1)