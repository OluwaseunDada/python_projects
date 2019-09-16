'''
The following function takes a string parameter and checks if there are exactly three questions marks (???) between any tow numbers that add up to 10
example string_value="arrb6???4xxb15???eee5"
'''
def question_marks(str):    
    try:
        # find the position of '???' in the given string
        position = str.find('???', 0, len(str)) 
    
        # get the values immediately before and after  ???
        val_before = int(str[position - 1])
        val_after = int(str[position + 3]) 

        result = val_before + val_after
        
        if (result == 10):
            return True
        else:
            return False
    except ValueError:
        return False


str="arrb6???4xxb15???eee5"
print(question_marks(str))
