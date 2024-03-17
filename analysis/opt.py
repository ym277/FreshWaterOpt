import matplotlib.pyplot as plt
from pulp import *
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
# import gurobipy
from gurobipy import Model, GRB
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap
import matplotlib.colors as mcolors
import pickle as pkl
import math
from tqdm import tqdm


with open('data.pkl', 'rb') as f:
    basins_info = pkl.load(f)
    protected_basins = pkl.load(f)
    main_to_basin = pkl.load(f)
    num_basins = pkl.load(f)

    species = pkl.load(f)
    species_orig_to_id = pkl.load(f)
    num_species = pkl.load(f)

    basin_species = pkl.load(f)
    species_basin = pkl.load(f)

    num_protected = pkl.load(f)
    total_area = pkl.load(f)
    protected_area = pkl.load(f)

with open('P.pkl', 'rb') as f:
    P = pkl.load(f)
    habitat_area_percentage = pkl.load(f)


non_protected_basins = set(i for i in range(num_basins) if i not in protected_basins) # 124019 basins
min_area_bound = protected_area/total_area # 0.16865753630596783
# area_bound = 0.3


basin_totalscore = np.sum(P, axis=0) # basin id -> total score

def solveLP_max_theta_with_areabound(area_bound):
    m = Model("max theta, fixed area bound")
    vars = {}
    for i in range(num_basins):
        x = m.addVar(vtype=GRB.CONTINUOUS, name="x"+str(i))
        vars[i] = x
        m.addConstr(vars[i] >= (0 if i in non_protected_basins else 1), "c0_"+str(i))
        m.addConstr(vars[i] <= 1, "c1_"+str(i))

    area = sum(basins_info[i]['area'] * vars[i] for i in non_protected_basins)
    max_additional_area = area_bound * total_area - protected_area
    m.addConstr(area <= max_additional_area, name='c_area')
        
    # alternative way
    # area = sum(basins_info[i]['area'] * vars[i] for i in range(num_basins))
    # max_additional_area = area_bound * total_area - protected_area
    # m.addConstr(area <= area_bound * total_area, name='c_area')

    theta = m.addVar(vtype=GRB.CONTINUOUS, name='theta')
    for j in range(num_species):
        score = sum(P[j][i] * vars[i] for i in range(num_basins))
        m.addConstr(score >= theta, 'theta_species_'+str(j))
    m.setObjective(theta, GRB.MAXIMIZE)

    m.optimize()

    sol = {}
    if m.status == GRB.OPTIMAL:
        print('Optimal solution found:')
        for v in m.getVars():
            try:
                i = int(v.varName[1:])
                sol[i] = v.x
                print(f'{v.varName} = {v.x}')
            except:
                pass
    else:
        print('No optimal solution found.')

    return sol, m.ObjVal



def solveLP_fixed_theta_max_totalscore(theta):
    m = Model("max total score, fixed theta (area bound = 0.3)")

    vars = {}
    for i in range(num_basins):
        x = m.addVar(vtype=GRB.CONTINUOUS, name="x"+str(i))
        vars[i] = x
        m.addConstr(vars[i] >= (0 if i in non_protected_basins else 1), "c0_"+str(i))
        m.addConstr(vars[i] <= 1, "c1_"+str(i))

    area = sum(basins_info[i]['area'] * vars[i] for i in non_protected_basins)
    max_additional_area = 0.3 * total_area - protected_area
    m.addConstr(area <= max_additional_area, name='c_area') # area constraint

    for j in range(num_species):
        score = sum(P[j][i] * vars[i] for i in range(num_basins))
        m.addConstr(score >= theta, 'theta_species_'+str(j)) # species score constraint
    
    score = sum(basin_totalscore[i] * vars[i] for i in non_protected_basins)
    m.setObjective(score, GRB.MAXIMIZE)

    m.optimize()

    sol = {}
    if m.status == GRB.OPTIMAL:
        print('Optimal solution found:')
        for v in m.getVars():
            try:
                i = int(v.varName[1:])
                sol[i] = v.x
                print(f'{v.varName} = {v.x}')
            except:
                pass
    else:
        print('No optimal solution found.')

    return sol, m.ObjVal



def main():
    if len(sys.argv) >= 3:
        mode = sys.argv[1]  # Get the second item in sys.argv as the mode (string)
        try:
            value = float(sys.argv[2])  # Try to convert the third item in sys.argv to a float
        except ValueError:
            print("The second argument must be a float")
            sys.exit(1)
    else:
        print("Usage: opt.py <mode> <value>")
        sys.exit(1)

    print("Mode:", mode)
    print("Value:", value)

    if mode == 'max_theta':
        sol_max_theta, max_theta = solveLP_max_theta_with_areabound(value)
        with open(f'results/max_theta_ab{str(value).replace(".","")}.pkl', 'wb') as f:
            pkl.dump(sol_max_theta, f)
            pkl.dump(max_theta, f)
    else:
        sol_max_totalscore, max_totalscore = solveLP_fixed_theta_max_totalscore(value)
        with open(f'results/max_totalscore_theta{str(value).replace(".","")}.pkl', 'wb') as f:
            pkl.dump(sol_max_totalscore, f)
            pkl.dump(max_totalscore, f)

    

if __name__ == "__main__":
    main()