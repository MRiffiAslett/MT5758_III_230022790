import os
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def plot_world_map(world, df, column, cmap_colors, save_filename=None):
    """Plots a world map with specified column data."""
    world_data = world.merge(df[['country', column]], how='left', left_on='name', right_on='country')

    # Create a custom colormap
    cmap = LinearSegmentedColormap.from_list('custom', cmap_colors)

    # Plot map with specified column values
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    world_data.plot(column=column, cmap=cmap, linewidth=0.8, ax=ax, edgecolor='black', legend=True)

    # Add title with brackets
    plt.title(f'(MT5758 Assignment III) World {column.capitalize()} Map', fontsize=20)
    
    plt.show()

filepath = "Country-data.csv.xls"

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Read data and append United States
df = read_data(filepath)

# Output directory for saving maps
output_dir = os.getcwd()  # Save maps to current working directory

# Plot and save world map with income values
plot_world_map(world, df, 'income', [(0.9, 0.9, 0.7), (0.5, 0.5, 0.3)])
plot_world_map(world, df, 'life_expec', [(0.1, 0.5, 0.2), (0.6, 0.9, 0.5)])
plot_world_map(world, df, 'gdpp', [(0.6, 0.8, 1), (0.1, 0.3, 0.9)])
