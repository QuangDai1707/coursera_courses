from datetime import timedelta
import datetime as dt
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Claudion Ng',
    'start_date': days_ago(0),
    'email': ['abcasdw@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='process_web_log',
    default_args=default_args,
    description='airflow DAG for analyze data',
    schedule_interval=timedelta(days=1)
)

extract_data = BashOperator(
    task_id='extract_data',
    bash_command='cut -d" " -f1 ~/airflow/dags/accesslog.txt > extract_data.txt',
    dag=dag 
)
transform_data = BashOperator(
    task_id = 'transform_data',
    bash_command='grep -o "198.46.149.143" ~/airflow/dags/extract_data.txt > transformed_data.txt',
    dag=dag
)

load_data = BashOperator(
    task_id = 'load_data',
    bash_command='tar -cvf weblog.tar ~/airflow/dags/transformed_data.txt',
    dag=dag
)

extract_data >> transform_data >> load_data