#!/bin/bash
echo "starting at `date` on `hostname`"

mkdir -p analysis/slurm_logs

output_log="analysis/slurm_logs/slurm-dissolve.out"

echo "sbatch --output="$output_log" --error="$output_log" --job-name=smw_dissolve  dissolve_run.sh"
sbatch --output="$output_log" --error="$output_log" --job-name=smw_dissolve dissolve_run.sh
sleep 1

