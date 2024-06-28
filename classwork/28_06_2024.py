#!/usr/bin/python

myset = {"banana", "mango", "Apple", "orange", "pineaple"}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
x = [10, 11, 13, 10, 3, 2, 8]
y = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
#myset.update(set2)
#myset.update(x)
#[myset.remove("mango") if "mango" in myset else print("Mango no in the set")]
#for i in myset:
#    print(i)
#set3 = myset.union(set2, x, y)
#set3 = set2 & y
#set2.intersection_update(y)
#set3 = y.difference(set2)
set3 = set2.symmetric_difference(y)
print(set3)

# ------------ Dictionary ---------------
myDict = [
    {
        "name": "Ikenna",
        "age": 20,
        "institution": "FUNAI",
        "graduationYear": 2021,
        "isStudent": False,
        "skill": ["HTML", "CSS", "JS", "C#", "JAVA", "PYTHON"],
        "stack": {
            "frontend": {
                "JavaScript": ["ReactJS", "Vue", "NextJS"],
                "Python": ["Django", "Flask"],
                "PHP": "Laravel",
                "C#": "ASP.NET"
                },
            "backend": {
                "JavaScript": ["Node", "NextJS"],
                "Python": ["Django", "Flask"],
                "PHP": "Laravel",
                "C#": "ASP.NET"
                }
            }
    },
    {
        "name": "Faith",
        "age": 21,
        "institution": "EBSU",
        "graduationYear": 2026,
        "skill": ["HTML", "CSS"],
        "stack": {}
    }
    ]
#skill = myDict.get("skill")
#print(myDict["skill"])
#print(skill)
#print(myDict.keys())
#print(myDict.values())
#print(myDict.items())
#[print(f"you are {myDict['age']} years old") if "age" in myDict else print("Age not in the object")]

#for x in myDict:
#    print(f"{x} : {myDict[x]}")
#[print(f"{x} : {myDict[x]}") for x in myDict]
#print(myDict['stack']['frontend']['JavaScript'][1])
print(myDict[1])
