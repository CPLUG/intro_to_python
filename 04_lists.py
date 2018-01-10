# Initialize it
test_list = [1, 2, 3]

# Append 4
test_list.append(4)
# Insert 0 at 0th position
test_list.insert(0, 0)

print("Test list: {}\n".format(test_list))

# Initialize it using its class name
next_list = list()
next_list.append(7)
next_list.append(2)
next_list.append(5)
next_list.append(1)

print("Next list: {}".format(next_list))
print("Sorted next list (does not mutate): {}\n".format(sorted(next_list)))

print("So here's next_list: {}".format(next_list))
if 3 in next_list:
    print("3 is here!")
else:
    print("No 3 :(")

if 2 in next_list:
    print("2 is here!")
else:
    print("No 2 :(")
    
