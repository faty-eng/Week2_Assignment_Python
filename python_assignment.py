my_list = []                          # 1
for value in [10, 20, 30, 40]:       # 2
    my_list.append(value)

my_list.insert(1, 15)                 # 3 (insert 15 at second position -> index 1)
my_list.extend([50, 60, 70])          # 4
my_list.pop()                         # 5 remove last element
my_list.sort()                        # 6 sort ascending

print(my_list)                        # final list
print("Index of 30:", my_list.index(30))  # 7 print index of 30