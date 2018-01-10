print("Hello, and ", end='') # Overrides the normal end of a newline
print("welcome to my cool program!!")

print("Please give me something to turn red:")
print("\033[31m" + input() + "\033[0m")
