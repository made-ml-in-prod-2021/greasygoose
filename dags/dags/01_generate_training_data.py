from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

from vars import VOLUME, default_args


with DAG(
        "01_generate_train_data",
        description="Generate data via loading sklearn breast cancer dataset",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:
    
    start = DummyOperator(task_id = "start_data_load")
    
    download = DockerOperator(
        task_id = "generate_train_data",
        image = "airflow-generate",
        command = "/data/raw/{{ ds }}",
        network_mode = "bridge",
        do_xcom_push = False,
        volumes = [VOLUME],
    )

    finish = DummyOperator(task_id = "finish_data_load")

    start >> download >> finish
