# This is likely what the enumerate function looks like
def prolly_pythons_enumerate(iterable):
    curr_index = 0
    for itm in iterable:
        yield (curr_index, itm)
        curr_index += 1

def apply_func(lst, func):
    for i,x in enumerate(lst):
        lst[i] = func(x)

test_lst = [1, 2, 3, 4]
print("Test list before: {}".format(test_lst))

apply_func(test_lst, lambda x: x**2)

print("Test list after: {}".format(test_lst))
