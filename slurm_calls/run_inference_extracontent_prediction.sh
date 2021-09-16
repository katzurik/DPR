#!/bin/bash
export TRANSFORMERS_CACHE=/home/joberant/home/urikatz1/hf_cache
/home/joberant/home/urikatz1/anaconda3/bin/python /home/joberant/home/urikatz1/dpr/DPR/dense_retriever.py \
 model_file="/home/joberant/home/urikatz1/dpr/experiments/training/extra_content_gold_dpr_128_ddp_nq/training_output/dpr_biencoder.69"\
 hydra.run.dir="/home/joberant/home/urikatz1/dpr/experiments/training/extra_content_gold_dpr_128_ddp_nq/inference_69/"\
 qa_dataset=strategy_extra_content_predicted_dev \
 ctx_datatsets=[dpr_strategyqa_tsv] \
 encoded_ctx_files=["/home/joberant/home/urikatz1/dpr/experiments/training/extra_content_gold_dpr_128_ddp_nq/dense_embeddings_69/dpr_ctx_*"] \
 out_file="/home/joberant/home/urikatz1/dpr/experiments/training/extra_content_gold_dpr_128_ddp_nq/inference_69/retriever_result_extracontent_predicted.json"
