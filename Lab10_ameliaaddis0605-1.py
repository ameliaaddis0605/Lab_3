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
                with self.__filepath.open(encoding="utf-8") as open_file:
                 for line in open_file:
                    extra = "“”‘’•"
                    table = str.maketrans("", "",string.punctuation + extra)
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
    files = {
        "1": Path("princess_mars.txt"),
        "2": Path("Tarzan.txt"),
        "3": Path("treasure_island.txt"),
        "4": Path("monte_cristo.txt")
    }
    choice = ""
    
    while choice != "5":
        print(f"\n--- Word Analyzer --- \nPlease select a file to analyze:")

        for number, file in files.items():
            print(f"{number}. {file.stem.replace("_"," ").title()}")

        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice in files:
            print(f"Processing {files[choice].name} ...")
            analyzer = WordAnalyzer(files[choice])

            if analyzer.process_file():
                analyzer.print_report()
            input("Press Enter to return to the menu...")                   
                       
                        
        elif choice == "5":
            print("\nGoodbye!")

        else:
            print("\nInvalid Choice. Please select from 1-5.\n")

            input("Press Enter to return to the menu...")                   
       


        
if __name__ == "__main__":
    main()





