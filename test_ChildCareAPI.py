import unittest
import ChildCareAPI as ChildCareAPI_Class

# Unittests for the ChildCareAPI Class
class TestChildCareAPI(unittest.TestCase):
    # New class instance
    api = ChildCareAPI_Class.ChildCareAPI()

    # Valid tests for function read_data with 
    # existing file
    def test_0_read_data(self):
        filename = "rawdata.csv"
        result = self.api.read_data(filename)
        self.assertEqual(result, 0)

    # Invalid tests for function read_data with 
    # none-existing file
    def test_1_read_data(self):
        filename = "vf34g.csv"
        with self.assertRaises(Exception) as context:
            self.api.read_data(filename)
        self.assertTrue("File doesn't exist." 
            in str(context.exception))


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()