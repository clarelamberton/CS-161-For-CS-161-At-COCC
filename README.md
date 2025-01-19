pet_type = "cat"
#I have a cat named Cleo
pet_gender = "her"
pet_name = "Cleo"
name = input("Enter your first name: ")
#User will input their first name
age = int(input("Enter your current age: "))
#user will input their current age
value = 10
#This is the needed variable to determine the age in 10 years
result= age + value
#calculate the sum
yearly_savings = int(input("Enter your yearly savings:$ "))
#The same user will input the amount they saved over the entire year
monthly_savings = yearly_savings/12
#This is the needed variable to determine the average monthly savings

current_month = (input("Enter which month it is: "))
#The user will input which month it is
x_days = int(input(f"Enter how many days are in the month of {current_month}: "))
#The user will input how many days are in a month
sec_per_day = 60*60*24
#There are 60 seconds in a minute and 60 minutes in an hour there are 24 hours in a day
sec_per_month = x_days*sec_per_day
#The program will run the inputted number of days and multiply it by how many seconds per day there are

number_of_eggs = int(input("Enter how many eggs you have: "))
#The user will input how many eggs they have on hand
if number_of_eggs >= 12:
    dozens_of_eggs = number_of_eggs//12
#The users input will be divided by 12 if they inputted a number over 0
    remaining_eggs = number_of_eggs % 12
#If there is a remainder of eggs after being divided by 12 the program will compute the remainder
else:
    dozens_of_eggs = 0
#If there are less than 12 eggs there cannot be a dozen eggs
    remaining_eggs = number_of_eggs


print(f"I have a {pet_type} and her name is {pet_name}.")
#My data about my cat will be printed out here

print(f"Hello, {name}!")
#The program will print hello and the users name after their input
print(f"You are currently {age} years old.")
#The user will input their age will trigger the program to print their current age
print(f"In ten years, you will be {result}.")
#The program will be triggered to print the users age in ten years based on their inputted data
print(f"If you save ${yearly_savings} each year, in 5 years you will have saved ${yearly_savings*5}.")
#The program will be triggered to print the users input and then multiply it by 5
print(f"Your average monthly savings is ${monthly_savings}")
#The program will be triggered to take the users input and divide by the amount of months in order to figure out the monthly amount saved


print(f"There are {sec_per_month} seconds in the month of {current_month}")
#The program will be triggered to take the users input of how many days and multiply by the number of seconds per day variable

print(f"This makes {dozens_of_eggs} dozen eggs with {remaining_eggs} left over.")
#The program will be triggered to print the users input and then divided by 12 to see how many dozen eggs they have and if they have any leftover
