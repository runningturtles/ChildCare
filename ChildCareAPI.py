# Class ChildCareAPI
import ChildCare as ChildCare_Class
import re
import os

class ChildCareAPI:
	def __init__(self):
		self.datasets = []

	def read_data(self, filename):
		if not os.path.isfile(filename):
			raise Exception("File doesn't exist.")

		self.filename = filename
		fh = open(filename, 'r')
		count = 0
		while True:
			count += 1 
			# Get next line from file,
			# if line is empty
			# end of file is reached
			line = fh.readline()
			if not line:
				break

			if (re.match(r"\d{4}", line.strip())):
				cc1 = ChildCare_Class.ChildCare()
				cc2 = ChildCare_Class.ChildCare()
				cc1.set_category("Tageseinrichtung")
				cc2.set_category("Tagespflege")

				year = line.strip()
				num_kids1 = []
				num_kids2 = []
				num_lunches1 = ""
				num_lunches2 = ""
				line = fh.readline()
				line = fh.readline()
				for i in range(4):
					sp = []
					count += 1
					line = fh.readline()
					line = line.replace(".", "")
					sp = line.split(";")
					if (i < 3):
						num_kids1.append(sp[1].strip())
						num_kids2.append(sp[2].strip())
					else:
						num_lunches1 = sp[1].strip()
						num_lunches2 = sp[2].strip()
				cc1.set_num_kids(num_kids1)
				cc2.set_num_kids(num_kids2)
				cc1.set_num_lunches(num_lunches1)
				cc2.set_num_lunches(num_lunches2)
				cc1.set_year(year)
				cc2.set_year(year)
				self.datasets.append(cc1)        
				self.datasets.append(cc2)       
		fh.close()
		return 0
       
         
	def filter_by_year(self, year):
		cc = ChildCare_Class.ChildCare()
		res = []
		for cc in self.datasets:
			if (str(cc.get_year()) == year):
				res.append(cc)
		return res

	def filter_by_category(self, category):
		cc = ChildCare_Class.ChildCare()
		res = []
		for cc in self.datasets:
			if (cc.get_category() == category):
				res.append(cc)
		return res
