# ChildCare
## What is it?

**ChildCare** is a Python library that takes a structured file as data source and provides statistical information about the day care situation. Additionally, data can be queried by year and by type of the care facilities.

## Features

- Importing data from a structured csv file
- Querying data by year
- Querying data by type of care facilities
- Displaying data 

## Prerequisite
Python 3.x

## Where to get it?

The source code is currently hosted on GitHub at: https://github.com/runningturtles/ChildCare  
Binary installers for the latest released version are available at: https://test.pypi.org/project/ChildCare

## How to install it?

Using pip to install the package from TestPyPI:   
`pip install -i https://test.pypi.org/simple/ ChildCare`  

## How to use it?

After installing the Python Package from TestPyPI, you can simply import the library by using:  
`from ChildCare import ChildCare as myChildCare`  
`from ChildCare import ChildCareLib as myChildCareLib`  

Creating an instance of the API with:   
`api = myChildCareLib.ChildCareLib()`  

You can then simply use the interfaces to get your preferred data.  
`api.read_data("demo.csv")`  
`api.show_data(api.filter_by_year("2009"))`  
The interfaces are decribed here: https://github.com/runningturtles/ChildCare/wiki/API-Reference  
Demostration data can be found at: https://github.com/runningturtles/ChildCare/tree/main/Examples  
If you use your own data file, please make sure it has the same structure as the demo file.   
More information about the file structure is available at: https://github.com/runningturtles/ChildCare/wiki/Data-File-Structure
  

## Documentation
Find more information for developers and users at:  
https://github.com/runningturtles/ChildCare/wiki
