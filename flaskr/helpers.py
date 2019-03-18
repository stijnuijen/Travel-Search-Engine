import re

def query(string):
    query_string = string.replace(' ', '+')
    return query_string.lower()


def paginate(results, n, page):
    """
    Function to create a pagination object that takes the full results list,
    number of results per page n and the current page as input.
    Returns the pagination results for the correct page.
    """
    
    page_to_index = page - 1
    paginate_results = [results[x:x+n] for x in range(0, len(results), n)]

    return paginate_results[page_to_index]
