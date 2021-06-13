import pickle
from typing import Dict, Union

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score # r2_score, mean_squared_error, mean_absolute_error
from sklearn.pipeline import Pipeline

from src.enities.train_params import TrainingParams

SklearnRegressionModel = Union[RandomForestClassifier, KNeighborsClassifier]


def train_model(
    features: pd.DataFrame, target: pd.Series, train_params: TrainingParams
) -> SklearnRegressionModel:
    if train_params.model_type == "RandomForestClassifier":
        model = RandomForestClassifier(
            n_estimators=train_params.model_params['n_estimators'],
            max_depth=train_params.model_params['max_depth'],
            random_state=train_params.random_state
        )
    elif train_params.model_type == "KNeighborsClassifier":
        model = KNeighborsClassifier()
    else:
        raise NotImplementedError()
    model.fit(features, target)
    return model


def predict_model(
    model: Pipeline, features: pd.DataFrame, use_log_trick: bool = True
) -> np.ndarray:
    predicts = model.predict(features)
    if use_log_trick:
        predicts = np.exp(predicts)
    return predicts


def evaluate_model(
    predicts: np.ndarray, target: pd.Series, use_log_trick: bool = False
) -> Dict[str, float]:
    if use_log_trick:
        target = np.exp(target)
    return {
        "accuracy_score": accuracy_score(target, predicts),
        # "r2_score": r2_score(target, predicts),
        # "rmse": mean_squared_error(target, predicts, squared=False),
        # "mae": mean_absolute_error(target, predicts),
    }


def create_inference_pipeline(
    model: SklearnRegressionModel, transformer: ColumnTransformer
) -> Pipeline:
    return Pipeline([("feature_part", transformer), ("model_part", model)])


def serialize_model(model: object, output: str) -> str:
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output
