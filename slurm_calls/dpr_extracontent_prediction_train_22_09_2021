#!/bin/bash
export TRANSFORMERS_CACHE=/home/joberant/home/urikatz1/hf_cache
/home/joberant/home/urikatz1/anaconda3/bin/python -m torch.distributed.launch --nproc_per_node=6 /home/joberant/home/urikatz1/dpr/DPR/train_dense_encoder.py train_datasets=[strategy_predicted_extracontent_train] dev_datasets=[strategy_predicted_extracontent_dev] hydra.run.dir='/home/joberant/home/urikatz1/dpr/experiments/training/predicted_extracontent_dpr_128_ddp_nq/training_output/' output_dir='/home/joberant/home/urikatz1/dpr/experiments/training/predicted_extracontent_dpr_128_ddp_nq/training_output/'
