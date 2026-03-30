grade_book = {
    "John": (85, 90, 78),"Jane": (92, 88, 95),"Ali": (70, 75, 80),
    "Emily": (90, 85, 88)
}
print("Initial Grade Book:", grade_book)
student_averages = {}
for student, scores in grade_book.items():
    average = sum(scores) / len(scores)
    student_averages[student] = average
    print(f"{student}'s average score: {average:.2f}")

highest_avg_student = None
highest_average = -1

for student, average in student_averages.items():
    if average > highest_average:
        highest_average = average
        highest_avg_student = student
print(f"\nStudent with the highest average: {highest_avg_student} (Average: {highest_average:.2f})")
grade_book["Zara"] = (88, 92, 95)
print("\nGrade book after adding Zara:", grade_book)
if "Ali" in grade_book:
    del grade_book["Ali"]
print("Grade book after removing Ali:", grade_book)
print("\nFinal Grade Book (Students and their averages):")
final_student_averages = {}
for student, scores in grade_book.items():
    average = sum(scores) / len(scores)
    final_student_averages[student] = average
    print(f"{student}: {average:.2f}")