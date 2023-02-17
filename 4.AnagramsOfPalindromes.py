"""Q4: Write a function that takes a list of strings and returns a new list with all strings that are anagrams of a
palindrome (i.e., a word or phrase that can be rearranged to form a palindrome). If you can use list comprehension
then it will be better. """

from collections import Counter


def anagram_palindrome(strings):
    def is_palindrome(input):
        return input == input[::-1]

    def is_anagram_palindrome(string):
        count = Counter(string)
        num_odd = sum(count[char] % 2 for char in count)
        return num_odd <= 1

    return [string for string in strings if is_anagram_palindrome(string) and is_palindrome(string)]


input_strings = ['racecar', 'hello', 'level', 'carcare', 'carecar', 'civic', 'lehol', 'vicic']
print(anagram_palindrome(input_strings))
