import re
def checkio(text: str) -> str:

    #replace this for solution
    text = text.lower()
    dict_letters = []
    for letter in text:
        if re.search(r"[a-z]", letter):
            dict_letters.append(dict(name=letter, count=text.count(letter)))
    dict_letters.sort(key=lambda x: x['count'], reverse=True)
    max = dict_letters[0]['count']
    max_dict = []
    for d in dict_letters:
        if d['count'] == max:
            max_dict.append(d)
        else:
            break

    max_dict.sort(key=lambda x: x['name'])
    return max_dict[0]['name']


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")