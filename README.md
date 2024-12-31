# CREDIT CARD PROJECT:
The purpose of this project is to carry out a complete Data Analytics process simulating a real case in a professional business. 
The case focuses on a company planning to launch a new credit card with advantageous benefits, specifically targeting the Christmas season.  
For this reason, it needs an analysis to identify which customers might qualify for it. Moreover, I will develop an app that predicts the ideal customer target for this product.   
In addition to addressing this task for the company, I will provide them with an app that, with just a few questions, will indicate whether a customer is the ideal match for this product or not.  

**The first step** is collecting the information from a CSV file created at https://mockaroo.com/.  
I loaded this file into Visual Studio Code to check the data, and I realized an issues:  
  * There were some empty spaces in the 'savings' column. I solved this by filling those spaces with 0.
  * The raw file is [MOCK_DATA.csv](https://github.com/JaviDoria/Credit-Card-Project/tree/main/MOCK_DATA.csv).

__The second step__ in this process is creating the database. I used MySQL to do this.
In the file [Credit_Card_DB.sql](https://github.com/JaviDoria/Credit-Card-Project/tree/main/Credit_Card_DB.sql), you can find the scripts for:

  * Creating the database (credit_card).
  * Creating the table (customers).
  * Loading the data from the CSV file.
  * Some queries to check the database.

**The third step** now that I have a view and can understand the dataset details, is to create a dashboard that facilitates interpreting the data and simplifies decision-making regarding this product.
To face this, I will use Power BI to create the dashboard.


**TEST**

**AHORA HAGO SEGUND COMPROBACIÓN**