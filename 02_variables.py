# Bind the name "secret_num" to the value 5
secret_num = 5

# Save result in user_num
user_num = input("Please give me a number: ")

# Turn user input from a string into an integer
# FIXME: Change "str" to "int" to convert to an integer
user_num = str(user_num)

print(user_num % secret_num)
