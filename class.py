class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"{self.name} says: hello! ")

    def say_age(self):
        print(f"{self.name} says i am {self.age} years old.")


person1 = person("farrux", 34)
person2 = person("donni", 34)

print("person1.name:", person1.name)
print("person2.name:", person2.name)

person1.introduce()
person2.say_age()
########################


class car():
    description = " this class makers cars"

    def __new__(cls, *args):
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def start_engine(self):
        print(f"{self.name} engine started")

    def stop_engine(self):
        print(f"{self.name} engine stoppped")


my_car = car("bmw", 2027)
my_car. start_engine()
my_car. stop_engine()
