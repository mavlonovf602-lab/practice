def calculate(*args):
    print("args", args)
    total = 1
    for x in args:
        total *= x
    print(f" the type value: {type(args)}")
    return total


calculate(2, 3, 4, 5, 6, 7, 8, 9, 77, 77, 65)
print(f"the total value:{total}")
