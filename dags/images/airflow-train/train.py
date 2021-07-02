import os
import click
import pickle
import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


@click.command("train")
# @click.option("--input-dir")
# @click.option("--model-dir")

@click.argument("input-dir")
@click.argument("model-dir")

def train_model(input_dir: str, model_dir: str):
    # model = KNeighborsClassifier(n_neighbors=12, weights='distance')
    model = RandomForestClassifier(n_estimators=50, oob_score=True, n_jobs=1)
    df = pd.read_csv(os.path.join(input_dir, "train.csv"), index_col = 0)
    x = df.drop(["target"], axis = 1, inplace = False).values
    y = df["target"].values
    
    model.fit(x, y)
    os.makedirs(model_dir, exist_ok = True)
    with open(os.path.join(model_dir, "model.pkl"), "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    train_model()

