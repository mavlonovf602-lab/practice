print("====number====")
count = 1000
count_type = type(count)
print("count:", count, count_type)
result1 = count.bit_count()
print(result1)
y = input("give me a number for y:")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")
