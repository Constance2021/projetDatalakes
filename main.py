# Load libraries
import pandas as pd
from azure.storage.blob import BlobClient
import os


# instantiation
All_Stock = pd.DataFrame()

# Define parameters
connectionString = "connectionstring"  # find in azure portal
containerName = "output"
outputBlobName = "All_Stock.csv"

# Establish connection with the blob storage account
blob = BlobClient.from_connection_string(
    conn_str=connectionString, container_name=containerName, blob_name=outputBlobName)

# concatener tous les fichiers csv
for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        All_Stock = All_Stock.append(pd.read_csv(file))

# change some columns names for avoiding issues
All_Stock = All_Stock.rename(
    columns={'Open': 'colOpen', 'Close': 'colClose', 'Adj Close': 'Adj_close'})

# Save the result in the file All_Stock.csv
All_Stock.to_csv(outputBlobName, index=False)

if blob.exists():
    print("""""")
else:
    with open(outputBlobName, "rb") as data:
        blob.upload_blob(data)
