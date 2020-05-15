import time
from binary_search_tree import BinarySearchTree
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Currently c^n complextity with a new name adding a new loop
# Replace the nested for loops below with your improvements

sortedNames1 = BinarySearchTree(names_1[0])
for name_1 in names_1[1:]:
    sortedNames1.insert(name_1)
for name_2 in names_2:
    if sortedNames1.contains(name_2):
        duplicates.append(name_2)

# sortedNames1.in_order_print(sortedNames1)

# names_1 = sorted(names_1)
# names_2 = sorted(names_2)
# currentLetter="A"
# names_2_chunk=[]
# names_2_index=0
# for name_2 in names_2:
#     if name_2[0] != currentLetter:

# for name_1 in names_1:
#     if name_1[0] != currentLetter:
#         currentLetter = name_1[0]

#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
