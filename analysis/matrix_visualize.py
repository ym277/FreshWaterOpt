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

with open('data/data.pkl', 'rb') as f:
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

with open('data/existence_matrix.pkl', 'rb') as f:
    existence_matrix = pkl.load(f)
    sorted_basins = pkl.load(f)
    sorted_species = pkl.load(f)


def plot_e_matrix():
    e_matrix = existence_matrix
    sorted_e_matrix = e_matrix[sorted_basins] # sort rows
    sorted_e_matrix = sorted_e_matrix[:, sorted_species] # sort columns

    sorted_e_matrix = sorted_e_matrix.T

    plt.figure(figsize=(40, 20))

    sns.heatmap(sorted_e_matrix, cmap="Reds", cbar=False, xticklabels=False, yticklabels=False)
    plt.title('Existence Matrix of Species in Basins')
    plt.xlabel('Basins')
    plt.ylabel('Species')
    plt.savefig('visualize/existence_matrix.png')

def plot_sol(sol, value, title):
    sol = np.array([sol[i] for i in range(num_basins)])
    sol = sol*0.5 + 0.5

    colors = ["white", "blue", "red"]
    anchor_points = [0.0, 0.5, 1.0]

    # Create a LinearSegmentedColormap
    custom_cmap = mcolors.LinearSegmentedColormap.from_list("custom_map", list(zip(anchor_points, colors)))

    print(existence_matrix.shape, sol.shape)
    e_matrix = existence_matrix * sol[:, np.newaxis]

    sorted_e_matrix = e_matrix[sorted_basins] # sort rows
    sorted_e_matrix = sorted_e_matrix[:, sorted_species] # sort columns

    sorted_e_matrix = sorted_e_matrix.T

    plt.figure(figsize=(40, 20))  # You can adjust the size to fit your dataset
    sns.heatmap(sorted_e_matrix, cmap=custom_cmap, cbar=False, xticklabels=False, yticklabels=False)

    plt.title(title)
    plt.xlabel('Basins')
    plt.ylabel('Species')
    # plt.savefig('solutions_visualization/'+'solutions{}.jpg'.format())
    red_patch = mpatches.Patch(color='red', label='100% protected')
    blue_patch = mpatches.Patch(color='blue', label='0% protected')
    
    # Add legend to the plot
    plt.legend(handles=[red_patch, blue_patch], loc='upper right')

    plt.savefig(f'visualize/e_matrix_sol_max_theta_ab{str(value).replace(".","")}.png')



def main():
    if len(sys.argv) >= 3:
        mode = sys.argv[1]  # Get the second item in sys.argv as the mode (string)
        try:
            value = float(sys.argv[2])  # Try to convert the third item in sys.argv to a float
        except ValueError:
            print("The second argument must be a float")
            sys.exit(1)
    else:
        print("Usage: matrix_visualize.py <mode> <value>")
        sys.exit(1)

    print("Mode:", mode)
    print("Value:", value)

    if mode == 'max_theta':
        file_path = f'results/max_theta_ab{str(value).replace(".","")}.pkl'
        title =f'Existence Matrix of Species in Basins, colored by solutions when area_bound = {value}, maximizing $\theta$'
    else:
        file_path = f'results/max_totalscore_theta{str(value).replace(".","")}.pkl'
        title =f'Existence Matrix of Species in Basins, colored by solutions when $\theta$ = {value}, maximizing total score'


    with open(file_path, 'rb') as f:
        sol = pkl.load(f)

    plot_sol(sol, value, title)

    # plot_e_matrix()


if __name__ == "__main__":
    main()
    print('finish')