with open('url_list.txt', 'r') as f:
    directory = 'wikipedia.org'
    sumy = sum(1 for line in f if directory in line)
    print("{} page count:{}".format(directory, sumy))