import requests,json,os
from pprint import pprint

def group_by_year():
    c = {}
    a = open('Task1.json','r')
    b= json.load(a)
    years = []
    for movie in b:
        if movie["year"] not in years:
            years.append(movie["year"])
    years.sort()
    # print(b)
    
    for i in years:
        movie_list=[]
        for movie in b:
            if i == movie["year"]:
                movie_list.append(movie)
        c[i]=movie_list
        
    # pprint(c)
        # print(i['year'])
    with open("task2.json", "w") as f:
        json.dump(c, f, indent=4)
        
group_by_year()