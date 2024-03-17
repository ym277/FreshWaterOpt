#!/bin/bash
echo "starting at `date` on `hostname`"

mkdir -p slurm_logs_visualize

mode="max_theta"
# values=(0.29)
values=(0.5 0.6 0.7)

for value in "${values[@]}" 
do
    value_str=$(echo "scale=0; $value * 10 / 1" | bc)
    # value_str="29"
    output_log="slurm_logs_visualize/slurm-%j_e_matrix_${mode}_ab0${value_str}.out"

    echo "sbatch --output="$output_log" --error="$output_log" --job-name=ym_max_theta_ab$value_str  vis.sh $mode $value"
    sbatch --output="$output_log" --error="$output_log" --job-name=ym_max_theta_ab$value_str  vis.sh $mode $value
    sleep 1
done


