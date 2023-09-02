from google.cloud import bigquery
from flask import Flask
from flask import request
import os ,json,logging

app = Flask(__name__)
client = bigquery.Client()

@app.route('/')

def main():
    table_id = "gcp-serverless-397705.udemy_course.us_states" #project id: gcp-serverless-397705
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
    )
    uri = "gs://raw-data-to-bq/us-states/us-states.csv" #bucket name: raw-data-to-bq
    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    ) 

    load_job.result()  

    destination_table = client.get_table(table_id)
    return {"data": destination_table.num_rows}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5052)))