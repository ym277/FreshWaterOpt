This folder contains the results running LP by gurobi. 

For example, max_theta_ab02.pkl is the result of maximizing theta with area bound = 0.2. It contains two objects, the first one is the lsit of solutions for each basin, and the second one is the max theta.

The LP problem is as the name for each file suggests. 

There are two .out files, which contains the results in text format which has not been processed yet. For example slurm-652197_max_theta_ab03.out is the result of another run for maximizing theta with area bound = 0.3. You can check if the solution there is the same as the result in max_theta_ab03.pkl, to see if the results output by gurobi in the two runs are the same.

!! Be careful when you open .pkl files with 'wb'.
Whenever you call open('xxx.pkl', 'wb'), it will wipe all the current data in the .pkl file immediately, even if you don't call pkl.dump().