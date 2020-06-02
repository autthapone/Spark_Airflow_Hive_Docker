from airflow import DAG
from airflow.operators import BashOperator,PythonOperator
from datetime import datetime, timedelta

seven_days_ago = datetime.combine(datetime.today() - timedelta(7),
                                      datetime.min.time())
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': seven_days_ago,
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('load_postgres', default_args=default_args) 

t1 = BashOperator(
    task_id='load_postgres',
    bash_command='python /dags/src/spark_consume_data/pyspark_load_order.py',
    dag=dag
)
