name_input = input ('what is your name?')
#hello users name
print ('Hello ' + name_input)
users_age = int(input("what's your age?"))
#the input wouldn't work before due to the input for age not seen as an integer
print(users_age+5)
year_input = int(input('How many years would you like to add to your age?'))
#user inputs a number of years to see how old they would be in x amount of years
age_from_input = users_age + year_input
#math for how old the user will be with their input to add to their age + current age
age_result = f"In {year_input} years you will be {age_from_input} years old."
#printing how old the user will be in x amount of years
print(age_result)
hours_worked_this_week = input('Enter the number of hours worked this week:')
#the user will enter their hours for the week
hourly_pay = input('Enter your hourly wage, without the $:')
#the user will enter their hourly pay before taxes without a $
float_worked_hours = float(hours_worked_this_week)
#turning these values into floating point values
float_wage = float(hourly_pay)
paycheck_for_this_week= float_worked_hours * float_wage
paycheck_in_money_form = f"{paycheck_for_this_week:.2f}"
#assigning the value to print only 2 digits after the decimal
yearly_pay = paycheck_for_this_week * 52
#assume there are 52 weeks in the year, and the user works the same amount of hours every week
yearly_pay_in_money_form = f"{yearly_pay:.2f}"
#assigning the value to print only 2 digits after the decimal
print(f"Your gross pay this week is $ {paycheck_in_money_form}, your estimated annual gross pay will be $ {yearly_pay_in_money_form}")
#calculated their inputs for their weekly gross paycheck and estimated yearly gross income
