-- Query 1: The Executive Summary (Total headcount, average salary, and overall attrition rate)
SELECT 
    COUNT(*) as total_headcount,
    ROUND(AVG("Employee_Salary"), 2) as average_salary,
    COUNT(CASE WHEN "Status" = 'InActive' THEN 1 END) as total_attrition,
    ROUND((COUNT(CASE WHEN "Status" = 'InActive' THEN 1 END)::NUMERIC / COUNT(*)) * 100, 2) 
    as attrition_rate
FROM employees;


-- Query 2: Department Breakdown (Which departments are losing the most talent?)
Select "Employee_Department"
as Department,
COUNT(*) as NO_OF_Employees,
COUNT(CASE WHEN "Status" = 'InActive' THEN 1 END) as employees_left,
ROUND((COUNT(CASE WHEN "Status" = 'InActive' THEN 1 END) :: NUMERIC / COUNT(*))*100,2) as department_attriation_rate
FROM employees
GROUP BY "Employee_Department"
ORDER BY department_attriation_rate DESC

