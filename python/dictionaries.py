# .***********************************************Access item key ? 

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["model"])

#......OR.....OR.....OR.........OR........ ?.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# print(x)

#.......OR......get method ?.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("model")
# print(x)


# ...... print all item in dic.

# print dic.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# .... ...................................remove dublicate item in dic.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,     # remove dublicate item .
#   "year": 2020
# }
# print(thisdict)

# .................................................

# .......String, int, boolean, and list data types:

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# print(thisdict["colors"])

# .............................................

# #.................Access all key in dict.
# #...The keys() method will return a list of all the keys in the dictionary.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.keys()
# print(x)

# #######################################

# .."""Add a new item to the original dictionary,and see that the keys list gets updated as well:

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }


# car["color"] = "white"      #...Add a new item to the original dictionary.

# print(car)

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change

# ###########################################

# *****************************************************Access All item value ?.

# The values() method will return a list of all the values in the dictionary.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.values()
# print(x)

# ################################################

# ..Make a change in the original dictionary ?.

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# car["year"] = 2020

# print(car)

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change

# ......................................

# ..Add a new item to the original dictionary?.

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change

# ####################################

# ..The items() method will return each item in a dictionary, as tuples in a list.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.items()
# print(x)

# #######################################


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print("before the change",x) #before the change

# car["year"] = 2020

# print("after the change",x) #after the change

# ...................................

# ..#..The items() method will return each item in a dictionary, as tuples in a list.

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change

# ####################################

# ************************************************************** Chenge item ?.
# ..change the value of a specific item by referring to its key name:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018
# print(thisdict)

# ####################################

# ..........................................change/Update Dictionary ?.
# ..........Update the "year" of the car by using the update() method:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)

# *************************************************************Adding Items ?.

# thisdict =  {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# .............................. Update Dictionary ?.

# ...The argument must be a dictionary, or an iterable object with key:value pairs ?.
# ..Add a color item to the dictionary by using the update() method:


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})
# print(thisdict)

# ***************************************************************** Remove Dictionary Items ?.

# ...Removing Items ?.

# thisdict =  {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("year")	# remove partikular keys 
# print(thisdict)

# ####################

# ......The popitem() method removes the last inserted item ?.
# thisdict =  {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# ###########################

# ********The del keyword removes the item with the specified key name ?.

# thisdict =  {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]		# partikular key delete
# print(thisdict)

# ...................... The del keyword can also delete the dictionary completely:

# thisdict =  {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict			# All dictionary delete .
# print(thisdict)

# ..... The clear() method empties the dictionary ?.

# thisdict =  {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)

# ****************************************************************** Loop Through a Dictionary ?.

# .....Print all key names in the dictionary, one by one ?.

# thisdict =  {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(x)

# .... Print all values in the dictionary, one by one ?.

# thisdict =  {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(thisdict[x])

# .... You can also use the values() method to return values of a dictionary ?.

# thisdict =  {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.values():
#   print(x)

# .... You can use the keys() method to return the keys of a dictionary ?.

# thisdict =  {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.keys():
#   print(x)

# .... Loop through both keys and values, by using the items() method ?. 

# thisdict =  {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x, y in thisdict.items():
#   #print(x, y)
#   print(x,":",y)

# *************************************************************** Copy a Dictionary ?.

# .... Make a copy of a dictionary with the copy() method:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# ..... Make a copy of a dictionary with the dict() function:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)

#********************************************Method  ?.

#.....fromkeys method .

# x = ('key1', 'key2', 'key3')
# y = 0
# thisdict = dict.fromkeys(x,y)
# print(thisdict)     # key not zero. 

#.......................................

# x = ('key1', 'key2', 'key3')
# thisdict = dict.fromkeys(x)
# print(thisdict)   # value print None .

#..... setdefault() Method ?.

###################################################################################

# Accece value by index 

# a={"student":[{"firstname":"amit","lastname":"yadav"}]}

# x = a["student"][0]
# print(x["firstname"])
# print(x["lastname"])

