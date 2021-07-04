import os
import click
import pickle
import pandas as pd


@click.command("predict")
# @click.option("--input-dir")
# @click.option("--model-dir")
# @click.option("--output-dir")

@click.argument("input-dir")
@click.argument("model-dir")
@click.argument("output-dir")


def predict(input_dir: str, model_dir: str, output_dir: str):

    data = pd.read_csv(os.path.join(input_dir, "features.csv"), index_col = 0)
    with open(os.path.join(model_dir, "model.pkl"), "rb") as f:
        model = pickle.load(f)
    with open(os.path.join(model_dir, "scaler.pkl"), "rb") as f:
        scaler = pickle.load(f)
    
    x = scaler.transform(data)
    preds = model.predict(x)
    preds = pd.DataFrame({'Predictions': preds})
    
    os.makedirs(output_dir, exist_ok = True)
    preds.to_csv(os.path.join(output_dir, "prediction.csv"))


if __name__ == "__main__":
    predict()
