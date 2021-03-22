# Unit tests for the ChildCareLib Class
# Valid and invalid tests for each function

import os
import unittest
import ChildCare.ChildCareLib as ChildCareLib_Class


class TestChildCareLib(unittest.TestCase):

    # Valid test for function read_data with 
    # a valid file. Return value should be 0.
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
        # Reading from an empty file should throw an error message
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

        # Reading from this file should throw an error message 
        with self.assertRaises(Exception) as context:
            api.read_data(filename)
        self.assertTrue("File doesn't contain valid data." 
            in str(context.exception))

        # Removing file
        os.remove(filename)

    # Invalid test for function read_data with 
    # an existing file but with incorrect data:
    # Raising error at the first skipped line
    def test_3_read_data(self):
        api = ChildCareLib_Class.ChildCareLib()

        # Creating a file
        filename = "incorrect_data.csv"
        fh = open(filename, "a")
        fh.write("2020")
        fh.close()

        # Reading from this file should throw an error message 
        with self.assertRaises(Exception) as context:
            api.read_data(filename)
        self.assertTrue("File structure not correct." 
            in str(context.exception))

        # Removing file
        os.remove(filename)

    # Invalid test for function read_data with 
    # an existing file but with incorrect data:
    # Raising error at the second skipped line
    def test_4_read_data(self):
        api = ChildCareLib_Class.ChildCareLib()

        # Creating a file
        filename = "incorrect_data.csv"
        fh = open(filename, "a")
        fh.write("2020")
        fh.write("Skipping 1. line: Total number of kids")
        fh.close()

        # Reading from this file should throw an error message 
        with self.assertRaises(Exception) as context:
            api.read_data(filename)
        self.assertTrue("File structure not correct." 
            in str(context.exception))

        # Removing file
        os.remove(filename)

    # Invalid test for function read_data with 
    # an existing file but with incomplete data:
    # Raising error if only a part of data is available
    def test_5_read_data(self):
        api = ChildCareLib_Class.ChildCareLib()

        # Creating a file
        filename = "incorrect_data.csv"
        fh = open(filename, "a")
        fh.write("2020")
        fh.write("Skipping line: Total number of kids")
        fh.write("Skipping line: Description")
        fh.write("Reading line: < 3y: 123;456;789")
        fh.write("Reading line: 3y - 6y: 6123;6456;6789")
        fh.write("Reading line: > 6y: 3230;6450;1209")         
        fh.close()

        # Reading from this file should throw an error message 
        with self.assertRaises(Exception) as context:
            api.read_data(filename)
        self.assertTrue("File structure not correct." 
            in str(context.exception))
            
        # Removing file
        os.remove(filename)

    # Valid test for function filter_by_year with a valid file 
    # Verifying the numbers of children with lunches
    def test_0_filter_by_year(self):
        api = ChildCareLib_Class.ChildCareLib()
        # Reading data
        filename = "./Examples/demo.csv"
        result = api.read_data(filename)
        # Filtering data
        res = api.filter_by_year("2014")
        for i in range(len(res)):
            # Comparing the values of "num_lunches" in both care facility types
            if (res[i].get_category() == "Tageseinrichtung"):
                self.assertEqual(int(res[i].get_num_lunches()), 164786)
            else:
                self.assertEqual(int(res[i].get_num_lunches()), 16519)

    # Invalid test for function filter_by_year with 
    # a valid file. Filtering by an invalid year 2064. 
    def test_1_filter_by_year(self):
        api = ChildCareLib_Class.ChildCareLib()
        # Reading data
        filename = "./Examples/demo.csv"
        result = api.read_data(filename)
        # Filtering data by an invalid value should throw an error
        with self.assertRaises(Exception) as context:
            api.filter_by_year("2064")
        self.assertTrue("No valid data found." 
            in str(context.exception))

    # Valid test for function filter_by_category with a valid file 
    # Verifying the total number of children with lunches over years
    def test_0_filter_by_category(self):
        api = ChildCareLib_Class.ChildCareLib()
        # Reading data
        filename = "./Examples/demo.csv"
        result = api.read_data(filename)
        # Filtering data
        res = api.filter_by_category("Tagespflege")
        # Total number of children with lunches over years
        sum_lunches = 0
        # Going through all the data
        for i in range(len(res)):
            # Summation, but X should be ignored
            if (res[i].get_num_lunches() != "X"):
                sum_lunches = int(res[i].get_num_lunches()) + sum_lunches
        # Comparing the sum
        self.assertEqual(sum_lunches, 194290) 

    # Invalid test for function filter_by_category with 
    # a valid file. Filtering by an invalid category "Tagesmutter". 
    def test_1_filter_by_category(self):
        api = ChildCareLib_Class.ChildCareLib()
        # Reading data
        filename = "./Examples/demo.csv"
        result = api.read_data(filename)
        # Filtering data by an invalid value should throw an error
        with self.assertRaises(Exception) as context:
            api.filter_by_category("Tagesmutter")
        self.assertTrue("No valid data found." 
            in str(context.exception))

    # Valid test for function show_data with 
    # valid data. Return value should be 0.
    def test_0_show_data(self):
        api = ChildCareLib_Class.ChildCareLib()
        # Reading data
        filename = "./Examples/demo.csv"
        api.read_data(filename)
        # Showing data should return 0
        result = api.show_data(api.datasets)
        self.assertEqual(result, 0)

    # Invalid test for function show_data with 
    # empty data
    def test_1_show_data(self):
        api = ChildCareLib_Class.ChildCareLib()
        data_list = []
        # Showing empty data list should throw an error
        with self.assertRaises(Exception) as context:
            api.show_data(data_list)
        self.assertTrue("No data found." 
            in str(context.exception))


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()