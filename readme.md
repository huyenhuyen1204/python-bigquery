# Local

env:
Windows
Python > 3.6
Cài đặt virtualenv
Cài đặt Google Cloud Sdk

```
virtualenv windows
windows\Scripts\activate
pip install -r requirements.txt
```

# Deploy to App Engine:

git clone https://github.com/huyenhuyen1204/python-bigquery.git

```
pip install virtualenv
virtualenv ubuntu
source ubuntu/bin/activate
pip install -r requirements.txt
python main.py

gcloud app create
gcloud app deploy app.yaml \
    --project handy-station-308214
```