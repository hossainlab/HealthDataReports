#!/usr/bin/env python
# coding: utf-8

# # Introduction to Geospatial Data 

# Geospatial data refers to any data set that includes information about the geographic location of the record in addition to other features. For example, a data set that contains information about several cities with their population size that also includes two extra columns with the latitude and longitude coordinates is considered geospatial data. Geospatial information is helpful with inferring a lot of extra information, for example, to find the distance between cities, calculate average household incomes by neighborhood, and to create maps.
# 
# Typically, geospatial data is represented in two ways: **vector** data and **raster data**. 

# ## Vector Data
# Vector data is a representation of a spatial element through its x and y coordinates. The most basic form of vector data is a point. Two or more points form a line, and three or more lines form a polygon. The following image shows each type of vector data along with its array representation.
# ![](../img/working-with-data-in-python-1.jpg)

# As an example, you can define the location of a city by a point (x and y coordinates), but in reality the shape of the city contains much more information. There are roads that can be represented by lines, which consist of the two points that represent the start and the end of the line. Also, there are many polygons that represent shapes of any form such as buildings, regions, and city boundaries.

# ### Data Representation
# Vector data can be represented in various formats. The simplest form is to include one or more extra columns in the table that defines its geospatial coordinates. More formal encoding formats such as GeoJSON also come in handy. [GeoJSON](https://geojson.org/), an extension to the [JSON](https://www.json.org/json-en.html) data format, contains a geometry feature that can be a Point, LineString, Polygon, MultiPoint, MultiLineString, or MultiPolygon. There are several other libraries available for representing geospatial data that are all described in the [Geospatial Data Abstraction Library (GDAL)](https://gdal.org/).

# Several GDAL-compatible Python packages have also been developed to make working with geospatial data in Python easier. Points, lines, and polygons can also be described as objects with [Shapely](https://shapely.readthedocs.io/). With these Shapely objects, you can explore spatial relationships such as contains, intersects, overlaps, and touches, as shown in the following figure.
# ![](../img/working-with-data-in-python-2.jpg)

# There are several ways to work with geospatial data using Python. For example, you can use [Fiona](https://pypi.org/project/Fiona/) to load the geometry data and then pass it to Shapely objects. This is what GeoPandas uses. [GeoPandas](https://geopandas.org/) is a package that makes working with vector data a similar experience to working with tabular data using Pandas.

# After you specify the file type (csv, geojson, or a shape file) that contains the geospatial data to GeoPandas, it uses Fiona to get the right format from GDAL. After reading the data using the following code, you have a GeoDataFrame that has all of the geospatial features such as finding the closest point or calculating areas and counting points within a polygon, in addition to the functions of a Pandas DataFrame.

# ## Raster Data
# Raster data is the other type of geospatial data. Raster data is used when spatial information across an area is observed. It consists of a matrix of rows and columns with some information associated with each cell. An example of raster data is a satellite image of a city represented by a matrix that contains the weather information in each of its cells. When you check the rain radar to see whether you need an umbrella, you are looking at this type of data.

# ## Data Representation
# There are several ways that you can work with raster data in Python. One recent package that is user-friendly is [xarray](http://xarray.pydata.org/en/stable/), which reads [netcdf](https://www.unidata.ucar.edu/software/netcdf/docs/faq.html#What-Is-netCDF) files. This is a binary data format consisting of multiple arrays, metadata of the variable names, coordinate systems, raster size, and author of the data. After you load a file as a DataArray, you can create a map with just one command (see the following code), similar to Pandas and GeoPandas.

# ## Coordinate Systems
# For both types of geospatial data, it’s important that you be aware of the coordinate system. Maps are represented on a regular grid of coordinates, but the earth is not a flat rectangle. The transformation of data from the 3-dimensional earth to the 2-dimensional maps is done in many ways, and the process is known as [map projection](https://en.wikipedia.org/wiki/Map_projection). The frequently used [Mercator projection](https://en.wikipedia.org/wiki/Mercator_projection) looks different from the [Mollweide projection](https://en.wikipedia.org/wiki/Mollweide_projection).
# 
# When working with GeoPandas across multiple data sets, it’s important to check whether the projection is the same for all of them. You can do this with the following code.
# 
# 

# When working with raster data, you must be aware of the values that depend on the location of it, which can be either larger at the equator than the poles or the other way around, depending on the projection used.
# 
# 

# In[ ]:




