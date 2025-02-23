any_number = int(input("Enter a number: "))
'''Checking how many times 5 goes into the input if divisible'''
if any_number % 5 == 0:
    print(f"{any_number} is divisible by 5")
else:
    print(f"{any_number} is not divisible by 5")


statedict = {
  "Washington": "Olympia",
  "Oregon": "Salem",
  "Arizona": "Phoenix",
  "Hawaii": "Honolulu",
  "Virginia" : "Richmond",
  "California" : "Sacramento"
}
state_in = input("Input a state: ")
capital = statedict.get(state_in, "I do not know that one")
if state_in == "Washington":
    print("Olympia")
elif state_in == "Oregon":
    print("Salem")
elif state_in == "Arizona":
    print("Phoenix")
elif state_in == "Hawaii":
    print("Honolulu")
elif state_in == "Virginia":
    print("Richmond")
elif state_in == "California":
    print("Sacramento")
else:
    print("I do not know that one")

print(capital)

command= input("Enter a state: ")
match command:
    case "Washington":
        print('Olympia')
    case "Oregon":
        print('Salem')
    case "Arizona":
        print('Phoenix')
    case "Hawaii":
        print('Honolulu')
    case "Virginia":
        print('Richmond')
    case "California":
        print('Sacramento')
    case other:
        print('No match found')


def pool_admission(age):
    '''Program will find price to enter pool based on input'''
    if (age < 2):
        return 0
    elif (age < 12):
        return 3
    elif (age < 60):
        return 6
    elif (age > 60):
        return 4
age = int(input("Enter age: "))
print(f"To enter the public pool it will cost ${pool_admission(age)}.")

with open("coccbobcat.com.html", "r") as file:
    html_content = file.read()
counts = html_content.count("160")

print(f"The substring '160' appears {counts} times in the HTML source of http://coccbobcat.com.")

import psutil
print("Number of running processes:", len(psutil.pids()))