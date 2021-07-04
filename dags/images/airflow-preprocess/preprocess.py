import os
import click
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler


@click.command("preprocess")
# @click.option("--input-dir")
# @click.option("--output-dir")
# @click.option("--model-dir")
@click.argument("input-dir")
@click.argument("output-dir")
@click.argument("model-dir")


def preprocess(input_dir: str, output_dir: str, model_dir: str):

    features = pd.read_csv(os.path.join(input_dir, "features.csv"), index_col = 0)
    target = pd.read_csv(os.path.join(input_dir, "target.csv"), index_col = 0)

    cols = features.columns.tolist()
    scaler = StandardScaler()
    features = scaler.fit_transform(features)

    features = pd.DataFrame(features, columns=cols)
    
    df = features.merge(target, right_index = True, left_index = True)
    os.makedirs(output_dir, exist_ok = True)
    df.to_csv(os.path.join(output_dir, "processed_data.csv"))

    os.makedirs(model_dir, exist_ok=True)
    with open(os.path.join(model_dir, "scaler.pkl"), "wb") as f:
        pickle.dump(scaler, f)


if __name__ == '__main__':
    preprocess()