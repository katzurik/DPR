#!/bin/bash
export TRANSFORMERS_CACHE=/home/joberant/home/urikatz1/hf_cache
/home/joberant/home/urikatz1/anaconda3/bin/python /home/joberant/home/urikatz1/dpr/DPR/generate_dense_embeddings.py out_file="/home/joberant/home/urikatz1/dpr/experiments/training/gold_baseline_dpr_128_4g/dense_embeddings/dpr_ctx" ctx_src=dpr_strategyqa_tsv model_file="/home/joberant/home/urikatz1/dpr/experiments/training/gold_baseline_dpr_128_4g/training_output_bsz128/dpr_biencoder.28" batch_size=12000
