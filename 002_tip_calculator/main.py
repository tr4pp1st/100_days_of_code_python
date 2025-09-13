# 100 Days of Code: Python
# Day 2 Project: Tip Calculator

print("Welcome to the Tip Calculator")
bill = float(input("Enter the total bill:\n").strip())
tip_in_percent = int(input("How much tip would you like to give? 10, 12, 15 or your own?\n").strip())
count_of_people = int(input("How many people to split the bill?\n").strip())
result = bill * (1 + tip_in_percent/100) / count_of_people

# print(f"Each person should pay: {round(result, 2)}")
print(f"Each person should pay: {result:.2f}")
