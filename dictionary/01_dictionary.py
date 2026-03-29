#Dictionary in python
student = {
    "name":"Ali",
    "age":"21",
    "major":"EE",
    "GPA":"3.5"}

print(student)
print(student["age"])

info = {}

info["country"] = "Pakistan"
print(info)

info["city"] = "Lahore"
print(info)


info["population"] = 14000000
print(info)

info["population"] = 15000000

print(info)

employee = {"name": "Sara", "department": "IT", "salary": 50000, "years": 3}

del employee["years"]

for i in employee:
  print(i)