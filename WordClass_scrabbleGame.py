class Word:
    def __init__(self, text):
    
        #Initializes the Word object with a text 

        self.text = text.lower()

    def __lt__(self, other):
        
        #Less-than operator for comparing two Word objects alphabetically.
        #This is useful when sorting or performing binary search.
    
        return self.text < other.text

    def __eq__(self, other):
        
        #Checks if two Word objects are equal
    
        return self.text == other.text

    def __str__(self):
    
        #Returns the string representation of the Word object (the word text itself)
    
        return self.text #end of class
