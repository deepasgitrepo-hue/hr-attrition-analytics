# Human Resources Information System (HRIS) Data Pipeline & Attrition Analysis

## Business Problem
**Core Challenge:** How can corporate leadership proactively identify and mitigate turnover risks among high-performing, short-tenure staff before it impacts organizational productivity?

This project simulates a modern HR Information System (HRIS) data architecture—mirroring platforms like Workday or BambooHR—to engineer an enterprise data pipeline, model corporate workforce metrics in PostgreSQL, and surface executive insights.

## The Tech Stack & Architecture
1. **Data Generation (Python & Faker):** Simulates a messy, 1,000-row transactional database extracting raw HR tables containing employee profiles, compensation bands, tenure metrics, and exit records.
2. **Data Pipeline ETL (Python & SQLAlchemy):** Programmatically connects to a live PostgreSQL server, staging and transforming raw structures into structured analytical tables.
3. **Data Warehouse Modeling (PostgreSQL):** Utilizes Common Table Expressions (CTEs) and Window Functions to compute operational metrics, rolling attrition velocities, and departmental distributions.
4. **Business Intelligence - Power BI :** Visual tracking of executive high-demand focuses.

## How to Run the Pipeline
Ensure you have PostgreSQL installed locally, then initialize your environment:

```bash
pip install pandas faker psycopg2-binary sqlalchemy
python generate_hr_data.py
python load_to_sql.py