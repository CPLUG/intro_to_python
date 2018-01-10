# Can define the list to loop through here
for x in [1, 5, 9, 2]:
    print("I have a {}".format(x))

# Or loop through an existing object
cool_stuff = [3, 7, 21, 18]

for num in cool_stuff:
    print("This {} is cool stuff".format(num))

# Range is a generator object -- we'll go over that later
for x in range(6):
    print("{} ".format(x), end='')

# Just print a new line
print()

go = True
while go:
    if input("Now type 'c' to continue: ") == "c":
        # Note that even when the condition becomes false, the loop code will continue 
        go = False
    print("Still going!")

while True:
    # We'll leave if the user types q 
    if input("Now type 'q' to quit: ") == "q":
        break
    print("Not done yet!")
