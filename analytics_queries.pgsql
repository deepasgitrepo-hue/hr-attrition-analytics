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

-- Query 3: 
-- Advanced Analytics: Employee Headcount & Attrition Timeline
WITH monthly_metrics AS (
    SELECT 
        DATE_TRUNC('month', "Employee_Start_Date"::date) as calendar_month,
        COUNT(*) as total_hired,
        COUNT(CASE WHEN "Status" = 'InActive' THEN 1 END) as total_left
    FROM employees
    GROUP BY DATE_TRUNC('month', "Employee_Start_Date"::date)
),
rolling_totals AS (
    SELECT 
        calendar_month,
        total_hired,
        total_left,
        -- WINDOW FUNCTION: Running sum of all employees hired up to this point
        SUM(total_hired) OVER (ORDER BY calendar_month ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as cumulative_hired,
        -- WINDOW FUNCTION: Running sum of all employees who left up to this point
        SUM(total_left) OVER (ORDER BY calendar_month ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as cumulative_left
    FROM monthly_metrics
)
SELECT 
    calendar_month,
    total_hired,
    total_left,
    (cumulative_hired - cumulative_left) as active_headcount,
    ROUND((cumulative_left::NUMERIC / NULLIF(cumulative_hired, 0)) * 100, 2) as rolling_attrition_rate
FROM rolling_totals
ORDER BY calendar_month DESC;