age = int(input("Enter age: "))
gender = input("Enter gender (male/female): ")
alone = input("Traveling alone? (yes/no): ")
tatkal = input("Is it Tatkal ticket? (yes/no): ")
blackout = input("Is it a holiday blackout date? (yes/no): ")

if (age >= 60 or (gender == "female" and alone == "yes")) and tatkal == "no" and blackout == "no":
    print("Eligible for discount!")
else:
    print("Not eligible.")