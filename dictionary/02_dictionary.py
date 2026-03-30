schedule={
    "Monday":("English","Maths"),
    "Wednesday":("AI","OOP"),
    "Friday":("System Design","Probability")
}

for key in schedule:
  print(key,":",schedule[key])

day = input("Enter the Day")
if day not in ("Monday", "Wednesday", "Friday"):
  print("Invalid Day")
else:
   print(schedule[day])

   student = {
    "Ali":(10,20,30),
    "Junaid":(100,90,80),
    "Hammad":(90,70,50),
    }

highestAvg=0
topStudent=""
for key in student:

  score=student[key]
  add=0
  for i in score:
    add += i
  averageScore=add/len(student)
  if(averageScore>highestAvg):
    highestAvg=averageScore
    topStudent=key

  print("Average score of",key,averageScore)

print("Highest Average: ",highestAvg)
print("Top Scorer: ",topStudent)

student["Zara"]=(88, 92, 95)
print(student)

del student["Ali"]


for sutdentName,scores in student.items():
  avg = sum(scores)/len(scores)
  print("Name:",sutdentName,"Scores:",scores,"Average:",avg)

student_info = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "GPA": 3.8
}


print("Entire student dictionary:", student_info)


print("Student Name:", student_info["name"])


print("Student GPA:", student_info["GPA"])

my_dict = {}
print("Initial empty dictionary:", my_dict)


my_dict["country"] = "Pakistan"
print("After adding country:", my_dict)


my_dict["city"] = "Lahore"
print("After adding city:", my_dict)


my_dict["population"] = 14000000
print("After adding population:", my_dict)


my_dict["population"] = 15000000
print("Final dictionary after modifying population:", my_dict)


