
import json
import csv
import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--qas_file",
        required=True,
        type=str,
        default=None,
        help="Question and file of the format detailed in the Readme file",
    )

    parser.add_argument(
        "--out_file",
        required=True,
        type=str,
        default=None,
        help="Evaluator format output path",
    )

    args = parser.parse_args()
    qas_file = args.qas_file
    out_path = args.out_file

    with open(qas_file) as json_file:
        json_list = json.load(json_file)


        with open(out_path, 'w', encoding="utf8") as tsvfile:
            writer = csv.writer(tsvfile, delimiter="\t")
            #writer = csv.writer(tsvfile, delimiter=" ")
            # file format: doc_id, doc_text, title

            for item in json_list:
                question = item['question']
                answer = [item["answers"]]
                writer.writerow((question, answer))

