This folder contains the data that have already been processed into python objects, as well as some analysis for them.

Environment requirements:
For python, just install all packages as needed. 
For Gurobi, check the cluster documentation for how to load the license (should just be sth like running 'module load gurobi').

Important files and directories:
- /data and /results: see README in each of them
- opt.py: the python file that actually runs the LP. You can see that it gets executed in the .sh scripts.
- analyze.ipynb: some code for analysis and visualization.
- .sh files (except for vis.sh and run_vis.sh): bash scripts to submit slurm jobs for python scripts to be executed. 
(For the codes take a lot of run-time and memory, we run them in background using slurm jobs, instead of running pythong xx.py or directly in jupyter notebooks. It will be helpful to learn a bit about how to do sbatch.)

Others not so important:
- matrix_visualize.py is the python file to visualize a solution in the (sorted) existence matrix (probably won't need this). 
- /slurm_logs and /slurm_logs_visualize: just the logs for the slurm jobs
- No need to look at process.ipynb unless you find it really necessary, which are some old codes, not yet cleaned.



