person = ("ffkarim", 60, "female")
name, age, gender = person
print("name:", name)
print("age:", age)
print("gender:", gender)
print("========= ")
print("name, age, gender:", name, age, gender)
students = [
    ("Ali", 85),
    ("Vali", 92),
    ("Guli", 78),
    ("Dilnoza", 95),
    ("Bekzod", 60)
]

for name, score in students:
    print(f"{name} - {score}")
print("====================")
subjeckts = ("math", "physics", "english", "history")
students = ("Ali", "Vali", "Guli", "Dilnoza", "Bekzod")
scores = 85, 92, 78, 95, 60
zipped = zip(students, scores, subjeckts)

print("zipped:", zipped)
result = list(zipped)
print(f"this is students has that results:{result}")
for student, score, subject in zip(students, scores, subjeckts):
    print(f"{student} {subject} fanidan {score} oldi")
