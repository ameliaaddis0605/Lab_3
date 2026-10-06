""" 
Word Count Project    
Amelia Addis 
File analyzer    
10/05/2026 
"""
from pathlib import Path
import string

class WordAnalyzer:
    def __init__(self, filepath): 
        self.__filepath = Path(filepath)
        self.__frequencies = {}
    def process_file(self):
        try:
            if self.__filepath.exists():
                with self.__filepath.open() as open_file:
                for line in open_file:
                    self.__filepath.string.punctuation()
                    self.__filepath.lower()
        except FileNotFoundError:
            return false
            
            
        

        
