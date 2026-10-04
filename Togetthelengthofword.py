words = ["apple", "banana", "kiwi", "cherry", "mango"]
dictionary = {}

for i in words:
    length_of_words = len(i)
    new_word = {i : length_of_words}
    dictionary.update(new_word)

print(dictionary)


"""         in place of this 
            new_word = {i : length_of_words}
            dictionary.update(new_word) 
            we can use this 
            dictionary[i] = length_of_words    """