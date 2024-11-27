# CREDIT CARD PROJECT:
The purpose of this project is to carry out a complete Data Analytics process simulating a real case in a professional business.  

**The first step** is collecting the information from a CSV file created at https://mockaroo.com/.  
I loaded this file into Visual Studio Code to check the data, and I realized an issues:  
  * There were some empty spaces in the 'savings' column. I solved this by filling those spaces with 0.
  * The raw file is MOCK_DATA.csv.

**The second step** in this process is creating the database. I used MySQL to do this.
In the file Credit_Card_DB.sql, you can find the scripts for:

  * Creating the database (Credit_Card).
  * Creating the table (customers).
  * Loading the data from the CSV file.
  * Some queries to check the database.
