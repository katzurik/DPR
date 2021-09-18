#!/bin/bash
export TRANSFORMERS_CACHE=/home/joberant/home/urikatz1/hf_cache
/home/joberant/home/urikatz1/anaconda3/bin/python /home/joberant/home/urikatz1/dpr/DPR/dense_retriever.py \
 model_file="/home/joberant/home/urikatz1/dpr/experiments/training/gold_description_dpr_128_ddp_nq/training_output/dpr_biencoder.69"\
 hydra.run.dir="/home/joberant/home/urikatz1/dpr/experiments/training/gold_description_dpr_128_ddp_nq/inference"\
 qa_dataset=strategy_description_dev \
 ctx_datatsets=[dpr_strategyqa_tsv] \
 encoded_ctx_files=["/home/joberant/home/urikatz1/dpr/experiments/training/gold_description_dpr_128_ddp_nq/dense_embeddings/dpr_ctx_*"] \
 out_file="/home/joberant/home/urikatz1/dpr/experiments/training/gold_description_dpr_128_ddp_nq/inference/retriever_result_description.json"
