#!/bin/bash
export TRANSFORMERS_CACHE=/home/joberant/home/urikatz1/hf_cache
/home/joberant/home/urikatz1/anaconda3/bin/python /home/joberant/home/urikatz1/dpr/DPR/dense_retriever.py \
 model_file="/home/joberant/home/urikatz1/dpr/DPR/outputs/2021-08-09/23-15-58/output/dpr_biencoder.28"\
 qa_dataset=strategy_gold_dev \
 ctx_datatsets=[dpr_strategyqa_tsv] \
 encoded_ctx_files=["/home/joberant/home/urikatz1/dpr/datasets/strategyqa/embedded_corpus/dpr_ctx_*"] \
 out_file="/home/joberant/home/urikatz1/dpr/experiments/gold/output"
