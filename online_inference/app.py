import logging
import os
import pickle
from typing import List, Union, Optional

import numpy as np
import pandas as pd
import uvicorn
from fastapi import FastAPI


from pydantic import BaseModel, conlist
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import requests
import datetime
import time

logger = logging.getLogger(__name__)

global SELECTED_FEATURES
SELECTED_FEATURES = {"cat": ["cp", "restecg", "slope"],
                   "num": ["thalach"] }
start_time = datetime.datetime.now()
SLEEP_TIME = 60
CRUSH_TIME = 3*60



def load_object(path: str) -> Pipeline:
    with open(path, "rb") as f:
        return pickle.load(f)

def prepare_data(df: pd.DataFrame) -> np.ndarray:
    cat_cols = SELECTED_FEATURES["cat"]
    num_cols = SELECTED_FEATURES["num"]
    df = df[cat_cols + num_cols]
    df[cat_cols] = df[cat_cols].astype("category")
    transformer = load_object("model/transformer.pkl")
    x = transformer.transform(df)
    return x


class HeartDiseaseModel(BaseModel):
    data: List[conlist(Union[float, None], min_items=4, max_items=40)]
    features: List[str]
    id_: int


class HealthResponse(BaseModel):
    id: int
    isHealty: int


model: Optional[Pipeline] = RandomForestClassifier


def make_predict(
    inp_data: List[Union[float, int, None]], features: List[str], id_: int, model: Pipeline,
) -> List[HealthResponse]:
    data = pd.DataFrame(inp_data).T
    data.columns = features
    x = prepare_data(data)
    predicts = model.predict(x)

    return HealthResponse(id=id_, isHealty=predicts)


app = FastAPI()


@app.get("/")
def main():
    return "it is entry point of our classifier"



@app.on_event("startup")
def load_model():
    time.sleep(SLEEP_TIME)
    global model
    model_path = r"model/model.pkl"
    if model_path is None:
        err = f"PATH_TO_MODEL {model_path} is None"
        logger.error(err)
        raise RuntimeError(err)

    model = load_object(model_path)


@app.get("/health")
def health() -> bool:
    current_delay = datetime.datetime.now() - start_time
    if current_delay.seconds > CRUSH_TIME:
        raise Exception("Application stop")
    return not (model is None)


@app.get("/predict/", response_model=List[HealthResponse])
def predict(request: HeartDiseaseModel):
    return make_predict(request.data, request.features, request.id_, model)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))
    # data = pd.read_csv("test_data.csv")
    # request_features = list(data.columns)
    # for i in range(100):
    #     request_data = [
    #         x.item() if isinstance(x, np.generic) else x for x in data.iloc[i].tolist()
    #     ]
    #     print(request_data)
    #     load_model()
    #     res = make_predict(request_data, request_features, i, model)
    #     res = res.json()