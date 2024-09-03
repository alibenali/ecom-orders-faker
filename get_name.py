import csv
import random

def load_csv(file_path):
    """Load the CSV file into a list of tuples (latin_script, arabic_script)."""
    entries = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) == 2:
                entries.append(tuple(row))
    return entries

def get_random_entry(entries, language):
    """Get a random entry from the list based on the language."""
    if language == 'latin':
        column_index = 0
    elif language == 'arabic':
        column_index = 1
    else:
        raise ValueError("Language must be 'latin' or 'arabic'")
    
    entry = random.choice(entries)
    return entry[column_index]

def random_name(language):
    names_entries = load_csv('names_full_dataset.csv')
    """Get a random name in the specified language."""
    return get_random_entry(names_entries, language)

def random_surname(language):
    surnames_entries = load_csv('surnames_full_dataset.csv')
    """Get a random surname in the specified language."""
    return get_random_entry(surnames_entries, language)




# randomly choose arabic or latin
def random_language():
    return random.choice(['arabic', 'latin'])

# get random name and surname
def random_name_and_surname(language):
    if language == 'arabic':
        return random_name('arabic'), random_surname('arabic')
    else:
        return random_name('latin'), random_surname('latin')

