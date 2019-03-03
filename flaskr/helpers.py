import re

def query(string):
    query_string = string.replace(' ', '+')
    return query_string.lower()
