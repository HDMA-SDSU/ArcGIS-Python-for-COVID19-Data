# basic program to convert csv with lat, long to an esri point shapefile.

# modules
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# read csv
df = pd.read_csv('C:/temp/covid_ethnicity.csv')
print(df.head())
print(len(df))

#create geometry from lat, long
geometry = []

for i, row in df.iterrows():
    x = row['Longitude']
    y = row['Latitude']
    geometry.append(Point(x, y))

# spatial reference
crs = {'init': 'epsg:4326'}

# create geodataframe with spatial attributes
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
print(len(gdf))
print(gdf.head())

# export as shapefile
gdf.to_file(driver='ESRI Shapefile', filename ='C:/temp/covid_ethnicity.shp')
