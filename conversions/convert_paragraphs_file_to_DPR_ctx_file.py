
import json
import csv
import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--paragraphs_file",
        required=True,
        type=str,
        default=None,
        help="Question and paragraphs file of the format detailed in the Readme file",
    )

    parser.add_argument(
        "--out_file",
        required=True,
        type=str,
        default=None,
        help="Evaluator format output path",
    )

    args = parser.parse_args()
    paragraph_file = args.paragraphs_file
    out_path = args.out_path

    if os.path.exists(paragraph_file):
        with open(
                paragraph_file, "r", encoding="utf8"
        ) as f:
            # _paragraphs_cache.update(json.load(f))
            json_list = list(f)

        with open(out_path, 'w', encoding="utf8") as tsvfile:
            writer = csv.writer(tsvfile, delimiter="\t")
            # file format: doc_id, doc_text, title
            writer.writerow(("id", "text", "title"))

            for json_str in json_list:
                item = json.loads(json_str)
                id = f'{item["title"]}-{item["para_id"]}'
                title = item['title']
                text = item["para"]
                writer.writerow((id, text, title))


