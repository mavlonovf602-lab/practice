# array and set
# array larni faqat intejerlar bilan ishlatilad: array("i", [1,2,3,4,5]) shunaqa qilib
from array import array
numbers = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9])
numbers.append(9)
print("numbers2:", numbers)
numbers.insert(9, 100)
print("numbers2:", numbers)
