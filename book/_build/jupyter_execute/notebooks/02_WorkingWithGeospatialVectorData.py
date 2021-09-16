#!/usr/bin/env python
# coding: utf-8

# # Working with geospatial vector data in Python

# In[5]:


import pandas as pd
import geopandas as gpd 
import matplotlib.pyplot as plt 
from shapely.geometry import Point, Polygon, LineString


# In[41]:


# Data adapted from https://en.wikipedia.org/wiki/Divisions_of_Bangladesh
df = pd.DataFrame({
    'city': ['Dhaka', 'Barisal', 'Chittagong', 'Khulna', 'Mymensingh', 'Rajshahi', 'Rangpur', 'Sylhet'], 
    'population': [36433505, 8325666, 29145000, 15687759, 11370000, 18485858, 15787758, 9807000], 
    'area': [20593.74, 13225.20, 33908.55, 22284.22, 10584.06, 18153.08, 16184.99, 12635.22], 
    'latitude': [23.8101, 22.7010, 22.3569,22.8456, 24.7471, 24.3745, 25.7439,24.8949], 
    'longitude': [90.4125, 90.3535, 91.7832, 89.5403, 90.4203, 88.6042,89.2752,91.8687]
})
df 


# In[7]:


# check type 
type(df)


# ## Geometries: Points, Linestrings and Polygons
# 
# Spatial **vector** data can consist of different types, and the 3 fundamental types are:
# 
# ![](../img/simple_features_3_text.svg)
# 
# * **Point** data: represents a single point in space.
# * **Line** data ("LineString"): represents a sequence of points that form a line.
# * **Polygon** data: represents a filled area.
# 
# And each of them can also be combined in multi-part geometries (Reference https://shapely.readthedocs.io/en/stable/manual.html#geometric-objects for extensive overview).

# ### Point 

# In[17]:


# create a point 
p = Point(0, 0)
print(p)


# In[18]:


# check type 
type(p)


# In[27]:


p.geom_type


# In[19]:


# show point
p 


# ### Polygon

# In[23]:


# create polygon 
polygon = Polygon([(1, 1), (2,3), (2, 1)])
print(polygon) 


# In[24]:


type(polygon)


# In[26]:


polygon.geom_type


# In[25]:


# show polygon 
polygon


# ### LineString

# In[37]:


line = LineString([(0, 0), (1, 2)])
print(line)


# In[38]:


line 


# ## General Attributes and Methods

# In[28]:


# distance 
p1 = Point(0, 0)
p2 = Point(1,1)
p1.distance(p2)


# In[29]:


p1.length


# In[30]:


p2.area


# In[31]:


p1.x


# In[32]:


p1.y


# In[36]:


line 


# In[42]:


df['point'] = list(zip(df.longitude, df.latitude))
df 


# In[43]:


df['geometry'] = df['point'].apply(Point)
df 


# ## GeoSeries and GeoDataFrame

# GeoPandas extends two of its main data structures, GeoSeries and GeoDataFrame, from pandas. GeoSeries, much like a pandas Series is a vector in which each entry represents one or more shapes corresponding to a row. GeoDataFrame, much like a pandas DataFrame is a two-dimensional data structure that has a column that is the GeoSeries, along with other information. The GeoSeries column within the GeoDataFrame is referred to as the geometry.

# ### GeoDataFrame
# A GeoDataFrame contains a tabular, geospatial dataset
# 
# * It has a **'geometry' column** that holds the geometry information (or features in GeoJSON).
# * The other columns are the **attributes** (or properties in GeoJSON) that describe each of the geometries
# 
# Such a `GeoDataFrame` is just like a pandas `DataFrame`, but with some additional functionality for working with geospatial data
# 
# * A `.geometry` attribute that always returns the column with the geometry information (returning a GeoSeries). The column name itself does not necessarily need to be 'geometry', but it will always be accessible as the `.geometry` attribute.
# * It has some extra methods for working with spatial data (area, distance, buffer, intersection, ...), which we will see in later notebooks

# In[44]:


# Create GeoDataFrame 
df = df.drop('point', 1)
cities = gpd.GeoDataFrame(df, geometry='geometry')
cities.head() 


