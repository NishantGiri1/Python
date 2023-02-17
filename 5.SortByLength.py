"""Q5: Write a function or lambda function (preferably) that takes a list of strings and returns a new list with all
strings sorted in descending order of length. """


def sort_by_length(string_array):
    return sorted(string_array, key=lambda s: -len(s))


string_array = ["dog", "cat", "bird"]
print(sort_by_length(string_array))
