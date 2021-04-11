from google.cloud import bigquery
from google.oauth2.service_account import Credentials
import json

def load(text):
    client = bigquery.Client()

    table_id_health = "handy-station-308214.{}.health_nutrition_population".format(text)
    table_id_areas = "handy-station-308214.{}.country_areas".format(text)
    table_id_population = "handy-station-308214.{}.country_population".format(text)

    job_config = bigquery.LoadJobConfig(
        skip_leading_rows=1,
        # The source format defaults to CSV, so the line below is optional.
        source_format=bigquery.SourceFormat.CSV,
    )

    results = []

    uri_health = "gs://huyenhuyen1204/health.csv"
    load_job_health = client.load_table_from_uri(
        uri_health, table_id_health, job_config=job_config
    )  # Make an API request.
    load_job_health.result()  # Waits for the job to complete.
    destination_table_health = client.get_table(table_id_health)
    print("Loaded {} rows.".format(destination_table_health.num_rows))
    results.append("Loaded table \"health_nutrition_population\" - {} rows.".format(destination_table_health.num_rows))

    uri_areas = "gs://huyenhuyen1204/country_areas.csv"
    load_job_areas = client.load_table_from_uri(
        uri_areas, table_id_areas, job_config=job_config
    )  # Make an API request.
    load_job_areas.result()  # Waits for the job to complete.
    destination_table_areas = client.get_table(table_id_areas)
    print("Loaded {} rows.".format(destination_table_areas.num_rows))
    results.append("Loaded table \"country_areas\" - {} rows.".format(destination_table_areas.num_rows))

    uri_population = "gs://huyenhuyen1204/country_population.csv"
    load_job_population = client.load_table_from_uri(
        uri_population, table_id_population, job_config=job_config
    )  # Make an API request.
    load_job_population.result()  # Waits for the job to complete.
    destination_table_population = client.get_table(table_id_population)
    print("Loaded {} rows.".format(destination_table_population.num_rows))
    results.append("Loaded table \"country_population\" - {} rows.".format(destination_table_population.num_rows))
    return results