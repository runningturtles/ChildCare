# Integration Test for Package ChildCare
# Testing if the package and the interfaces work well
# on the target system

from ChildCare import ChildCareLib as myChildCareLib

# Intializing the API
api = myChildCareLib.ChildCareLib()

# Importing data
api.read_data("./Examples/demo.csv")

# Getting data by a given year and 
# comparing the results
data_by_year = api.filter_by_year("2009")
for data in data_by_year:
    if (data.get_category() == "Tageseinrichtung"):
        if (data.get_num_lunches() == "131907"):
            print("Ran 1. test: OK")
        else:
            errmsg = "Ran 1. test: failed\n" + \
                "Number of Lunches shoud be 131907\n" + \
                "But not " + data.get_num_lunches()
            raise Exception(errmsg)

# Getting data by a given category and 
# comparing the results             
data_by_category = api.filter_by_category("Tagespflege")
for data in data_by_category:
    if (data.get_year() == "2019"):
        if (data.get_num_lunches() == "20121"):
            print("Ran 2. test: OK")
        else:
            errmsg = "Ran 2. test: failed\n" + \
                "Number of Lunches shoud be 20121\n" + \
                "But not " + data.get_num_lunches()
            raise Exception(errmsg)
