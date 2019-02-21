stringy = 'https://www.lonelyplanet.com/thorntree/forums/americas-south-america/argentina/70-days-on-from-buenos-aries-where-to-spend-my-birthday'

with open('url_list.txt','r') as f:
    if stringy not in f.read():
        print("Hi")