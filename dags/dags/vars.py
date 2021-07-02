from datetime import timedelta

VOLUME = 'D:/MADE/ML_prod/greasygoose/dags/data/:/data'
DATA_RAW_DIR = r"/data/raw/{{ ds }}"
DATA_PROCESSED_DIR = r"/data/output/{{ ds }}"
MODEL_DIR = r"/data/model/{{ ds }}"
PRED_DIR = r"/data/predictions/{{ ds }}"


default_args = {
        "owner": "greasygoose",
        "email": ["myemail@gmail.com"],
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    }