
# [START bigquery_query_no_cache]
# import pandas
from google.cloud import bigquery
import matplotlib.pyplot as plt
from time import time

# # We use this helper function to show how much quota a query consumed.
def print_usage(job):
    print('Processed {} bytes, {} MB billed (cache_hit={})'.format(
        job.total_bytes_processed, job.total_bytes_billed / (1024 * 1024), job.cache_hit))

# Construct a BigQuery client object.
client = bigquery.Client()

job_config = bigquery.QueryJobConfig(use_query_cache=True)

sql = """
SELECT
  year,
  country_name,
  ROUND(value,2) AS ratio
FROM
bigquery-public-data.world_bank_health_population.health_nutrition_population
WHERE
  indicator_code = "SP.POP.GROW"
  AND country_name IN ("Vietnam", "China", "India", "Japan", "France")
ORDER BY
  year
"""
tic = time()
query_job = client.query(sql, job_config=job_config)  # Make an API request.
toc = time()
print('Time: {}ms'.format(toc - tic))
df = query_job.to_dataframe()  # Wait for the query to finish, and create a Pandas DataFrame.
# print(df)

df_vn = df.loc[df['country_name'] == "Vietnam"]
df_china = df.loc[df['country_name'] == "China"]
df_india = df.loc[df['country_name'] == "India"]
df_jp = df.loc[df['country_name'] == "Japan"]
df_fran = df.loc[df['country_name'] == "France"]
# print(df_vn)
# print(df_vn['ratio'])

x = list(set(df['year']))
y_vn = df_vn['ratio']
y_china = df_china['ratio']
y_india = df_india['ratio']
y_jp = df_jp['ratio']
y_fran = df_fran['ratio']

plt.plot(x, y_vn, label = "Vietnam")
plt.plot(x, y_china, label = "China")
plt.plot(x, y_india, label = "India")
plt.plot(x, y_jp, label = "Japan")
plt.plot(x, y_fran, label = "France")
plt.legend()
plt.show()

