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

# out_file = open("myfile.json", "w")
  
# json.dump(dict1, out_file, indent = 6)
  
# out_file.close()


import json
employee={'name':'amit',
          'age':25,
          'salery':15000,
          'ismarried':True,
          'isshavinggirlfrinde':None
          }
json_string = json.dump(employee)
print(json_string)
# print(type(json_string))

# with open('emp.json','w') as f:
#   json.dumps(json_string,f, indent=4)