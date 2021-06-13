## **Heart Disease classification**
==============================

Folder contains solution for Heart Disease classification task (https://www.kaggle.com/ronitf/heart-disease-uci).
Solution is based on randomforest model predicting the probability of heart decease relying on patient params.


Installation: 
~~~
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
~~~
Usage:
~~~
python src/train_pipeline.py configs/train_config.yaml
~~~
~~~

Project Organization
------------


    ├── README.md          <- The top-level README for developers using this project.
    ├── dataset            <- Data from third party sources.
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebookswith EDA
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── ml_example                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- code to download or generate data
    │   │
    │   ├── features       <- code to turn raw data into features for modeling
    │   │
    │   ├── models         <- code to train models and then use trained models to make
    │_