GRANT_CAP = 15000

def calculateRawCost(participants, costPerHead):
    return participants * costPerHead

def calculateBudget(rawCost, discount):
    return rawCost - (rawCost * discount / 100) + 500

participants = 100
costPerHead = 200
discount = 10

rawCost = calculateRawCost(participants, costPerHead)
finalBudget = calculateBudget(rawCost, discount)

print("Raw Cost:", rawCost)
print("Final Budget:", finalBudget)

if finalBudget <= GRANT_CAP:
    print("Event budget is approved")
else:
    print("Event budget is not approved")



# #====================================


def calculate_fine(days, book_type, premium):
    fine = 0

    if book_type == "standard":
        if days <= 5:
            fine = days * 5
        else:
            fine = 25 + (days - 5) * 10

    elif book_type == "reference":
        fine = days * 20

    if premium:
        fine = fine - (fine * 20 / 100)

    return fine


print(calculate_fine(7, "standard", True))