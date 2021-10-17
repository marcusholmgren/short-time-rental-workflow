#!/usr/bin/env python
"""
Download from Weights & Biases the raw dataset and apply some basic data cleaning,
exporting the result to a new artifact in W&B
"""
import argparse
import logging
import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    ######################
    # YOUR CODE HERE     #
    ######################
    print(f"Hello from basic_cleaning: {args.parameter1}, {args.parameter2}, {args.parameter3}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")

    parser.add_argument(
        "--input_artifact",
        type=str,
        help="the input artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact",
        type=str,
        help="the name for the output artifact",
        required=True
    )

    parser.add_argument(
        "--output_type",
        type=str,
        help="the type for the output artifact",
        required=True
    )

    parser.add_argument(
        "--output_description",
        type=str,
        help="a description for the output artifact",
        required=True
    )

    parser.add_argument(
        "--min_price",
        type=float,
        help="the minimum price to consider",
        required=True
    )

    parser.add_argument(
        "--max_price",
        type=float,
        help="the maximum price to consider",
        required=True
    )


    args = parser.parse_args()

    go(args)
