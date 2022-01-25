import json
people_string = '''     
{
  "states"= [
    {
      'name':"amit",
      "abriviation":"xl",
      "area_code":["320","251","502"],
    },
    { "name":"Alaka",
      "abriviation":"AK",
      "area_code":["201","140","032","412"]
    }
    { "name":"Ala",
      "abriviation":"AKo",
      "area_code":["21","10","002","402"]
    }
  ]
}'''

with open('sta.json') as f:
  data = json.load(f)
print(data)

# for state in data['states']:
#   print(state)
# #............................

# # with open('states.json','r') as f:
# #   data = json.load(f)

# # for state in data['states']:
# #   del state['area_code']

# # with open('new_state.json','w') as f:
# #   json.dump(data,f, indent=2)

