#!/bin/bash
export TRANSFORMERS_CACHE=/home/joberant/home/urikatz1/hf_cache
/home/joberant/home/urikatz1/anaconda3/bin/python /home/joberant/home/urikatz1/dpr/DPR/train_dense_encoder.py train_datasets=[strategy_gold_train] dev_datasets=[strategy_gold_dev] output_dir='/home/joberant/home/urikatz1/dpr/experiments/training/gold/training_output/'
