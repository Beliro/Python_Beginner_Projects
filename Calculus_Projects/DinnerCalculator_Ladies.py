#This program will help to calculate the total dinner cost for ladies, or any other outing
#Accepting user input
num_participants = int(input("Enter the number of participants: "))

#accpetting the bill amount
bill = float(input("Bill amount: "))

#determining the cost per person
cost_per_head = bill // num_participants

#Showing result
print(f"\nAmount to be paid per head: GHC{cost_per_head}")