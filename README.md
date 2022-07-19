# projetDatalakes
All resources and services are in the same resource group
for this project i have a a batch account, dabricks, a datafactory, a storage account(within blobs)

main.py is the code for transforming all the csv files in one file by using batch activity and also rename some headers like Open and close that are key word in Azure SQL 

loadinBd.ipynb is for connecting databricks and azure sql database and also for calculating moving average

All_Stock.csv is the file concatenated
