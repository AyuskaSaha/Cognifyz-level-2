import re
from collections import Counter

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

        # Remove punctuation and convert to lowercase
        text = re.sub(r'[^\w\s]', '', text).lower()
        
        # Split the text into words
        words = text.split()
        
        # Count the occurrences of each word
        word_counts = Counter(words)
        
        # Sort the word counts by word (alphabetically)
        sorted_word_counts = dict(sorted(word_counts.items()))

        # Display the results
        for word, count in sorted_word_counts.items():
            print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    count_words(file_path)
