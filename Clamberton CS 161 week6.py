x = int(input(f"Enter a number: "))
while x > 0:
    if x%2 == 0:
        print(f"{x} is an even number")
    else:
        print(f"{x} is an odd number")
    x = x - 1
print ("blastoff!!")

y = int(input(f"Enter a number: "))
z = int(input(f"Enter the amount of decrease: "))
while y > 0:
    if y % 2 == 0:
        print(f"{y} is an even number")
    else:
        print(f"{y} is an odd number")
    y = y - z
print ("blastoff!!")
wor = input(f"Enter a word: ")
while len(wor) >= 5:
    print(f"{wor} has {len(wor)} letters")
    wor = input(f"Enter a word: ")
if len(wor) < 5:
    print(f"goodbye")
counter = 1
word = input(f"Enter a word: ")
counts = 1
while len(word) >= 5 and counts < 5:
    print(f"{word} has {len(word)} letters")
    word = input(f"Enter a word: ")
    counts += 1
if counts == 5:
    print("loser")
elif len(word) < 5:
    print("goodbye")
count = 10
while count <= 100:
    print(f" {count}  {bin(count)} {hex(count)}")
    count += 1
square_s = int(input(f"Enter a number of stars: "))
def print_stars(square_s):
    while square_s > 0:
        print('*' * square_s)
        square_s -= 1
print_stars(square_s)