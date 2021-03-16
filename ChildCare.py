# Class ChildCare contains data structure and
# methods to store and modify information about: 
#   - Two different types of care facilities
#   - Number of kids supervised by such facilities, 
#     divided into 3 levels:
#       - < 3 years old
#       - between 3 and 6 years old
#       - between 6 and 14 years old
#   - Number of kids with Lunches
#   - In which year these numbers are recorded


class ChildCare:
    # Initial attributes with empty values
    def __init__(self):
        self.category = ""
        self.num_kids = []
        self.num_lunches = ""
        self.year = ""

    # GET category function returns 
    # value of the care facility
    def get_category(self):
        return self.category

    # GET number of kids function returns 
    # a list of values contained the number of kids sorted by ages    
    def get_num_kids(self):
        return self.num_kids

    # GET number of lunches function returns 
    # value of lunches 
    def get_num_lunches(self):
        return self.num_lunches

    # GET year function returns 
    # value of the year    
    def get_year(self):
        return self.year

    # SET category function verifies firstly  
    # if the input value is valid and then
    # set it to the attribute category;
    # Only two types of categories are allowed:
    # "Tageseinrichtung" and "Tagespflege"
    def set_category(self, category):
        if (category == "Tageseeinrichtung" or category == "Tagespflege"):
            self.category = category
        else:
            raise Exception("Betreuungsart nicht korrekt.")

    # SET number of kids function verifies firstly  
    # if the input list is valid and then
    # set it to the attribute num_kids;
    # Only X, 0 and positiv numbers are allowed.
    def set_num_kids(self, num_kids):
        self.num_kids = []
        for i in range(len(num_kids)):
            num = num_kids[i].replace("X", "0")
            if (num.isdigit()):
                self.num_kids.append(num)
            else:
                raise Exception("Nur X, 0 und positive Zahlen sind erlaubt.") 

    # SET number of lunches function verifies firstly  
    # if the input value list is valid and then
    # set it to the attribute num_lunches;
    # Only X, 0 and positiv numbers are allowed.
    def set_num_lunches(self, num_lunches):
        num = num_lunches.replace("X", "0")
        if (num.isdigit()):
            self.num_lunches = num
        else:
            raise Exception("Nur X, 0 und positive Zahlen sind erlaubt.")  
  
    # SET year function verifies firstly  
    # if the input value is valid and then
    # set it to the attribute year;
    # Only years between 2007 and 2020 are allowed.
    def set_year(self, year):
        if (year.isdigit()):
            if (int(year) < 2007 or int(year) > 2020):
                raise Exception("Jahr muss zwischen 2007 und 2020 sein.")
            else:
                self.year = year
        else:
            raise Exception("Jahr muss eine Zahl sein.")


    #def get_sum_kids(self):
    #    return sum(self.num_kids)
 
#class ChildCareList:
#    def __init__(self):
#	    self.cclist=[]
#
#    def add_to_list(self, cc):
#	    self.cclist.append(cc)
#	    return self.cclist
#
#   def get_list(self):
#	    return self.cclist

