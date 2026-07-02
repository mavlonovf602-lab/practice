'''functions
(1) Define and call
(2)Parametrs and arguments
(3)keyword and defoult arguments
(4) scope
'''
print("====define and call====")
#################


def greet(a):
    print(f"hello what is your fucking name,{a}")


greet('farrex')
####################


def greet(a):
    print(f"how dod you do,{a}")


def greeting(b):
    print(f"what is your car,{b}")
    return f"hi{b}"


result1 = greet("frrex")
print("result1:", result1)
result2 = greeting("ferrux")
print("result2:", result2)
