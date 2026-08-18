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
numbers = [1, 2, 3, 4, 5, 54, 3, 32, 1, 3, 4, 3, 2]
set_numbs = {*numbers}
print("setr_numbers:", set_numbs)
dic_people = {person[0]: person[1] for person in people}
print("p---", dic_people)
dic_people1 = {person[0]: person[1] for person in people if person[1] > 23}
print("p---", dic_people1)
