small_num = int(input("Input the smaller number:"))
#The user will input 2 numbers the smaller one first than the larger number
large_num = int(input("Input the larger number:"))
print("The even numbers between", small_num, "and", large_num, "are:")
#The program will determine if there are any even numbers between the two inputs and print them
for num in range(small_num, large_num + 1):
    if num % 2 == 0:
        print(num)

numbe = int(input("Input a positive number:"))
#The user will input a number and the program will print out the integers that are factors of the number
print("The integers that are factors of", numbe, "are:")
numb = 1
#The program will determine if the inputted integer is evenly divided by 1 and then increase each number by one to find all the factors
while numb <= numbe:
    if numbe % numb == 0:
        print(numb)
    numb += 1

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
name = input("Input your name: ")
total= 0
for character in name:
#The program will take the input and find the position of each letter in the name
    if "a" <= character <= "z":
        total += ord(character) - ord('a')
#The program will add up each position of the name inputted to print the sum
print("The sum of the position of the letters in", name, "is", total)

n = int(input("Input a positive integer:"))
#The user will input a positive number to plug in for the variable n below
def squares_recursion(n):
    if n > 0:
        squares_recursion(n - 1)
        print(n*n)
#The program will take the input and print the occurrences of the squares results of all the numbers
print("Recursion Results:")
squares_recursion(n)

unsorted = input("Input a unsorted list of numbers seperated with spaces: ")
unsorted_list = list(map(int, unsorted.split()))
#The code will sort numbers into a teepee with the largest number in the middle and the odd numbers in order to the left ascending from center and the even numbers in order to the right descending from center
largest_number = max(unsorted_list)
#The code will then remove the largest number in the set so it does not get repeated in the list
unsorted_list.remove(largest_number)
odd_numbers = sorted(num for num in unsorted_list if num % 2 != 0)
#The code will determine if each number is even or odd
even_numbers = sorted([num for num in unsorted_list if num % 2 == 0], reverse=True)
#The code will then organize all numbers from left to right based on the teepee
teepee =odd_numbers + [largest_number] + even_numbers
print("Teepee:", teepee)

find_next = int(input("Input a number without commas or spaces:"))
#The user will input a value of numbers
def next_largest_number(l):
    digits = list(str(l))
#Turning the number into a list
    length = len(digits)
#find the furthest right decreasing digit
    pivot_i = -1
    for t in range(length - 2, -1, -1):
        if int(digits[t]) < int(digits[t+1]):
            pivot_i = t
            break
#If there is no digit fitting exists the function lets the user know there is no larger value that can be rearranged
    if pivot_i == -1:
        return None
    replacement_i = -1
    # finding the smallest digit on the right of the pivoted that is larger than the pivoted
    for t in range(length - 1, pivot_i, -1):
        if int(digits[t]) > int(digits[pivot_i]):
            replacement_i = t
            break
#the smallest digit on the right on the pivoted number will be swapped with the pivoted number to replace each other
    digits[pivot_i], digits[replacement_i] = digits[replacement_i], digits[pivot_i]
    digits[pivot_i+1:] = sorted(digits[pivot_i+1:])
    return int("".join(digits))
#joining the digits back into an integer from a string

print(next_largest_number(find_next))