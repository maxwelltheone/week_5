# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string 
magic = 'abracadabra'
# a. Retrieve the 5th character.

print(magic[5])
# b. Retrieve the second to last character.
print(magic[9])
# c. Find the first occurrence of the letter 'c'.
substring= magic.find("c")
print(substring)

# Advanced Slicing:
# Given the string
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
substring= alphabet.find("hij")
print(substring)
substring= alphabet[7:10]
print(substring)
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:13:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote2= "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
substring= quote2.find("John F. Kennedy")
print(substring)
substring= quote2[83:100]
print(substring)
# Manipulating Words:
# Given the string 
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
substring = info.find("subjective")
print(substring)
# b. Extract every third word.
substring = info[0:-1:3]

# Problem Set 3: String Methods
quote = "MAY THE FORCE BE WITH YOU."
# Upper & Lower:
# Convert the following text to lowercase: 
print(quote.lower())

# String Joining and Splitting:
# Given the list 
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
word_list = ["Make", "haste", "slowly."]
joined_list = " ".join(word_list)
print(joined_list)

# Replacing Words:
# Modify the sentence: 
sentence = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
new_sentence = sentence.replace("busy", "distracted")
print(new_sentence)
# b. Replace "plans" with "mistakes".
new_sentence = sentence.replace("plans", "mistakes")
print(new_sentence)

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
Iteration = "Iteration" * 7
print(Iteration)

# Word Search:
# Check if the word "moonlight" appears in the 
quote3 = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print(quote3.find("moonlight"))

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the
phrase = "Supercalifragilisticexpialidocious"
print(len(phrase))

# maxwelltheone
# elpancho17