phrase_1 = input("Input a phrase: ")
phrase_caps = input("Input the same phrase in all uppercase: ")
#User will input a phrase and then prompted to enter the same phrase in all caps
if phrase_1.upper() == phrase_caps:
#If the first phrase is the same phrase as the second but the second is in all caps it will tell user to stop shouting
    print("Stop shouting please")

count = 0
#the counter for the vowels is set at 0
ent_st = input("Enter a string: ")
#the user enters a string
if 'a' in ent_st:
    count += 1
if 'e' in ent_st:
    count += 1
if 'i' in ent_st:
    count += 1
if 'o' in ent_st:
    count += 1
if 'u' in ent_st:
    count += 1
if 'y' in ent_st:
    count += 1
#The code will search the string for each vowel and compare and add up the total number of vowels and print them
print(ent_st, "has", count, " different vowels")

wor_1 = input("Input a string: ")
#The user will input 2 strings
wor_2 = input("Input another string: ")
if wor_1 < wor_2:
#If the first string is before the second string in the alphabet it prints that
    print(wor_1, "comes before", wor_2)
elif wor_1 > wor_2:
##If the second string is before the first string in the alphabet it prints that
    print(wor_2, "comes before", wor_1)

email_1 = input("Enter your email address: ")
#User will input an email and then prompted to enter the same email
email_2 = input("Enter your email address again: ")
while email_1 != email_2:
#If the two inputs are not equal it will tell the user they do not match and ask them to reenter them until they match
    print("The two inputs did not match")
    email_1 = input("Enter your email address: ")
    email_2 = input("Enter your email address again: ")
if email_1 == email_2:
#If the first input is equal to the second it will print thank you
    print("Thank you")

import time
#importing time to count how long it takes for both functions
def factorial_recursive(n):
    return 1 if (n==1 or n==0) else n * factorial_recursive(n - 1)
#Recursive function above
def factorial_iterative(n):
    result_2 = 1
    for i in range(1, n + 1):
        result_2 *= i
    return result_2
#Iterative function above
num = int(input("Enter a number: "))
start = time.perf_counter_ns()
result_recursive = factorial_recursive(num)
stop = time.perf_counter_ns()
print("Factorial of",num,"is",result_recursive)
#The code will run and determine the factors for the recursive function and print the number of seconds it took to run and the factorials
print("Time taken (recursive):", stop - start)
#Rest of the iterative function
numb = int(input("Enter a number: "))
start = time.perf_counter_ns()
result_iterative = factorial_iterative(numb)
stop = time.perf_counter_ns()
print("Factorial of",numb,"is", result_iterative)
#The code will run and determine the factors for the iterative function and print the number of seconds it took to run and the factorials
print("Time taken(iterative):", stop - start)
#The recursive function takes longer than the iterative function