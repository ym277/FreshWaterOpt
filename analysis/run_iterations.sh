#!/bin/bash
echo "starting at `date` on `hostname`"

mkdir -p slurm_logs

mode="max_theta"
values=(0.18)
#values=(0.18 0.20 0.22 0.24 0.26 0.28 0.30)
# values=(0.1 0.2 0.3 0.4 0.5 0.6)
for value in "${values[@]}" 
do
    value_str=$(echo "scale=0; $value * 100 / 1" | bc)
    output_log="slurm_logs/slurm-%j_iterations_ab0${value_str}.out"

    echo "sbatch --output="$output_log" --error="$output_log" --job-name=smw_iterations_ab$value_str  fish_run.sh $mode $value"
    sbatch --output="$output_log" --error="$output_log" --job-name=smw_iterations_ab$value_str  fish_run.sh $mode $value
    sleep 1
done