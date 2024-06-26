#!/bin/bash
echo "starting at `date` on `hostname`"

mkdir -p slurm_logs

mode="max_theta"
values=(0.18 0.25 0.35)
# values=(0.1 0.2 0.3 0.4 0.5 0.6)
for value in "${values[@]}" 
do
    value_str=$(echo "scale=0; $value * 100 / 1" | bc)
    output_log="slurm_logs/slurm-%j_max_theta_ab0${value_str}.out"

    echo "sbatch --output="$output_log" --error="$output_log" --job-name=ym_max_theta_ab$value_str  fish_run.sh $mode $value"
    sbatch --output="$output_log" --error="$output_log" --job-name=ym_max_theta_ab$value_str  fish_run.sh $mode $value
    sleep 1
done