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
                    for word in apart:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1
                return True
            else: 
                return False

        except FileNotFoundError:
            return False

        
    def print_report(self):
        sort = sorted(self.__frequencies.keys())
        for word in sort:
            print(f"{word:<10} :: {self.__frequencies[word]}")
def main():
    file = {
        "1": Path("princess.mars.txt"),
        "2": Path("Tarzan.txt"),
        "3": Path("treasure_island.txt"),
        "4": Path("monte_cristo.txt")
    }
    choice = ""
    
    while choice != "5":
        print(f"--- Word Analyzer ---")

        for number, file in file.items():
            print(number, file.stem)

        print("5. Exit")

        print(input("Enter your choice (1-5):"))

