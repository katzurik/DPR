#!/bin/bash
export TRANSFORMERS_CACHE=/home/joberant/home/urikatz1/hf_cache
/home/joberant/home/urikatz1/anaconda3/bin/python /home/joberant/home/urikatz1/dpr/DPR/generate_dense_embeddings.py out_file="/home/joberant/home/urikatz1/dpr/experiments/training/gold_baseline_dpr_128_4g_ddp_nq/dense_embeddings/dpr_ctx" hydra.run.dir="/home/joberant/home/urikatz1/dpr/experiments/training/gold_baseline_dpr_128_4g_ddp_nq/dense_embeddings/" ctx_src=dpr_strategyqa_tsv model_file="/home/joberant/home/urikatz1/dpr/experiments/training/gold_baseline_dpr_128_4g_ddp_nq/training_output/dpr_biencoder.26" shard_id=0 num_shards=6 batch_size=2400



