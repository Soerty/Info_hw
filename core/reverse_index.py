#-*- coding: utf-8 -*-
from collections import defaultdict


def reverse_index(texts):
    """Returns the reverse index of a set of texts

    For example, if we have three texts:
       T0 = "it is what it is"
       T1 = "what is it"
       T2 = "it is a banana"
    Then the inverse index will be:
       "a":      {2}
       "banana": {2}
       "is":     {0, 1, 2}
       "it":     {0, 1, 2}
       "what":   {0, 1}

    :param texts: The set of texts
    :return: defaultdict with reverse index

    >>> texts = [
    ...     'it is what it is',
    ...     'what is it',
    ...     'it is a banana'
    ... ]
    >>> sorted(reverse_index(texts))
    ['a', 'banana', 'is', 'it', 'what']
    """
    index = defaultdict(set)

    for id, text in enumerate(texts):
        for word in text.split():
            index[word].add(id)

    return index


if __name__ == '__main__':
    import doctest
    doctest.testmod()
