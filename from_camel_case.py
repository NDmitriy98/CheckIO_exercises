def from_camel_case(name):
    new_name = ''
    for i, c in enumerate(name):
        if c.isupper():
            if i == 0:
                new_name += c.lower()
            else:
                new_name += '_' + c.lower()
        else:
            new_name += c
    return new_name
