This folder contains the basin data for all basin units and species and their inclusion relations.

!! Be careful when you open .pkl files with 'wb'.
Whenever you call open('xxx.pkl', 'wb'), it will wipe all the current data in the .pkl file immediately, even if you don't call pkl.dump().

Note:
Due to git file size limit, these files were not added to the git repo. You can just access them in the cluster and copy them to your local code base:
/home/fs01/ym277/SouthAmerica/analysis/data/basins_gdf.pkl
/home/fs01/ym277/SouthAmerica/analysis/data/data.pkl
/home/fs01/ym277/SouthAmerica/analysis/data/existence_matrix.pkl
/home/fs01/ym277/SouthAmerica/analysis/data/P.pkl
You should have access to them in the cluster. If not just let me know. 

The .pkl files can be loaded as:

# this is the geodataframe of all basin units. Each line corresponds to a basin unit, containing its basic info and the species in it
with open('basins_gdf.pkl', 'rb') as f:
    basins_gdf = pkl.load(f)

# this contains the python objects storing the basin units and species info. This is probably the main one you need to load if you want to do the analysis in python
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


with open('existence_matrix.pkl', 'rb') as f:
    existence_matrix = pkl.load(f)
    sorted_basins = pkl.load(f)
    sorted_species = pkl.load(f)

with open('P.pkl', 'rb') as f:
    P = pkl.load(f)
    habitat_area_percentage = pkl.load(f)


