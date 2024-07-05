income = int(input("Enter your monthly income: "))
expense = int(input("Enter your total monthly expenses: "))
monthly_saving = income - expense
projected_saving = int(monthly_saving * 12 + (monthly_saving * 12 * 0.05))
print("Your monthly savings are $" + str(monthly_saving) + ".")
print("Projected savings after one year, with interest, is: $" + str(projected_saving) + ".")