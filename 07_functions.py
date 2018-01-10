# Define a function that takes 1 argument, called lst
def find_max(lst):
    mx = lst[0]
    for x in lst[1:]:
        if x > mx:
            mx = x
    return mx

lst1 = [1, 1, 1]
lst2 = [30, 1, 2]
lst3 = [1, 5, 9, 7, 3]
lst4 = [6, 9, 30, 340]

print(find_max(lst1))
print(find_max(lst2))
print(find_max(lst3))
print(find_max(lst4))
