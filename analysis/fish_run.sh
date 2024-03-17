#!/bin/bash
#SBATCH --partition=aida
#SBATCH --ntasks=1
#SBATCH --time=48:00:00
#SBATCH --cpus-per-task=32
#SBATCH --mem=128G

# Note: you can change the configs in the comments above. They will take effect. For example if you want 64G memory instead of 128G.

echo "starting fish_run at `date` on `hostname`"

# activate conda environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate dam

mode=$1
value=$2

echo "Processing"
which python
echo "python opt.py $mode $value"
python opt.py $mode $value