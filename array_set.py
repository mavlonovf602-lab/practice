# array and set
# array larni faqat intejerlar bilan ishlatilad: array("i", [1,2,3,4,5]) shunaqa qilib
from array import array
numbers = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9])
numbers.append(9)
print("numbers2:", numbers)
numbers.insert(9, 100)
print("numbers2:", numbers)

print("--------setr-------------")
# set of unique collections without keeping order
new_numbers = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9])
numb_set = set(new_numbers)
print("j:", numb_set)
numb_set.add(101)
print("result:", numb_set)
print("===== set operators =====")
# |, &,-, ^
a = {1, 2, 3, 4, 5, 6, 7}
b = {2, 3, 4, 5, 6, 7, 8, 98, 88, 99}
result1 = a | b  # union
print("union:", result1)
result2 = a & b  # inersaction
print("intersection:", result2)
result3 = a - b  # differance
print("differance:", result3)
result4 = a ^ b  # symmetric differance
print("symmetric differance:", result4)