# In[46]:


type(cities)


# ### GeoSeries 
# A Series object designed to store shapely geometry objects. General methods and attributes.

# In[47]:


cities['population']


# In[49]:


type(cities.geometry)


# ## Attributes and Methods
# https://geopandas.org/docs/reference.html

# In[50]:


cities['population'].mean()


# In[51]:


cities['area'].min() 


# In[52]:


cities['density'] = cities['population']/cities['area']
cities


# In[53]:


cities.area


# In[55]:


cities.total_bounds


# In[56]:


cities.geom_type


# In[57]:


cities.distance(cities.geometry[0])


# In[58]:


cities2 = cities.copy() 
cities2 = cities2.drop([2, 3])
cities2.head() 


# In[59]:


cities2.area


# In[60]:


cities2.bounds


# In[61]:


cities2.bounds


# In[62]:


cities2.centroid


# In[ ]:





# ## Importing Geospatial Vector Data

# Geospatial data is often available from specific GIS file formats or data stores, like ESRI shapefiles, GeoJSON files, geopackage files, PostGIS (PostgreSQL) database, ...
# 
# We can use the GeoPandas library to read many of those GIS file formats (relying on the `fiona` library under the hood, which is an interface to GDAL/OGR), using the `geopandas.read_file()` function.
# 
# For example, let's start by reading a shapefile with all the countries of the world (adapted from http://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/, zip file is available in the `/data` directory), and inspect the data:

# In[14]:


# read data 
data = gpd.read_file("zip://../data/ne_110m_admin_0_countries.zip")
data.head()


# In[12]:


# reading shape files 
# countries = data = gpd.read_file(r'../shapefiles/world.shp')


# ## Exploring Data 

# In[15]:


# type of dataframe 
type(data)


# In[16]:


# shape 
data.shape 


# In[17]:


# dtypes 
data.dtypes 


# In[18]:


# columns 
data.columns 


# In[19]:


# info 
data.info() 


# In[22]:


data.head() 


# In[21]:


data.plot()
plt.show() 


# What can we observe:
# 
# - Using `.head()` we can see the first rows of the dataset, just like we can do with Pandas.
# - There is a 'geometry' column and the different countries are represented as polygons
# - We can use the `.plot()` method to quickly get a *basic* visualization of the data

# In[23]:


type(data)


# In[24]:


data.geometry


# In[25]:


type(data.geometry)


# In[26]:


data.geometry.area


# **It's still a DataFrame**, so we have all the pandas functionality available to use on the geospatial dataset, and to do data manipulations with the attributes and geometry information together.
# 
# For example, we can calculate average population number over all countries (by accessing the 'pop_est' column, and calling the `mean` method on it):

# In[28]:


data['pop_est'].mean()


# Or, we can use boolean filtering to select a subset of the dataframe based on a condition:

# In[29]:


africa = data[data['continent'] == 'Africa']


# In[30]:


africa.plot()


# ---
# 
# The rest of the tutorial is going to assume you already know some pandas basics, but we will try to give hints for that part for those that are not familiar.   
# A few resources in case you want to learn more about pandas:
# 
# - Pandas docs: https://pandas.pydata.org/pandas-docs/stable/10min.html
# - Other tutorials: chapter from pandas in https://jakevdp.github.io/PythonDataScienceHandbook/, https://github.com/jorisvandenbossche/pandas-tutorial, https://github.com/TomAugspurger/pandas-head-to-tail, ...

# <div class="alert alert-info" style="font-size:120%">
# 
# **REMEMBER:** <br>
# 
# * A `GeoDataFrame` allows to perform typical tabular data analysis together with spatial operations
# * A `GeoDataFrame` (or *Feature Collection*) consists of:
#     * **Geometries** or **features**: the spatial objects
#     * **Attributes** or **properties**: columns with information about each spatial object
# 
# </div>

# 

# For the example we have seen up to now, the individual geometry objects are Polygons:

# In[31]:


print(data.geometry[2])


# Let's import some other datasets with different types of geometry objects.
# 
# A dateset about cities in the world (adapted from http://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-populated-places/, zip file is available in the `/data` directory), consisting of Point data:

