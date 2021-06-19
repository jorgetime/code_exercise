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
