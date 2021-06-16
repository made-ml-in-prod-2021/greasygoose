from datetime import timedelta

VOLUME = 'D:/MADE/ML_prod/greasygoose/dags'

default_args = {
        "owner": "greasygoose",
        "email": ["androidegsensation@gmail.com"],
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    }