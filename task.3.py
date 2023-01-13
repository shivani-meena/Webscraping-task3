from task2 import movie_dict
from pprint import pprint
import json

def group_by_year():
    year_list=[]
    dict={}
    for i in movie_dict:
        i=int(i)
        m=i%10
        n=i-m
        if n not in year_list:
            year_list.append(n)
    print(year_list)
    year_list.sort()
    print(year_list)
    for i in year_list:
        dict[i]=[]
    for i in dict:
        g=i+9
        for x in movie_dict:
            if x<=g and x>=i:
                for v in movie_dict[x]:
                    dict[i].append(v)
    with open("task3.json","w") as a:
        json.dump(dict,a,indent=6)
    return dict
n=group_by_year()



