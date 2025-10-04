#This program will help to find the remainder of time left from an input of numbers of days
#Accepting user input
days = int(input("Enter number of days: "))

#Remaining time in hours
hours = days * 24

#Remaining time in minutes
minutes = hours * 60

#Remaining time in seconds
seconds = minutes * 60

#Displaying the results to the user
print(f"{days} days is equivalent to {hours} hours, or {minutes} minutes, or {seconds} seconds.")