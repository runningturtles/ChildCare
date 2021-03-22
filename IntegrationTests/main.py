# Integration Test for Package ChildCare
# Testing if the package and the interfaces work well
# on the target system

from sys import argv
from ChildCare import ChildCareLib as myChildCareLib

# Number of input argument should be 2
if (len(argv) != 2):
    raise Exception("Using: python main.py <path_to_file>")
# The second argument should be the name of the input file
filename = argv[1]

# Intializing the API
api = myChildCareLib.ChildCareLib()

# Importing data
api.read_data(filename)

# Getting data by a given year 
data_by_year = api.filter_by_year("2009")

# Verifying if the results are correct
# Going through all the data related to year "2009"
for data in data_by_year:

    # Finding out how many children had lunches
    # in year "2009" in the care facility "Tageseinrichtung"
    if (data.get_category() == "Tageseinrichtung"):

        # If the number of children with lunches is identical
        # with the original data, test passes.
        if (data.get_num_lunches() == "131907"):
            print("1. Run: OK.")
            print("Year 2009 and Category 'Tageseinrichtung'")
            print("Number of children with lunches: 131907")            
        # Otherwise, test fails.
        else:
            errmsg = "1. Run: failed\n" + \
                "Number of children with lunches shoud be 131907\n" + \
                "But not " + data.get_num_lunches()
            raise Exception(errmsg)

# Getting data by a given category 
data_by_category = api.filter_by_category("Tagespflege")

# Verifying if the results are correct
# Going through all the data related to category "Tagespflege"
for data in data_by_category:

    # Finding out how many children had lunches
    # in year "2019" in the care facility "Tagespflege"
    if (data.get_year() == "2019"):
        
        # If the number of children with lunches is identical
        # with the original data, test passes.
        if (data.get_num_lunches() == "20121"):
            print("2. Run: OK.")
            print("Year 2019 and Category 'Tagespflege'")
            print("Number of children with lunches: 20121")
        # Otherwise, test fails.
        else:
            errmsg = "2. Run: failed\n" + \
                "Number of children with lunches shoud be 20121\n" + \
                "But not " + data.get_num_lunches()
            raise Exception(errmsg)
