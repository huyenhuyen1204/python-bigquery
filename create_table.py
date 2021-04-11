# [START bigquery_create_table]
from google.cloud import bigquery
from google.oauth2.service_account import Credentials
import json

def createTable(dataset):
    client = bigquery.Client(project=None, credentials=Credentials.from_service_account_file
                        (r"C:\Users\Dell\Desktop\ThS\handy-station-308214-824c524ce43c.json"))

    # Set table_id to the ID of the table to create.
    table_id_health = "handy-station-308214.{}.health_nutrition_population".format(dataset)
    table_id_areas = "handy-station-308214.{}.country_areas".format(dataset)
    table_id_population = "handy-station-308214.{}.country_population".format(dataset)


    # Create fields of health:
    schema_health = [
        bigquery.SchemaField("country_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("country_code", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("indicator_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("indicator_code", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("value", "FLOAT", mode="REQUIRED"),
        bigquery.SchemaField("year", "INTEGER", mode="REQUIRED"),
    ]

    # Create fields of Areas:
    schema_areas = [
        bigquery.SchemaField("country_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("country_code", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("indicator_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("indicator_code", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("year_2018", "FLOAT", mode="NULLABLE"),
    ]

    # Create fields of Population:
    schema_population = [
        bigquery.SchemaField("country_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("country_code", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("indicator_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("indicator_code", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("year_2019", "FLOAT", mode="NULLABLE"),
    ]


    list_results = []
    table_health = bigquery.Table(table_id_health, schema=schema_health)
    table_health = client.create_table(table_health)  # Make an API request.
    print(
        "Created table \"{}.{}.{}\"".format(table_health.project, table_health.dataset_id, table_health.table_id)
    )
    list_results.append("Created table \"{}.{}.{}\"".format(table_health.project, table_health.dataset_id, table_health.table_id))

    table_areas = bigquery.Table(table_id_areas, schema=schema_areas)
    table_areas = client.create_table(table_areas)  # Make an API request.
    print(
        "Created table \"{}.{}.{}\"".format(table_areas.project, table_areas.dataset_id, table_areas.table_id)
    )
    list_results.append("Created table \"{}.{}.{}\"".format(table_areas.project, table_areas.dataset_id, table_areas.table_id))

    table_population = bigquery.Table(table_id_population, schema=schema_population)
    table_population = client.create_table(table_population)  # Make an API request.
    print(
        "Created table \"{}.{}.{}\"".format(table_population.project, table_population.dataset_id, table_population.table_id)
    )
    list_results.append("Created table \"{}.{}.{}\"".format(table_population.project, table_population.dataset_id, table_population.table_id))
    return list_results
    # [END bigquery_create_table]
