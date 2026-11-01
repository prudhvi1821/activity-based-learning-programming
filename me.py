 total = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))
threshold = float(input("Enter eligibility percentage: "))
current = (attended / total) * 100
print("Current Attendance:", round(current, 2), "%")
if current >= threshold:
    print("You are already eligible")
else:
    required = 0
    while ((attended + required) / (total + required)) * 100 < threshold: required += 1
    print("Minimum consecutive classes required:", required)