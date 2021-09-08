
import os
import sys
import json
import csv
import argparse
from pathlib import Path

def creating_question2id_map(mapping_file_path):
    if os.path.exists(mapping_file_path):
        with open(
                mapping_file_path, "r", encoding="utf8"
        ) as f:
            json_list = json.load(f)
        quid_dic = {}
        for json_str in json_list:
            quid_dic[json_str['question']] = json_str['qid']

    return quid_dic


def creating_resulted_dict(retriever_results, quest2id,top_k):
    if os.path.exists(retriever_results):
        with open(
                retriever_results, "r", encoding="utf8"
        ) as f2:
            retriever_res = json.load(f2)
            results_dict = dict()
            has_seen = False
            for res in retriever_res:
                question = res['question']
                #question =  question.rsplit('?', 1)[0]+"?"
                qid = quest2id[question]
                if question == "Can Tulsi Gabbard eat the fries at McDonald's?" and has_seen:
                    qid = "7a4802347e6dd236cb50"
                if question == "Can Tulsi Gabbard eat the fries at McDonald's?" and not has_seen:
                    has_seen = True
                paragraphs = []
                for i in range(top_k):
                    paragraphs.append(res['ctxs'][i]['id'])
                results_dict[qid] = { 'paragraphs': paragraphs }
        return results_dict


def save_json(out_path, json_dict):
    with open(out_path, 'w', encoding="utf8") as f3:
        json.dump(json_dict, f3, indent=4)


if __name__ == "__main__":
    mapping_path = "/Users/uri/Documents/Uri/school/Thesis/Implicit/thesis/DPR/conf/datasets/StrategyQA dataset/modified_data/gold/strategyQA_dev__USE_EVAL_ONLY.json"

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--retriever_output_file",
        required=True,
        type=str,
        default=None,
        help="Question and paragraphs file of the format detailed in the Readme file",
    )

    parser.add_argument(
        "--out_file",
        required=False,
        type=str,
        default=None,
        help="Evaluator format output path",
    )

    parser.add_argument(
        "--top_k",
        required=False,
        type=int,
        default=100,
        help="top k documents",
    )

    args = parser.parse_args()

    quest2id = creating_question2id_map(mapping_path)

    retriever_results = args.retriever_output_file
    out_path = args.out_file
    top_k = args.top_k

    json_dict = creating_resulted_dict(retriever_results, quest2id,top_k)

    if out_path:
        with open(out_path, 'w', encoding="utf8") as f3:
            json.dump(json_dict, f3, indent=4)
    else:
        output_folder = Path(retriever_results).parent
        out_path = output_folder.joinpath('retriever_results_for_evaluation.json')
        with open(out_path, 'w', encoding="utf8") as f3:
            json.dump(json_dict, f3, indent=4)









