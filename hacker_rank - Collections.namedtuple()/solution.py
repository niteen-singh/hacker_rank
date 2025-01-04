num_students = int(input())
fields = input().split()

marks_index = fields.index('MARKS')
total_marks = 0

for _ in range(num_students):
    data = input().split()
    total_marks += int(data[marks_index])

print(total_marks / num_students)