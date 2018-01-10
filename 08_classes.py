class Food:
    # Self is a implicit argument; it has to do with the way Python manages objects at a lower-level 
    def __init__(self, itm, p):
        self.item = itm
        self.price = p

    # As such, you always need self 
    def inflate(self):
        self.price *= 1.02

    # Functions with __ around the name are special builtins that you can override; see Python documentation for more 
    def __str__(self):
        # This is fancy Python 3.6 formatting, only use if you only want to support 3.6+
        return f"{self.item} costs {self.price}"

# Initialize based on the __init__ function, ignore self
apple = Food("Apple", 1)
orange = Food("Orange", 2.49)

# The "self" parameter is passed by calling the function on some object. In this
# case, "apple" is what is passed to self
apple.inflate()
print(apple)

# Java uses getters and setters. Don't do that in Python, just modify it in place
orange.price += 0.5
orange.item = "Blood Orange"
print(orange)
