from datetime import datetime
entry = datetime.strptime(input("Enter entry time (HH:MM): "), "%H:%M")
exit = datetime.strptime(input("Enter exit time (HH:MM): "), "%H:%M")
vehicle = input("Enter vehicle type (car/bike): ").lower()
if vehicle not in ["car", "bike"]: print("Invalid vehicle type")
else:
    hours = (exit - entry).total_seconds() / 3600
    hours = hours if hours > 0 else hours + 24
    rate = 30 if vehicle == "car" else 15
    fee = min(500, max(1, int(hours + 0.99)) * rate) + (100 if hours > 12 else 0)
    print("Parking hours:", round(hours, 2), "\nTotal parking fee: Rs.", fee if hours > 0 else "Invalid time")