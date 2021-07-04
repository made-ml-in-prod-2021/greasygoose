import os
import click
import pandas as pd
from sklearn.model_selection import train_test_split


@click.command("split")
# @click.option("--input-dir")
# @click.option("--output-dir")

@click.argument("input-dir")

def split(input_dir: str):
    df = pd.read_csv(os.path.join(input_dir, "processed_data.csv"), index_col=0)
    train, val = train_test_split(df, random_state = 42)

    train.to_csv(os.path.join(input_dir, "train.csv"))
    val.to_csv(os.path.join(input_dir, "test.csv"))


if __name__ == "__main__":
    split()
