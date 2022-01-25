#............... convert from python to JSON ?
#.............JSON.dumps () method ?
# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# # convert into JSON:
# y = json.dumps(x)
# # the result is a JSON string:
# print(y)
#******************************Parse JSON - Convert from JSON to Python ?
#................  using the json.loads() method ?
# import json

# # some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])

#****************************************************

# import json
# my = '''{
#   "name":"Amit",
#   "score":11.75,
#   "isAdmin":"false",
#   "license":"null",
#   "shopitems":["food","oil","clothes"],
#   "myobj":{
#         "name":"nested",
#         "marks":45
#   }
# }'''

# y=json.loads(my)
# print(y["shopitems"][2])
#...........................................................
# import json
# my ={
#   "name":"Amit",
#   "score":11.75,
#   "isAdmin":False,
#   "license":"null",
#   "shopitems":("food","oil","clothes"),
#   "myobj":{
#         "name":"nested",
#         "marks":45
#   }
# }
# y=json.dumps(my)
# print(y)

#*********************************************************** read and write file ?

# import json
# employee={'name':'amit',
#           'age':30,
#           'salery':15000,
#           'ismarried':True,
#           'isshavinggirlfrinde':None
#           }
# json_string = json.dumps(employee)
# print(json_string)


# with open('ka.json','r') as f:    #....read ka.json file
#   d=json.load(f)
# print(d)
# print(d['name'])

# with open('ka.json','r') as f:    #....read ka.json file
#   d=json.loads(f.read())
# print(d['salery'])

#.........................................................
#................. How to access b value ?
# import json
# my = '''{
#   "name":"Amit",
#   "score":11.75,
#   "isAdmin":"false",
#   "license":"null",
#   "shopitems":["food","oil","clothes"],
#   "myobj":{
#         "name":"nested",
#         "marks":45,
#         "shopitem2":["chay","roti",{"a":"mota"},{"b":"mama"}]
#   }
# }'''
# y=json.loads(my)
# print(y["myobj"]["shopitem2"][3]["b"])

#....................................................................


# import json
# employee={'name':'amit',        
#           'age':25,
#           'salery':15000,
#           'ismarried':True,
#           'isshavinggirlfrinde':None
#           }
# # json_string = json.dumps(employee, indent=4)
# # print(json_string)
# # print(type(json_string))

# with open('emp.json','w') as f:       
#   y=json.dump(employee,f, indent=1)
# print(y)

#...................................

# import json
# my = '''{
#   "name":"Amit",
#   "score":11.75,
#   "isAdmin":"false",
#   "license":"null",
#   "shopitems":["food","oil","clothes"],
#   "myobj":{
#         "name":"nested",
#         "marks":45,
#         "shopitem2":["chay","roti",{"a":"mota"},{"b":"mama"}]
#   }
# }'''
# y=json.loads(my)
# print(y)


# y=json.loads(my)
# for k,v in y.items():
#   print(k,":",v)

# y=json.loads(my)
# for k,v in y.items():
#   print('{} : {}'.format(k,v))


# y=json.loads(my)
# for k in y:
#   print(k,":",y[k])

# y=json.loads(my)
# z=y['name']
# print(z) 

# f=open('my1.json')    # not complited
# y=json.load(f)
# print(y)
# f.close()

#........................................................


# import json
# dict1 ={
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     },
# }

# mystring = json.dumps(dict1, indent=4)
# print(mystring)

# out_file = open("myfile.json", "w")
# json.dump(dict1, out_file, indent = 4)
# out_file.close()

#.................................................. ???????????

# import json

# people_string = '''
# {
#   "people":[
#   {
#     "name":"Jonh smith",
#     "phone":"251525154",
#     "email":["jonhsmith@gmail.com","jonh.smith@work-place.com"],
#     "has_linces":false
#     },
#     {
#     "name":"amit yadav",
#     "phone":"9651025253",
#     "Email":"yadavamit222137",
#     "has_linces":true
#     }
#   ]
# }'''

# data=json.loads(people_string)
# for people in data['people']:
#   print(people)
#   print(people["name"])

# del people['phone']

# data=json.loads(people_string)
# new_string=json.dumps(data, indent=2,)
# print(new_string)


# data=json.loads(people_string)
# new_string=json.dumps(data, indent=2, sort_keys=True)
# print(new_string)

#...........................................

# import json
# # not complited
# people_string = '''     
# {
#   "states"= [
#     {
#       'name':"amit",
#       "abriviation":"xl",
#       "area_code":["320","251","502"],
#     },
#     { "name":"Alaka",
#       "abriviation":"AK",
#       "area_code":["201","140","032","412"]
#     }
#     { "name":"Ala",
#       "abriviation":"AKo",
#       "area_code":["21","10","002","402"]
#     }
#   ]
# }'''

# with open('states.json','r') as f:
#   data = json.load(f)
# print(data)


# for state in data['states']:
#   print(state)
# #............................

# # with open('states.json','r') as f:
# #   data = json.load(f)

# # for state in data['states']:
# #   del state['area_code']

# # with open('new_state.json','w') as f:
# #   json.dump(data,f, indent=2)

#...................................

# with open('stu1.json','w',encoding='utf-8') as f:
#   json.dump(people_string,f,ensure_ascii=False,indent=5)

#*********************************************************************************
#.................................... Question 1 ?

# import json
# my = '''{           # not complited 
#   "name":"Amit",
#   "score":11.75,
#   "isAdmin":"false",
#   "license":"null",
#   "shopitems":["food","oil","clothes"],
#   "myobj":{
#         "name":"nested",
#         "marks":45,
#         "shopitem2":["chay","roti",{"a":"mota"},{"b":"mama"}]
#   }
# }'''
# y=json.loads(my)
# print(y)

#................................... Question 4 ?
# import json
# m = {
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4
#     }
# print(json.dumps(m, indent=4, sort_keys=True))

#......................... question 6 ?

# import json
# k = {"a":  1,
#      "a":  2,
#      "a":  3, 
#      "a": 4,   
#      "b": 1, 
#      "b": 2
#  }

# l=json.dumps(k)
# print(l)

#.................................question 7 ?

# import json

# n = {
#     "Name": "Abhishek",
#     "Designation": "CEO of navgurukul",
#     "Gender":"male",
#     "Age": "29"
#     }

# o = json.dumps(n , indent=4)
# print(o)

#....................................... Question 8 ?





# import json, time

# # some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'
# # y=0

# # # parse x:
# # y = json.loads(x)

# # # print(x["age"])
# # # the result is a Python dictionary:
# # print(y["age"])

# a= open('filename.json', 'r')
# # time.sleep(5)
# x=(a.read()).split()
# print(x)
# y = json.load(x)
# print(type(y))
# # a.write('we are learning file handling.')


# a.close()





