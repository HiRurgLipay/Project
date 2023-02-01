words = ('комок', 'мама', 'палка', 'ротор', 'телец')

def is_palindrome(word):
    return word == word[::-1]

palindromes = filter(is_palindrome, words)
print(*palindromes)