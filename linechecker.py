with open('url_list_large.txt', 'r') as f:
    directory = 'lonelyplanet'
    sumy = sum(1 for line in f if directory in line)
    print("{} page count:{}".format(directory, sumy))