# In[15]:


cities = geopandas.read_file("zip://./data/ne_110m_populated_places.zip")


# In[16]:


print(cities.geometry[0])


# And a dataset of rivers in the world (from http://www.naturalearthdata.com/downloads/50m-physical-vectors/50m-rivers-lake-centerlines/, zip file is available in the `/data` directory) where each river is a (multi-)line:

# In[17]:


rivers = geopandas.read_file("zip://./data/ne_50m_rivers_lake_centerlines.zip")


# In[18]:


print(rivers.geometry[0])


# <div class="alert alert-info" style="font-size:120%">
# 
# **REMEMBER**: <br>
# 
# Single geometries are represented by `shapely` objects:
# 
# * If you access a single geometry of a GeoDataFrame, you get a shapely geometry object
# * Those objects have similar functionality as geopandas objects (GeoDataFrame/GeoSeries). For example:
#     * `single_shapely_object.distance(other_point)` -> distance between two points
#     * `geodataframe.distance(other_point)` ->  distance for each point in the geodataframe to the other point
# 
# </div>

# ## Plotting our different layers together

# In[24]:


ax = countries.plot(edgecolor='k', facecolor='none', figsize=(15, 10))
rivers.plot(ax=ax)
cities.plot(ax=ax, color='red')
ax.set(xlim=(-20, 60), ylim=(-40, 40))


# See the [04-more-on-visualization.ipynb](04-more-on-visualization.ipynb) notebook for more details on visualizing geospatial datasets.

# ## Let's practice!
# 
# Throughout the exercises in this course, we will work with several datasets about the city of Paris.
# 
# Here, we start with the following datasets:
# 
# - The administrative districts of Paris (https://opendata.paris.fr/explore/dataset/quartier_paris/): `paris_districts_utm.geojson`
# - Real-time (at the moment I downloaded them ..) information about the public bicycle sharing system in Paris (vélib, https://opendata.paris.fr/explore/dataset/stations-velib-disponibilites-en-temps-reel/information/): `data/paris_bike_stations_mercator.gpkg`
# 
# Both datasets are provided as  files.
# 
# Let's explore those datasets:

# <div class="alert alert-success">
# 
# **EXERCISE**:
# 
# We will start with exploring the bicycle station dataset (available as a GeoPackage file: `data/paris_bike_stations_mercator.gpkg`)
#     
# * Read the stations datasets into a GeoDataFrame called `stations`.
# * Check the type of the returned object (with `type(..)`)
# * Check the first rows of the dataframes. What kind of geometries dooes this datasets contain?
# * How many features are there in the dataset? (hint: use the `.shape` attribute)
#     
# <details><summary>Hints</summary>
# 
# * The geopandas.read_file() function can read different geospatial file formats. You pass the file name as first argument.
# 
# </details>
#     
#     
# </div>

# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data1.py


# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data2.py


# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data3.py


# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data4.py


# <div class="alert alert-success">
# 
# **EXERCISE**:
# 
# * Make a quick plot of the `stations` dataset.
# * Make the plot a bit larger byt setting the figure size to (12, 6) (hint: the `plot` method accepts a `figsize` keyword).
#  
# </div>

# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data5.py


# A plot with just some points can be hard to interpret without any spatial context. Therefore, in the next exercise we will learn how to add a background map.
# 
# We are going to make use of the [contextily](https://github.com/darribas/contextily) package. The `add_basemap()` function of this package makes it easy to add a background web map to our plot. We begin by plotting our data first, and then pass the matplotlib axes object (returned by dataframe's `plot()` method) to the `add_basemap()` function. `contextily` will then download the web tiles needed for the geographical extent of your plot.
# 
# 
# 
# 
# <div class="alert alert-success">
# 
# **EXERCISE**:
# 
# * Import `contextily`.
# * Re-do the figure of the previous exercise: make a plot of all the points in `stations`, but assign the result to an `ax` variable.
# * Set the marker size equal to 5 to reduce the size of the points (use the `markersize` keyword of the `plot()` method for this).
# * Use the `add_basemap()` function of `contextily` to add a background map: the first argument is the matplotlib axes object `ax`.
# 
# </div>

# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data6.py


# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data7.py


# <div class="alert alert-success">
# 
# **EXERCISE**:
# 
# * Make a histogram showing the distribution of the number of bike stands in the stations.
# 
# <details>
#   <summary>Hints</summary>
# 
# * Selecting a column can be done with the square brackets: `df['col_name']`
# * Single columns have a `hist()` method to plot a histogram of its values.
#     
# </details>
#     
# </div>

# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data8.py


# <div class="alert alert-success">
# 
# **EXERCISE**:
# 
# Let's now visualize where the available bikes are actually stationed:
#     
# * Make a plot of the `stations` dataset (also with a (12, 6) figsize).
# * Use the `'available_bikes'` colums to determine the color of the points. For this, use the `column=` keyword.
# * Use the `legend=True` keyword to show a color bar.
#  
# </div>

# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data9.py


# <div class="alert alert-success">
# 
# **EXERCISE**:
# 
# Next, we will explore the dataset on the administrative districts of Paris (available as a GeoJSON file: "data/paris_districts_utm.geojson")
# 
# * Read the dataset into a GeoDataFrame called `districts`.
# * Check the first rows of the dataframe. What kind of geometries does this dataset contain?
# * How many features are there in the dataset? (hint: use the `.shape` attribute)
# * Make a quick plot of the `districts` dataset (set the figure size to (12, 6)).
#     
# </div>

# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data10.py


# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data11.py


# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data12.py


# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data13.py


# <div class="alert alert-success">
# 
# **EXERCISE**:
#     
# What are the largest districts (biggest area)?
# 
# * Calculate the area of each district.
# * Add this area as a new column to the `districts` dataframe.
# * Sort the dataframe by this area column for largest to smallest values (descending).
# 
# <details><summary>Hints</summary>
# 
# * Adding a column can be done by assing values to a column using the same square brackets syntax: `df['new_col'] = values`
# * To sort the rows of a DataFrame, use the `sort_values()` method, specifying the colum to sort on with the `by='col_name'` keyword. Check the help of this method to see how to sort ascending or descending.
# 
# </details>
# 
# </div>

# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data14.py


# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data15.py


# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data16.py


# <div class="alert alert-success">
# 
# **EXERCISE**:
# 
# * Add a column `'population_density'` representing the number of inhabitants per squared kilometer (Note: The area is given in squared meter, so you will need to multiply the result with `10**6`).
# * Plot the districts using the `'population_density'` to color the polygons. For this, use the `column=` keyword.
# * Use the `legend=True` keyword to show a color bar.
# 
# </div>

# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data17.py


# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data18.py


# In[ ]:


# %load _solved/solutions/01-introduction-geospatial-data19.py


# ---
# 
# ## For the curious: A bit more on importing and creating GeoDataFrames

# ### Note on `fiona`
# 
# Under the hood, GeoPandas uses the [Fiona library](http://toblerity.org/fiona/) (pythonic interface to GDAL/OGR) to read and write data. GeoPandas provides a more user-friendly wrapper, which is sufficient for most use cases. But sometimes you want more control, and in that case, to read a file with fiona you can do the following:
# 

# In[ ]:


import fiona
from shapely.geometry import shape

with fiona.Env():
    with fiona.open("zip://./data/ne_110m_admin_0_countries.zip") as collection:
        for feature in collection:
            # ... do something with geometry
            geom = shape(feature['geometry'])
            # ... do something with properties
            print(feature['properties']['name'])


# ### Constructing a GeoDataFrame manually

# In[ ]:


geopandas.GeoDataFrame({
    'geometry': [Point(1, 1), Point(2, 2)],
    'attribute1': [1, 2],
    'attribute2': [0.1, 0.2]})


# ### Creating a GeoDataFrame from an existing dataframe
# 
# For example, if you have lat/lon coordinates in two columns:

# In[ ]:


df = pd.DataFrame(
    {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
     'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
     'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
     'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})


# In[ ]:


gdf = geopandas.GeoDataFrame(
    df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))


# In[ ]:


gdf


# See http://geopandas.readthedocs.io/en/latest/gallery/create_geopandas_from_pandas.html for full example
