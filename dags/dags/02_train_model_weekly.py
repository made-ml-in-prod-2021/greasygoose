from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

from vars import VOLUME, default_args


with DAG(
        "02_train_model",
        description="Train model on sklearn dataset",
        default_args=default_args,
        schedule_interval="@weekly",
        start_date=days_ago(5),
) as dag:
    
    start = DummyOperator(task_id = "Start")
    
    preprocess = DockerOperator(
        task_id = "preprocess",
        image = "airflow-preprocess",
        command = "--input-dir /data/raw/{{ ds }} --output-dir /data/processed/{{ ds }} --model_dir /data/model/{{ ds }}",
        network_mode = "bridge",
        do_xcom_push = False,
        volumes = [VOLUME],
    )
    
    split = DockerOperator(
        task_id = "split",
        image = "airflow-split",
        command = "--input-dir /data/processed/{{ ds }} --output-dir /data/split/{{ ds }}",
        network_mode = "bridge",
        do_xcom_push = False,
        volumes=[VOLUME]
    )

    train = DockerOperator(
        task_id = "train",
        image = "airflow-train",
        command = "--input-dir /data/split/{{ ds }} --model-dir /data/model/{{ ds }}",
        network_mode = "bridge",
        do_xcom_push = False,
        volumes=[VOLUME]
    )
    
    validate = DockerOperator(
        task_id = "validate",
        image = "airflow-validate",
        command = "--input-dir /data/split/{{ ds }} --model-dir /data/model/{{ ds }}",
        network_mode = "bridge",
        do_xcom_push = False,
        volumes=[VOLUME]
    )

    finish = DummyOperator(task_id = "Finish")

    start >> preprocess >> split >> train >> validate >> finish
    
