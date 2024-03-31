import pandas as pd
import geopandas as gpd

# Read CSV file into DataFrame
df = pd.read_csv("Country-data.csv.xls")  # Replace "Country-data.csv.xls" with your actual file path

# Read world map data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge world map data with the DataFrame based on country names
merged_df = pd.merge(df, world[['name', 'continent', 'geometry']], left_on='country', right_on='name', how='left')

# Extract latitude and longitude from the geometry column
def extract_coordinates(geom):
    if geom:
        return geom.centroid.y, geom.centroid.x
    else:
        return None, None

merged_df['latitude'], merged_df['longitude'] = zip(*merged_df['geometry'].apply(extract_coordinates))

# Drop the redundant 'name' column and geometry column
merged_df.drop(columns=['name', 'geometry'], inplace=True)

# Export the DataFrame to a CSV file in the current working directory
merged_df.to_csv("merged_data_with_coordinates.csv", index=False)

# Print a message indicating successful export
print("DataFrame with latitude and longitude columns exported to 'merged_data_with_coordinates.csv'")
