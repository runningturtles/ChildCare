# Class ChildCareLib provides the interfaces to
# import, query and display data

import os
import re
from . import ChildCare as ChildCare_Class


class ChildCareLib:

	# Initializing ChildCareLib with empty data
	# The entire data from the data source will be stored in this list
	def __init__(self):
		self.datasets = []

	# Reading data from a file
	# If the file doesn't exist, throw an error message,
	# otherwise generate a list of data sets
	def read_data(self, filename):

		# Checking if file exists
		if not os.path.isfile(filename):
			raise Exception("File doesn't exist.")

		# Opening file and reading the contents line by line
		fh = open(filename, 'r')
		count = 0
		while True:
			count += 1 
			# Get next line from file, until a year is detected.
			# If line is empty, end of file is reached.
			line = fh.readline()
			if not line:
				break
			# If the content of the line is a year, then two data sets will be 
			# added into the list, one data set for each care facility type.
			# If a string of a year is found, the next 6 lines should have 
			# structure like this:
			#	1. line: Year
			#	2. line: Total numbers of the children separated by ";"
			#	3. line: Description
			#	4. line: Numbers of children younger than 3 years old separated by ";"
			#	5. line: Numbers of children between 3 and 6 years old separated by ";"
			#	6. line: Numbers of children between 6 and 14 years old separated by ";"
			#	7. line: Numbers of children with lunches separated by ";"
			# If the structure is not corrected, throw an error message.
			if (re.match(r"\d{4}", line.strip())):				
				# Initializing the variables
				cc1 = ChildCare_Class.ChildCare()
				cc2 = ChildCare_Class.ChildCare()
				cc1.set_category("Tageseinrichtung")
				cc2.set_category("Tagespflege")
				year = line.strip()
				num_kids1 = []
				num_kids2 = []
				num_lunches1 = ""
				num_lunches2 = ""
				# Skipping the line about the total number of the kids 
				# Total number of kids can be calculated by the available data.
				line = fh.readline()
				if not line:
					fh.close()
					raise Exception("File structure not correct.")
				# Skipping the line of the description.
				line = fh.readline()
				if not line:
					fh.close()
					raise Exception("File structure not correct.")
				# The next three lines are about the number of children
				# categorized by ages; the fourth line is about the number of
				# children with lunches.
				for i in range(4):
					sp = []
					count += 1
					line = fh.readline()
					if not line:
						fh.close()
						raise Exception("File structure not correct.")
					# Replacing all thousands separators 
					line = line.replace(".", "")
					# Splitting the numbers
					sp = line.split(";")
					# Setting the values to the variables 
					if (i < 3):
						num_kids1.append(sp[1].strip())
						num_kids2.append(sp[2].strip())
					else:
						num_lunches1 = sp[1].strip()
						num_lunches2 = sp[2].strip()
				# Setting values to the data sets
				cc1.set_num_kids(num_kids1)
				cc2.set_num_kids(num_kids2)
				cc1.set_num_lunches(num_lunches1)
				cc2.set_num_lunches(num_lunches2)
				cc1.set_year(year)
				cc2.set_year(year)
				# Adding the data sets to the list
				self.datasets.append(cc1)        
				self.datasets.append(cc2)
		# Closing the file
		fh.close()

		# If no valid data was detected, throw an error.
		if (len(self.datasets) == 0):
			raise Exception("File doesn't contain valid data.")			
		return 0
       
    # Filtering the data sets by year     
	def filter_by_year(self, year):
		# New data instance 
		cc = ChildCare_Class.ChildCare()
		# List to store result
		res = []
		# Going through all data
		for cc in self.datasets:
			# If the data is related to the given year,
			# add it to the result list
			if (str(cc.get_year()) == year):
				res.append(cc)
		# If result list is empty, throw an error message.
		if (len(res) == 0):
			raise Exception("No valid data found.")
		return res

	# Filtering the data sets by category
	def filter_by_category(self, category):
		# New data instance 
		cc = ChildCare_Class.ChildCare()
		# List to store result
		res = []
		# Going through all data
		for cc in self.datasets:
			# If the data is related to the given category,
			# add it to the result list
			if (cc.get_category() == category):
				res.append(cc)
		# If result list is empty, throw an error message.
		if (len(res) == 0):
			raise Exception("No valid data found.")
		return res

	# Printing out data to console
	def show_data(self, data_list):
		# If input list is empty, throw an error message.
		if (len(data_list) == 0):
			raise Exception("No data found.")
		else:
			# New data instance
			cc = ChildCare_Class.ChildCare()
			# Going through the whole data list
			for cc in data_list:
				# Displaying the associated information
				print("Category: " + cc.get_category())
				print("Number of Childern ['<3y', '3-6y', '6-14']:")
				print(cc.get_num_kids())
				print("Number of Lunches: " + cc.get_num_lunches())
				print("Year: " + cc.get_year())
			return 0		
