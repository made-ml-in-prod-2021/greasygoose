import os
import click
from sklearn.datasets import load_breast_cancer


@click.command("generate")
# @click.option("--output-dir")
@click.argument("output-dir")

def download(output_dir: str):
    x, y = load_breast_cancer(return_X_y=True, as_frame=True)
    os.makedirs(output_dir, exist_ok=True)
    x.to_csv(os.path.join(output_dir, "features.csv"))
    y.to_csv(os.path.join(output_dir, "target.csv"))


if __name__ == '__main__':
    download()