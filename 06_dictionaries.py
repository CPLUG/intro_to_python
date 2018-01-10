# Initialize a dictionary
test_dict = {
        "apple": 5,
        "banana": 9,
        }
        
# Store something in it
test_dict["orange"] = 3

# Let's see what's there
print(test_dict)

pin = input("How many pineapples do we need? ")
test_dict["pineapple"] = pin

print(test_dict)

print("\nAnother apple, no banana")
test_dict["apple"] += 1
del test_dict["banana"]

print(test_dict)
