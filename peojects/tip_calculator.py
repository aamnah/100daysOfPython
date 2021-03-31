print("Welcome to the tip calculator!")

bill_amount = int(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# 12 / 100 = 0.12
tip_amount = bill_amount / tip_percentage   # float
print(f"\nTip amount is: ${round(tip_amount, 2)}")

total_amount = bill_amount + tip_amount
print(f"Total amount is: ${round(total_amount, 2)}")

share_to_pay = total_amount / people

print(f"\nEach person should pay: ${round(share_to_pay, 2)}")