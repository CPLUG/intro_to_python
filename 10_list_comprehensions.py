lst = [2, 3, 17, 10]
print("Our dear list: {}".format(lst))

new_lst = [x * 2 for x in lst]
print("Our dear list, but 2-upped: {}".format(new_lst))

even_list = [x for x in lst if not x % 2]
print("Our dear list, but only the evens: {}".format(even_list))
