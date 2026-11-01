venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per person: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per person: "))
sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per participant: "))
fixed = venue + equipment + transport
variable = catering + certificate
shortfall = max(0, fixed - sponsorship)
break_even = int(shortfall / (fee - variable)) + 1 if fee > variable and shortfall > 0 else 0 if shortfall == 0 else -1
print("Total fixed cost:", fixed, "\nVariable cost/person:", variable, "\nSponsorship shortfall:", shortfall, "\nMinimum participants:", break_even)