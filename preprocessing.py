import unidecode
import re

def remove_accents(a):
    if (a is None):
        return
    return unidecode.unidecode(a)

def remove_punctuation(p):

    return (re.sub(r'[^\w\s]', "", p) if p is not None else p)

def delete_empty(e):
    if (e is None):
        return
    return e.strip()
