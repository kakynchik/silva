def palindrome(word):
    word = word.lower()
    reversed_word = word[::-1]
    return word == reversed_word
input_word = input('vvedit slovo pzh: ')
if palindrome(input_word):
    print('palindrom')
else:
    print('ne palindrom')