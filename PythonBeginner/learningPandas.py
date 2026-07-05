# raw Python is rarely used 
# Python uses libraries - widely used : Pandas, NumPy
import pandas as pd



hr_columns = ["Employee_ID", "Employee_Name", "Employee_Department", "Employee_Salary"]

hr_data = [
[1000, "A", "HR", 75000],
[1001, "B", "Operation", 100000],
[1002, "C", "sales", 56000]
]

#use pandas library to define dta frame from the raw date .. to make a table
# 2D list like excel row-column - inner list- row , define column name separatley

df = pd.DataFrame(data= hr_data, columns= hr_columns)
print (df)