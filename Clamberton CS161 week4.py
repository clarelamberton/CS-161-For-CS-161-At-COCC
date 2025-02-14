def average(num1, num2, num3):
    '''Takes three numbers added up divides by the total amount of number(3) to return their average.'''
    return (num1 + num2 + num3) / 3
print(average(7, 5, 9))
print(average(6, 6, 7))

print (average(7, 5, 9))
print (average(6, 6, 7))
def average(num1, num2, num3):
    '''Takes three numbers added up divides by the total amount of number(3) to return their average.
    Will not run because the def statement is after the print statement
    Therefore it has no way to define the average if the top function that is formatted correctly was deleted from the code
    The code will run when the top function is up there because it is formatted correctly and has the same purpose'''
    return (num1 + num2 + num3)/3

def da_sum(age):
    '''Input of age subtracted by 2 adding 24 then multiplying by 4 to find the dogs age in human years'''
    return 24 +(age - 2 ) * 4
age= int(input("Please input the number for how old your dog is in years without anything else!"))
dogs_age_in_human_years = da_sum(age)
print(f"{age} dog years is equivalent to {dogs_age_in_human_years} human years.")

def car_loss(price_of_car, car_dep, years_h):
    '''Input of price and type of car and associated it with the assigned percentage of depreciation as a decimal and multiplies by number of years to find the value of the car after x years'''
    return price_of_car * (1 - car_dep) ** years_h
car_type = input(f"Input if your car is german, japanese, or italian without capitalization.")
if car_type == "german" or car_type == "italian" :
    car_dep = 0.05
elif car_type == "japanese" :
        car_dep = 0.07
else:
    print("Invalid car type inputted. ")
    exit()
price_of_car = int(input("Initial value of the car $:"))
years_h = int(input("How old is the car in years? "))
depreciation_c = car_loss(price_of_car, car_dep, years_h)
if car_type == "german" :
    print(f"The value of the German car will be ${depreciation_c :.2f} after {years_h} years.")
elif car_type == "italian" :
    print(f"The value of the Italian car will be ${depreciation_c :.2f} after {years_h} years.")
elif car_type == "japanese" :
    print(f"The value of the Japanese car will be ${depreciation_c :.2f} after {years_h} years.")

def d_sum(d_age):
    '''The code takes the decimal of the age input and adds it to 22'''
    return 22 + d_age
d_name = (input(f"Please input your dogs name"))
'''The input will be inputted into d_age to personalize asking how old the users dogs is'''
d_age = int(input(f"How old is {d_name}? ")) / 10
'''The code takes the dogs age and turns it into a decimal'''
i_dog_age_in_human_years = d_sum(d_age)
print(f"Your dog {d_name} is {i_dog_age_in_human_years} human years old.")

def cost_of_ice_cream(number_of_scoops):
    '''The code takes the input of scoops and multiplies it by 1.15 and adds 2.25'''
    return number_of_scoops * 1.15 + 2.25
number_of_scoops = int(input(f"How many scoops of ice cream would you like? "))
price = cost_of_ice_cream(number_of_scoops)
print(f"A {number_of_scoops}-scoop cone of ice cream will cost you ${price:.2f}.")


def average(num1, num2, num3):
    '''The code will not understand that num1 is 7 or 6 depending on which set of numbers therefore it will not run
    these numbers are not defined as a variable they are seen as an input to the definition without being established'''
    return (num1 + num2 + num3) / 3
print(average(7, 5, 9))
print(average(6, 6, 7))
print(num1)
