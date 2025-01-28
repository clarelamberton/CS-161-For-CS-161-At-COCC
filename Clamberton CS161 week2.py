x=31
#print the value of 31 in hexadecimal and binary
y=1.825
#changing the value to find the error
z=18
#changing the value to 18
n = 0b1011
#assigning 2 different hexadecimal values
m = 0xA3
w = z + n + m
#adding the different variables together
original_size = 225
#the original size of the text
dictionary_size = 22
#the size of the dictionary
compressed_text_size = 140
#the compressed text size
perc_1 = 100
# the variable = 100%
total_size= compressed_text_size + dictionary_size
#the sum of the compressed text size and dictionary size

print (x, bin(x), hex(x))
#print the value of 31 in hexadecimal and binary
print (z, bin(z), hex(z))
#changing the value to 18
print (n, m)
#assigning 2 different hexadecimal values to a variable
print ('the sum is ' , w)
#the sum of 18 + both hexadecimal variables
print(f"Compressed text size: {compressed_text_size} characters")
#printing the number of compressed text size characters
print(f"     Dictionary size: {dictionary_size} characters")
#printing the number of dictionary size characters
print(f"               Total: {total_size} characters")
#printing the total numer of compressed text size and dictionary size characters
print(f"  Original text size: {original_size} characters")
#printing the original text size characters
Percent_of_compression = perc_1 - ((compressed_text_size + dictionary_size) / original_size * 100)
#taking the compressed text size and adding the dictionary size then dividing by the original size and multiplying the result by 100 to get a %
print(f"         Compression: {Percent_of_compression}%")
#the value 1.825 in not a whole number therefore it cannot be put into hexadecimal and binary
print (y, bin(y), hex(y))


