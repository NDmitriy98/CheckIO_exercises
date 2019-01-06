def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    pos_begin = text.find(begin) if text.find(begin) != -1 else None
    pos_end = text.find(end) if text.find(end) != -1 else None

    if pos_begin is not None and pos_end is not None:
        if pos_begin < pos_end:
            return text[pos_begin + len(begin):pos_end]
        else:
            return ''
    elif pos_begin is not None and pos_end is None:
        return text[pos_begin + len(begin):]
    elif pos_begin is None and pos_end is not None:
        return text[:pos_end]
    else:
        return text


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')