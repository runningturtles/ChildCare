# Class ChildCare contains data structure and
# methods to store and modify data about: 
#   - Two different types of care facilities
#   - Number of children supervised by such facilities, 
#     divided into 3 groups:
#       - < 3 years old
#       - between 3 and 6 years old
#       - between 6 and 14 years old
#   - Number of children with Lunches
#   - To which year these numbers are related


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
    # a list of values contained the number of children grouped by ages    
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
        # Checking if category has a valid value,
        # if not, throw an error.
        if (category == "Tageseinrichtung" or category == "Tagespflege"):
            self.category = category
            return 0
        else:
            raise Exception("Type of care facility not allowed.")

    # SET number of kids function verifies firstly  
    # if the input list is valid and then
    # set it to the attribute num_kids;
    # Only X, 0 and positive numbers are allowed.
    # X means information not available
    def set_num_kids(self, num_kids):
        self.num_kids = []
        # Going through the list
        for i in range(len(num_kids)):
            # Striping the string
            num = num_kids[i].strip()
            # Checking if the number of children has a valid value,
            # if not, throw an error.
            if (num.isdigit() or num == "X"):
                self.num_kids.append(num)
            else:
                raise Exception("Only X, 0 and positiv numbers are allowed.") 
        return 0

    # SET number of lunches function verifies   
    # if the input list is valid and then
    # set it to the attribute num_lunches;
    # Only X, 0 and positive numbers are allowed.
    # X means information not available
    def set_num_lunches(self, num_lunches):
        # Striping the string
        num = num_lunches.strip()
        # Checking if the number of children with lunches has a valid value,
        # if not, throw an error.       
        if (num.isdigit() or num == "X"):
            self.num_lunches = num
            return 0
        else:
            raise Exception("Only X, 0 and positiv numbers are allowed.")  
  
    # SET year function verifies   
    # if the input value is valid and then
    # set it to the attribute year;
    # Only 4-digit numbers are allowed.
    def set_year(self, year):
        # Checking if year has a valid value,
        # if not, throw an error.
        if (year.isdigit() and len(year.strip()) == 4):
            self.year = year
            return 0
        else:
            raise Exception("Year has invalid value.")
