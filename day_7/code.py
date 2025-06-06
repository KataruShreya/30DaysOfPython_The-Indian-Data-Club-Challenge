import string

def clean_text(text):
    text = text.lower()
    clean_text = ''

    for char in text:
        if char not in string.punctuation:
            clean_text += char
        else:
            clean_text += ' '
    return clean_text

def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count



f = open('data.txt', 'r')
text = f.read()
print("The text BEFORE pre-processing is:", text)

processed_text = clean_text(text)
print("The text AFTER pre-processing is:", processed_text)

words = processed_text.split()

word_counts = count_words(words)

for word, count in word_counts.items():
    print(f"{word}: {count}")




# CODE LOGIC

'''

1. Import the string module to access punctuation characters.

2. Define a function "clean_text(text)" to:
   - Convert the input text to lowercase.
   - Replace every punctuation character with a space.
   - Return the cleaned text without punctuation.

3. Define a function "count_words(words)" to:
   - Initialize an empty dictionary `word_count`.
   - Iterate over the list of words.
   - For each word, increment its count in `word_count`.
   - Return the dictionary containing word frequencies.

4. Open the file "data.txt" in read mode and read its contents into "text".

5. Print the original text before preprocessing.

6. Call "clean_text(text)" to remove punctuation and convert to lowercase, store result in "processed_text".

7. Print the cleaned text after preprocessing.

8. Split "processed_text" into a list of words using ".split()".

9. Call "count_words(words)" to get a dictionary of word frequencies.

10. Iterate over the dictionary and print each word with its count.


'''


# ***Note!***

'''

The below way is an alternative method to count word frequencies without using dictionaries.
It uses a set to find unique words and then counts each word's frequency by using the list's count() method. 
It is a simple alternative way to count word frequencies without additional libraries


import string

def clean_text(text):
    text = text.lower()
    cleaned = ''
    for char in text:
        if char not in string.punctuation:
            cleaned += char
        else:
            cleaned += ' '
    return cleaned

def count_words(words):
    unique_words = set(words)
    for word in unique_words:
        print(f"{word}: {words.count(word)}")


f = open('data.txt', 'r')
text = f.read()

cleaned_text = clean_text(text)
words = cleaned_text.split()

count_words(words)

 
'''



