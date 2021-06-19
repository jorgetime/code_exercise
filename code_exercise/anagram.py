def is_anagram(word, anagram):
    if not isinstance(word, str) or not isinstance(anagram, str):
        raise ValueError('One or more words are not strings')
    if len(word) == 0 or len(anagram) == 0:
        raise ValueError('One or more words are empty')
    if len(word.split()) != 1 or len(anagram.split()) != 1:
        raise ValueError('One or more words are invalid')
    if not word.isalpha() or not anagram.isalpha():
        raise ValueError('One or more words has an invalid character')

    word_list = list(word)
    word_list.sort()
    anagram_list = list(anagram)
    anagram_list.sort()

    return word_list == anagram_list
