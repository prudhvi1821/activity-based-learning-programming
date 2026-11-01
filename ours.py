n = int(input("Enter number of students: "))
m = int(input("Enter number of subjects: "))
marks = [[float(input(f"Student {i+1}, Subject {j+1}: ")) for j in range(m)] for i in range(n)]
for i, row in enumerate(marks):
    print("Student", i+1, "Total:", sum(row), "Average:", round(sum(row)/m, 2))
for j in range(m):
    col = [marks[i][j] for i in range(n)]
    avg = sum(col) / n
    print("Subject", j+1, "Average:", round(avg, 2))
    if avg < 40: print("Low performance subject:", j+1)
totals = [sum(row) for row in marks]
print("Top Performer: Student", totals.index(max(totals))+1, "with", max(totals), "marks")