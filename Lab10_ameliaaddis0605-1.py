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
                    table = str.maketrans("", "",string.punctuation)
                    line = line.translate(table)
                    line = line.lower()
                    apart = line.split()
        except FileNotFoundError:
            return False
