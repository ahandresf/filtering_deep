#!/bin/bash
#SBATCH --job-name=qutoek
#SBATCH --gres=gpu:1
#SBATCH -p gpu
#SBATCH --nodelist=gpu4
#SBATCH --output=/home/ahandres/output_diag3.log

time singularity exec -B /lfstev:/lfstev --nv /home/singularity/ML/ubuntu1604-cuda-90-ML-tf1.8.simg python /home/ahandres/img_filter.py
exit
