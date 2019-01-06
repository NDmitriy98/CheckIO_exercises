
def list_to_str(lst):
    return ''.join(lst)

def unic_lst(list1, list2):
    res = []
    temp_l1 = []
    for a in list1:
        temp_l1.append(a)
    for item in list2:
        if item not in temp_l1:
            temp_l1.append(item)
            res.append(item)
    return res

def checkio(data):
    symbols = {}
    cur_mass = 0
    for word in data:
        for i, symb in enumerate(word):
            if symbols.get(symb) is None:
                try:
                    symbols[symb] = unic_lst(list(symb), list(word[i+1:]))
                except IndexError:
                    symbols[symb] = []
            else:
                try:
                    symbols[symb].extend(unic_lst(symbols[symb], list(word[i+1:])))
                except IndexError:
                    pass

    last = set()
    for symb in symbols:
        if len(symbols[symb]) == 0:
            last.add(symb)
    alph_ordered = list(last)
    alph_ordered.sort()

    'f'.up

    return


#checkio(["aazzss"])
checkio(["klm", "kadl", "lsm"])