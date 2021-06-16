from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

from vars import VOLUME, default_args


with DAG(
        "03_apply_model",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:

    start = DummyOperator(task_id = "Start")
   
    predict = DockerOperator(
        task_id = "predict",
        image = "airflow-predict",
        command = "/data/split/{{ ds }} /data/model/{{ ds }} /data/predictions/{{ ds }}",
        network_mode = "bridge",
        do_xcom_push = False,
        volumes = [VOLUME],
    )
    
    finish = DummyOperator(task_id = "Finish")

    start >> predict >> finish
    
