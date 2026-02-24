from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="first_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    task_1 = BashOperator(
        task_id="start_task",
        bash_command="echo 'Pipeline Started'"
    )

    task_2 = BashOperator(
        task_id="end_task",
        bash_command="echo 'Pipeline Finished'"
    )

    task_1 >> task_2