
applicants = []

n = int(input("Enter number of applicants: "))

# Collecting applicant details
for i in range(n):
    print("\nEnter details of Applicant", i + 1)

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    aggregate = float(input("Enter aggregate marks: "))

    subject_count = int(input("Enter number of subjects: "))
    subject_marks = []

    for j in range(subject_count):
        mark = float(input(f"Enter marks of subject {j + 1}: "))
        subject_marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    # Checking eligibility
    if (aggregate >= MIN_AGGREGATE and
        all(mark >= MIN_SUBJECT_MARKS for mark in subject_marks) and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):

        applicants.append({
            "name": name,
            "roll_no": roll_no,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

        print("Eligible for scholarship")

    else:
        print("Not eligible for scholarship")