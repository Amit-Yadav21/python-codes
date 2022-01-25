# import json

# file = open('demo.json', 'r')
# dict1 = {
#     "name": "amit",
#     "age" : 25,
#     "gender": "M",
#     "contact_no": 124567890
# }

# a=json.load(file)
# print(a)
# file.close()

#....................................................

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
# # # print(y)
# for k,v in y.items():
#   print(k,":",v)


# y=json.loads(my)
# for k,v in y.items():
#   print('{} : {}'.format(k,v))


# y=json.loads(my)
# for k in y:
#   print(k,":",y[k])

# # # # z=y['name']
# # # # print(z) 

# f=open('my1.json','r')
# y=json.load(f)
# print(y)
# f.close()


