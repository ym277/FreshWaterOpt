#!/bin/bash
#SBATCH --partition=aida
#SBATCH --ntasks=1
#SBATCH --time=48:00:00
#SBATCH --cpus-per-task=32
#SBATCH --mem=100G

# Note: you can change the configs in the comments above. They will take effect. For example if you want 64G memory instead of 128G.

echo "starting dissolve_alt.py at `date` on `hostname`"

# activate conda environment
source ~/miniconda3/etc/profile.d/conda.sh
conda activate dissolve_env

echo "Processing"
which python
echo "python dissolve_alt.py"
python dissolve_alt.py


