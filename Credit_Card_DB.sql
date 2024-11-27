# 1º CREATING THE DATABASE
CREATE DATABASE credit_card;

# 2º CREATING THE TABLE 'customers'
CREATE TABLE IF NOT EXISTS customers (
id VARCHAR(8) PRIMARY KEY,
first_name VARCHAR(25),
last_name VARCHAR(30),
age INT,
email VARCHAR(50),
gender VARCHAR(6),
marital_status VARCHAR(20),
number_of_children INT,
education_level VARCHAR(25),
job VARCHAR(25),
salary FLOAT(7),
savings FLOAT(20),
housin VARCHAR(3),
current_loans VARCHAR(3),
monthly_expenses FLOAT(7)
) ;

# 3º LOADING THE DATA FROM THE CSV FILE
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\MOCK_DATA.csv'
INTO TABLE customers
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, first_name, last_name, age, email, gender, marital_status, number_of_children, education_level, job, salary, savings, housin, current_loans, monthly_expenses)
;

# 4º CHECKING  THE DATABASE
SELECT * FROM customers;

SELECT ROUND(AVG(SALARY),2) AvgSalary FROM customers;

SELECT COUNT(id) FROM customers
WHERE gender = 'Female' AND marital_status = 'married';

SELECT * FROM customers
WHERE marital_status = 'divorced' AND number_of_children > 3;