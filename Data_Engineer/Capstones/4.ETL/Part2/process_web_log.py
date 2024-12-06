from datetime import timedelta
import datetime as dt
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Claudion Ng',
    'start_date': days_ago(0),
    'email': ['abcasdw@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='process_web_log',
    default_args=default_args,
    description='airflow DAG for analyze data',
    schedule_interval=timedelta(days=1)
) as dag: 

    extract_data = BashOperator(
        task_id='extract_data',
        bash_command='cut -d" " -f1 ~/airflow/dags/accesslog.txt > extract_data.txt | ls',
    )
    print_dir1 = BashOperator(
        task_id='print_directory1',
        bash_command='pwd && ls',
    )
    print_dir2 = BashOperator(
        task_id='print_directory2',
        bash_command='pwd && ls',
    )
    print_dir3 = BashOperator(
        task_id='print_directory3',
        bash_command='pwd && ls',
    )
    transform_data = BashOperator(
        task_id = 'transform_data',
        bash_command='grep -o "198.46.149.143" ~/airflow/dags/extract_data.txt > transformed_data.txt',
    )

    load_data = BashOperator(
        task_id = 'load_data',
        bash_command='tar -cvf weblog.tar ~/airflow/dags/transformed_data.txt',
    )

    print_dir1 >> extract_data >> print_dir2 >> transform_data >> print_dir3 >> load_data