# Unit tests for the ChildCareLib Class
# Valid and invalid tests for each function

import os
import unittest
import ChildCare.ChildCareLib as ChildCareLib_Class


class TestChildCareLib(unittest.TestCase):

    # Valid test for function read_data with 
    # a valid file
    def test_0_read_data(self):
        api = ChildCareLib_Class.ChildCareLib()
        filename = "./Examples/demo.csv"
        result = api.read_data(filename)
        self.assertEqual(result, 0)

    # Invalid test for function read_data with 
    # none-existing file
    def test_1_read_data(self):
        api = ChildCareLib_Class.ChildCareLib()
        filename = "vf34g.csv"
        with self.assertRaises(Exception) as context:
            api.read_data(filename)
        self.assertTrue("File doesn't exist." 
            in str(context.exception))

    # Invalid test for function read_data with 
    # an existing file but without any valid data
    def test_2_read_data(self):
        api = ChildCareLib_Class.ChildCareLib()
        # Touch an empty file
        filename = "fakedata.csv"
        fh = open(filename, "a")
        fh.close()
        # Reading from this file should throw out
        # error message 
        with self.assertRaises(Exception) as context:
            api.read_data(filename)
        self.assertTrue("File doesn't contain any valid data." 
            in str(context.exception))
        # Removing the empty file
        os.remove(filename)

    # Valid test for function filter_by_year with 
    # a valid file 
    def test_0_filter_by_year(self):
        api = ChildCareLib_Class.ChildCareLib()
        filename = "./Examples/demo.csv"
        result = api.read_data(filename)
        res = api.filter_by_year("2014")
        for i in range(len(res)):
            if (res[i].get_category() == "Tageseinrichtung"):
                self.assertEqual(int(res[i].get_num_lunches()), 164786)
            else:
                self.assertEqual(int(res[i].get_num_lunches()), 16519)

    # Invalid test for function filter_by_year with 
    # a valid file. Filtering by an invalid year 2064. 
    def test_1_filter_by_year(self):
        api = ChildCareLib_Class.ChildCareLib()
        filename = "./Examples/demo.csv"
        result = api.read_data(filename)
        with self.assertRaises(Exception) as context:
            api.filter_by_year("2064")
        self.assertTrue("No valid data found." 
            in str(context.exception))

    # Valid test for function filter_by_category with 
    # a valid file 
    def test_0_filter_by_category(self):
        api = ChildCareLib_Class.ChildCareLib()
        filename = "./Examples/demo.csv"
        result = api.read_data(filename)
        res = api.filter_by_category("Tagespflege")
        sum_lunches = 0
        for i in range(len(res)):
            sum_lunches = int(res[i].get_num_lunches()) + sum_lunches
        self.assertEqual(sum_lunches, 194290) 

    # Invalid test for function filter_by_category with 
    # a valid file. Filtering by an invalid category "Tagesmutter". 
    def test_1_filter_by_category(self):
        api = ChildCareLib_Class.ChildCareLib()
        filename = "./Examples/demo.csv"
        result = api.read_data(filename)
        with self.assertRaises(Exception) as context:
            api.filter_by_category("Tagesmutter")
        self.assertTrue("No valid data found." 
            in str(context.exception))

    # Valid test for function show_data with 
    # valid data
    def test_0_show_data(self):
        api = ChildCareLib_Class.ChildCareLib()
        filename = "./Examples/demo.csv"
        api.read_data(filename)
        result = api.show_data(api.datasets)
        self.assertEqual(result, 0)

    # Invalid test for function show_data with 
    # empty data
    def test_1_show_data(self):
        api = ChildCareLib_Class.ChildCareLib()
        data_list = []
        with self.assertRaises(Exception) as context:
            api.show_data(data_list)
        self.assertTrue("No data found." 
            in str(context.exception))


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()