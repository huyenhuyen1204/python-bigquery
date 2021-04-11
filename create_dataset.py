
# [START bigquery_create_dataset]
from google.cloud import bigquery
from google.oauth2.service_account import Credentials
from classes import DatasetResult
import json
import time

def createDataset(text):
    client = bigquery.Client(project=None, credentials=Credentials.from_service_account_file
                (r"C:\Users\Dell\Desktop\ThS\handy-station-308214-824c524ce43c.json"))

    print(client.project)
    # dataset: health
    dataset_id_health = "{}.{}".format(client.project, text)
    dataset_health = bigquery.Dataset(dataset_id_health)
    dataset_health.location = "US"
    start_time = time.time()
    dataset_health = client.create_dataset(dataset_health, timeout=30)  # Make an API request.
    
    # project_id=dataset_health.project,
    # job_id=dataset_health.job_id,
    # location=dataset_health.location
    # dataResult = DataResult(project_id,job_id,location)
    
    return "Created dataset \"{}.{}\" - {} seconds".format(client.project, dataset_health.dataset_id, round(time.time() - start_time, 2))

# [END bigquery_create_dataset]
