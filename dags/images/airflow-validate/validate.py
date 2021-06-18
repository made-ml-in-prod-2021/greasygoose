import os
import pickle
import json
import click
import pandas as pd


@click.command("validate")
@click.option("--input-dir")
@click.option("--model-dir")

# @click.argument("input-dir")
# @click.argument("model-dir")

def validate(input_dir: str, model_dir: str):

    val = pd.read_csv(os.path.join(input_dir, "test.csv"), index_col=0)
    x = val.drop(["target"], axis = 1, inplace = False).values
    y = val["target"].values

    with open(os.path.join(model_dir, "model.pkl"), "rb") as f:
        model = pickle.load(f)

    # preds = model.predict(x)
    accuracy = model.score(x, y)

    os.makedirs(model_dir, exist_ok=True)
    with open(os.path.join(model_dir, "model_scores.json"), "w") as f:
        json.dump({"Accuracy" : accuracy}, f)


if __name__ == "__main__":
    validate()
