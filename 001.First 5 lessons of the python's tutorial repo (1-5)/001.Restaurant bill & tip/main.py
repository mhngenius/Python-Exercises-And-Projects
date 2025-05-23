# Create a small app that asks for the total bill and tip percentage,
# then calculates how much each person should pay if the bill is split.

bill = int(input("Enter the price of the bill: "))
tip_percentage = int(input("Enter the percentage of tip: "))
amount_of_people = int(input("How many people are there? "))

tip_amount = (bill * tip_percentage) / 100

total_with_tip = bill + tip_amount

amount_per_person = total_with_tip / amount_of_people

print("Each person should pay:", round(amount_per_person, 2))