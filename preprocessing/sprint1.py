from bs4 import BeautifulSoup
import unidecode
import re

TAGS_HTML = [
    ''
    ]

def remove_accents(a):
    if (a is None):
        return
    return unidecode.unidecode(a)

def remove_punctuation_space_start(p):
    if(p is None):
        return
    return re.sub('^[#!¡¿?.+*\-\\_(),;:=·\s\'<=>"]*','', p)

def remove_punctuation_space_end(p):
    if(p is None):
        return
    return re.sub('[#!¡¿?.+*\-\\_(),;:=·\s\'<=>"]*$','',p)

def delete_empty(e):
    if (e is None):
        return
    return e.strip()

def delete_arroba_unicode(a):
    if(a is None):
        return
    return re.sub('(?:\(R\))','',a)

def remove_tags_html(w):
    return BeautifulSoup(w).get_text()

def remove_incomplete_tags_html(w):
    return 