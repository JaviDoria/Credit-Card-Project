# CREDIT CARD PROJECT:
The purpose of this project is to carry out a complete Data Analytics process simulating a real case in a professional business. 
The case focuses on a company planning to launch a new credit card with advantageous benefits, specifically targeting people with certain financial characteristics.
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

![General Overview](https://github.com/user-attachments/assets/2d56e820-e068-4b53-a463-0ec2ae46e422)
On this page we get an overview of the customers selected for this campaign, such as gender, marital and employment status. These three characteristics can be found on all pages.
In addition, we have some graphs where we can see information about the age and educational level of the customers.
At the top we have some cards that show the total number of available customers, the number of customers who have a home loan, how many have children and the average number of their children.

![Finance Overview](https://github.com/user-attachments/assets/f20e8afc-fffa-47a5-933c-0a66aeef3476)
Finance Overview offer us important information such a how many customers has a positive balance or how many has savings.
Also we can see a comparation of averages from monthly salary vs expenses and a graphic giving us important informations analizing the risky customers who are the ones have housing and personal loan. This is important because we can see that 74.2 % are possible convertions.
Such the first page, we have some cards bringing us information like average monthly expenses, average savings and average monthly salary.

![Family Overview](https://github.com/user-attachments/assets/2439eebb-1a6a-45f8-9797-725498c365b4)


I leave the link if you want to use this dashboard: 
[LINK](https://app.powerbi.com/view?r=eyJrIjoiNjFhOTQzOGItOTNhOS00OWEzLWJiNzAtYWU5ZWVhYTIwYTYwIiwidCI6ImUzM2ExNjJlLWUwZDctNDA3NS05NWQyLWNmNDAyNWI5YWI3ZSIsImMiOjl9&pageName=9ac759e234e0993d8e52)

