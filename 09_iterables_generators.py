class ICanIter:
    def __init__(self):
        self.distros = ["Arch", "Debian", "Ubuntu", "Fedora", "OpenSUSE"]
        self.current = 0
    
    # This just let's Python know it can iterate over instances of this class 
    def __iter__(self):
        return self

    def __next__(self):
        # Need to check and raise so we don't get IndexError instead 
        if self.current >= len(self.distros):
            raise StopIteration

        dist = self.distros[self.current]
        self.current += 1
        return dist

test = ICanIter()
for d in test:
    print(d)

# Can't do, it's at the end 
# print(next(test))

# By having yield, it becomes a generator
def show_me_the_steps(num):
    num *= 2
    yield num
    num += 5
    yield num
    num /= 4
    yield num

print("\nTime for some generation")
gen = show_me_the_steps(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
