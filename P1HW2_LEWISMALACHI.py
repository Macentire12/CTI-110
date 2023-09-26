# MALACHI LEWIS
#9/26/2023
#Estimate Travel expenses

budget= int(input("Enter Budget: "))

dest = input("Where are you traveling? ")

gas = int(input("Enter gas Budget: "))

food= int(input("Enter food  budget: "))

hotel = int(input("Enter  hotel  Budget: "))

expenses= gas+food+hotel
print("----------Travel Expeneses------")
print("Location: ", budget)
print("Initial Budget: ", budget)
print()
print("Gas Cost: ",gas)
print("Gas Food: ",food)
print("Gas Hotel: ", hotel)
print()
print("Remaining Balance: ", budget-expenses )
