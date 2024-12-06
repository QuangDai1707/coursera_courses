# Local Machine
## Step 1: download airflow
- pip install apache-airflow
- export AIRFLOW_HOME="~/airflow"
## Step 2: initialize db -> create the db schema
- airflow db init
- airflow db migrate
## Step 3: create admin user
```python
airflow users create \
          --username admin \
          --firstname FIRST_NAME \
          --lastname LAST_NAME \
          --role Admin \
          --email admin@example.org
```
## Start server and scheduler
- airflow webserver -p 8080 & airflow scheduler &

## Run DAG
- submit dag to airflow: 
  - cp accesslog.txt ~/airflow/dags/
- unpause dag:
  - airflow dag unpause process_web_log

## Note:
Schedule monitor all tasks and DAGs, then trigger the task instances once their dependencies are completed.



# Docker
# 1. Pull the Latest Apache Airflow Image
docker pull apache/airflow:latest

# 2. Prepare Necessary Folders
mkdir -p ~/airflow/{dags,logs,plugins}

# 3. Set Environment Variables
export AIRFLOW_UID=$(id -u)  # Use your current user's UID
export AIRFLOW_GID=0        # Use root group ID

# 4. Initialize Airflow
docker run -it --rm \
  -e AIRFLOW_UID=$AIRFLOW_UID \
  -e AIRFLOW_GID=$AIRFLOW_GID \
  -v ~/airflow/dags:/opt/airflow/dags \
  -v ~/airflow/logs:/opt/airflow/logs \
  -v ~/airflow/plugins:/opt/airflow/plugins \
  apache/airflow:latest standalone

# 5. Run the Airflow Webserver
docker run -d \
  -p 8080:8080 \
  --name airflow \
  -e AIRFLOW_UID=$AIRFLOW_UID \
  -e AIRFLOW_GID=$AIRFLOW_GID \
  -v ~/airflow/dags:/opt/airflow/dags \
  -v ~/airflow/logs:/opt/airflow/logs \
  -v ~/airflow/plugins:/opt/airflow/plugins \
  apache/airflow:2.10.3-python3.9 webserver

# 6. Access the Web Interface
http://localhost:8080

