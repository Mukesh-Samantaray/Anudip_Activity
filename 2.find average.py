marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks of subject {i}: "))
    marks.append(mark)

average = sum(marks) / 5

if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'F'

print(f"Average = {average}")
print(f"Grade = {grade}")
