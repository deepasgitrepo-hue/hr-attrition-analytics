from faker import Faker
import random

fake = Faker()
departmets = ['Sales','HR','Operations','Marketing']

print ("------Generating 5 Fake Employees------")
print ("Name \t\t Department \t Salary \n")
for i in range(5):
    name = fake.name()
    dept= random.choice(departmets)
    salary = random.randint(50000,120000)

    print(f"{name} \t {dept} \t {salary}")


