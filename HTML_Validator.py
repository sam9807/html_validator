#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking
    whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a
    # list of html tags without any extra text;
    # then process these html tags using the balanced
    # parentheses algorithm from the class/book
    # the main difference between your code and the code from class will be
    # that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags

    s = []
    balanced = True

    for tags in _extract_tags(html):
        if '/' not in tags:
            s.append(tags)
        else:
            if s == []:
                balanced = False
            else:
                top = s.pop()
                if top[2:] not in tags[1:]:
                    balanced = False
    if balanced and s == []:
        return True
    else:
        return False


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be
    used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags
    contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    s = []

    for index in range(len(html)):
        temp = ''
        tags = html[index]

        if tags == '<':
            temp += '<'
            while tags != '>':
                if index < (len(html) - 1):
                    index = index + 1
                    tags = html[index]
                    temp += tags
                else:
                    break
            s.append(temp)
    return s
