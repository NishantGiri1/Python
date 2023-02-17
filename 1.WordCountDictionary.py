"""Write a program that reads in all the lines of the file (take any random or article from wikipedia),
and then create a dictionary, where the key is the line number and value is another dictionary.
This another dictionary should contain length of the words as keys, and the number of words having same length as values."""


def word_count_dict(file):
    dictionary = {}
    with open(file, 'r') as f:
        for i, line in enumerate(f, 1):
            words = line.strip().split()
            count_dict = {}
            for word in words:
                length = len(word)
                if length not in count_dict:
                    count_dict[length] = 1
                else:
                    count_dict[length] += 1
            dictionary[i] = count_dict
    return dictionary


filename = 'wordCountFile.txt'
print(word_count_dict(filename))
