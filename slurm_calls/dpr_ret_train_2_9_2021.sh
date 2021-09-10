#!/bin/bash
export TRANSFORMERS_CACHE=/home/joberant/home/urikatz1/hf_cache
/home/joberant/home/urikatz1/anaconda3/bin/python -m torch.distributed.launch --nproc_per_node=8 /home/joberant/home/urikatz1/dpr/DPR/train_dense_encoder.py train_datasets=[strategy_gold_train] dev_datasets=[strategy_gold_dev] hydra.run.dir='/home/joberant/home/urikatz1/dpr/experiments/training/gold_baseline_dpr_128_4g_ddp_nq/' output_dir='/home/joberant/home/urikatz1/dpr/experiments/training/gold_baseline_dpr_128_4g_ddp_nq/training_output/'
