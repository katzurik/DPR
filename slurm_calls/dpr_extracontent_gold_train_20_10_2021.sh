#!/bin/bash
export TRANSFORMERS_CACHE=/home/joberant/home/urikatz1/hf_cache
/home/joberant/home/urikatz1/anaconda3/bin/python -m torch.distributed.launch --nproc_per_node=6 /home/joberant/home/urikatz1/dpr/DPR/train_dense_encoder.py seed=11818 train_datasets=[strategy_extracontent_gold_train] dev_datasets=[strategy_extracontent_gold_dev] hydra.run.dir='/home/joberant/home/urikatz1/dpr/experiments/training/extra_content_gold_dpr_128_nq_seedb/' output_dir='/home/joberant/home/urikatz1/dpr/experiments/training/extra_content_gold_dpr_128_nq_seedb/training_output/'
