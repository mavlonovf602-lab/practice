''' comprehensions nima va list camp
set and dictionary comprehension

'''
print("======comrehensions ========")
# comprehension pythondagi spread operatori sifatida ishlatiladi#
# lit comp
people = [("anwar", 23), ("samir", 56)]
list_person = [person[0] for person in people]
print("list_person:", list_person)
list_person = [age[1] for age in people]
print("list_person:", list_person)
cars = [("bmw", 1988),
        ("mers", 1999),
        ("audio", 1888),
        ("ford", 2003)]
old_cars = [car[0] for car in cars if car[1] > 1990]
print("old_cars:", old_cars)
