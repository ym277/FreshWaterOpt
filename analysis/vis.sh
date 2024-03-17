#!/bin/bash
#SBATCH --partition=aida
#SBATCH --ntasks=1
#SBATCH --time=2:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=128G
 
echo "starting vis at `date` on `hostname`"

# activate conda environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate dam

mode=$1
value=$2

echo "Processing"
which python
echo "python matrix_visualize.py ${mode} ${value}"
python matrix_visualize.py ${mode} ${value}