import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

#configuration lists
department = ['Sales','HR','Marketing','Operations','Finance']

employee_records= []

print("Generating 1000 records of employees")

for i in range(1000):
    employee_id = 1000+i
    employee_name = fake.name()
    employee_dept = random.choice(department)
    employee_salary = random.randint(45000,150000)
    employee_start_date = fake.date_between(start_date='-8y',end_date='-2y')

#10% employee Attrition
    if random.random() <0.10:
        employee_exit_date = fake.date_between(start_date=employee_start_date,end_date='today')
        status = "InActive"
    else:
        employee_exit_date = None
        status = "Active"

    employee_records.append([employee_id, employee_name, employee_dept, employee_salary, employee_start_date, employee_exit_date, status])

employee_columns = ['Employee_ID', "Employee_Name", "Employee_Department","Employee_Salary", "Employee_Start_Date", "Employee_End_date" ,"Status"]

df = pd.DataFrame(data=employee_records,columns=employee_columns)

print (df.head())

#Export dataframe to csv file
df.to_csv('raw-hr-data.csv',index=False)
