import pytest
from code_exercise.anagram import is_anagram


@pytest.mark.parametrize('word, anagram, result', [
    ('lemonade', 'memonade', False),
    ('diet', 'tedi', True),
    ('lemonade', 'memonade', False),
    ('househouse', 'house', False),
    ('qqqwww', 'qqqqww', False)])
def test_is_anagram(word, anagram, result):
    assert is_anagram(word, anagram) == result


@pytest.mark.parametrize('word, anagram, message', [
    ('', 'tedi', 'One or more words are empty'),
    ('something', '', 'One or more words are empty'),
    (1, 'anagram', 'One or more words are not strings'),
    ('word', ['a'], 'One or more words are not strings'),
    ('word word', 'anagram', 'One or more words are invalid'),
    ('word', 'anagram anagram', 'One or more words are invalid'),
    ('%', 'anagram', 'One or more words has an invalid character'),
    ('word', '^', 'One or more words has an invalid character'),
    ('.word', 'anagram', 'One or more words has an invalid character'),
    ('word', 'anagram&', 'One or more words has an invalid character')])
def test_is_anagram_value_error(word, anagram, message):
    with pytest.raises(ValueError, match=message):
        is_anagram(word, anagram)
