bill = float(input("Enter total bill: "))
friends = int(input("Enter number of friends: "))

tip = bill * 10 / 100

total_bill = bill + tip

per_person = total_bill / friends

print("Original bill:", bill)
print("Tip:", tip)
print("Total bill:", total_bill)
print("Each person pays:", per_person)