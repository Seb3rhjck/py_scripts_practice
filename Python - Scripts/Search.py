from lib2to3.pytree import _Results
from unittest import result
from google import  search

b = "In search of Sunrise - DJ Tiesto"
resultado = search(b)
for a in resultado:
    print(a)