def count_words(filename):
    import string # Necessary for python functions to remove punctuations
    ### Counts number of words without punctuations in the textfile

    # Opening file
    try:
        with open(filename) as file:
            text = file.read()
    # Removing punctuations according to https://www.geeksforgeeks.org/python/python-remove-punctuation-from-string/
        translator = str.maketrans('','',string.punctuation)
        clean_text = text.translate(translator)
        # Separating words in file in list, including punctuations and counting the words in list
        clean_words = clean_text.split()
        clean_words_counts = len(clean_words)
    # If the file can't be found, return None
    except FileNotFoundError:
        clean_words_counts = None
    return clean_words_counts


print('Please enter your filename to count words in it (Example textfile suggested : The_Zen_of_Python.txt)')
filename = input()
clean_words_counts = count_words(filename)
print(f'The file {filename} contains {clean_words_counts} words without punctuation.')
