"""15. Write a program that:
Takes a sentence as input
Splits it into words
Stores the frequency of each word in a dictionary
Prints the dictionary
Example:
Input: "python is fun and python is powerful"
                         Output: {"python": 2, "is": 2, "fun": 1, "and": 1, "powerful": 1}
"""

sentence = input("Enter a sentence: ")
words = sentence.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)
