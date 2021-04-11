# [START gae_python38_bigquery]
# [START gae_python3_bigquery]
import concurrent.futures

import flask
from google.cloud import bigquery
from google.oauth2.service_account import Credentials
from create_dataset import createDataset
from create_table import createTable
from load import load
from flask import Flask, request, render_template


app = flask.Flask(__name__)
# bigquery_client = bigquery.Client()
bigquery_client = bigquery.Client(project=None, credentials=Credentials.from_service_account_file
            (r"C:\Users\Dell\Desktop\ThS\handy-station-308214-824c524ce43c.json"))


dataset =""


@app.route("/")
def main():
    # dataset =""
    return flask.render_template("query_result.html")

@app.route('/', methods=['POST'])
def my_form_post():
    global dataset
    results = []
    dataset = request.form['text']
    results.append(createDataset(dataset))
    result2 = createTable(dataset)
    results.extend(result2)
    return flask.render_template("query_result.html", results=results)

@app.route('/button')
def button():
    global dataset
    print(dataset)
    loaded = load(dataset)
    return flask.render_template("query_result.html", loaded= loaded, loading = True)

@app.route('/view')
def view():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Do Something':
            print("Do Something")
        elif request.form['submit_button'] == 'Do Something Else':
            print("Do Something Else")
    return flask.render_template("result.html")

# @app.route("/results")
# def results():    
#     project_id = flask.request.args.get("project_id")
#     job_id = flask.request.args.get("job_id")
#     location = flask.request.args.get("location")

#     query_job = bigquery_client.get_job(
#         job_id,
#         project=project_id,
#         location=location,
#     )

#     try:
#         # Set a timeout because queries could take longer than one minute.
#         results = query_job.result(timeout=30)
#     except concurrent.futures.TimeoutError:
#         return flask.render_template("timeout.html", job_id=query_job.job_id)

#     return flask.render_template("query_result.html", results=results)


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)

# [END gae_python3_bigquery]
# [END gae_python38_bigquery]
