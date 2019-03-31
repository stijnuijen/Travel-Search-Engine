import json
import nltk
import re
from nltk.corpus import stopwords
from sys import getsizeof
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from spellchecker import SpellChecker

# Create small DEMO inverted index for faster computation



JSON_dir = "C:/Users/leonv/Documents/development/Master/Information_retrieval/clean_INDEX.json"
with open(JSON_dir) as f:
    INDEX = json.load(f)

# give queries and process in same manner as in search
query = "Planning a trip Argentina Hanoi to Hue Vietnam Rome Italy Restaurants"
text = query.lower()
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text)
spelling_correction = SpellChecker()
tokens2 = []
for word in tokens:
    tokens2.append(spelling_correction.correction(word))
ps = nltk.PorterStemmer()
words = [ps.stem(word) for word in tokens2]
stopset = set(stopwords.words('english'))
words = [word for word in words if word not in stopset]

food_vocab = ['acorn', 'squash', 'alfalfa', 'sprout', 'almond', 'anchovi', 'anis', 'appet', 'appetit', 'appl', 'apricot', 'artichok', 'asparagu', 'aspic',
                    'ate', 'avocado', 'bacon', 'bagel', 'bake', 'bamboo', 'shoot', 'banana', 'barbecu', 'barley', 'basil', 'batter', 'beancurd', 'bean', 'beef', 'beet', 'bell',
                    'pepper', 'berri', 'biscuit', 'bitter', 'blackbean', 'blackberri', 'black-ey', 'pea', 'bland', 'blood', 'orang', 'blueberri', 'boil', 'bowl', 'boysenberri', 'bran',
                    'bread', 'breadfruit', 'breakfast', 'broccoli', 'broil', 'browni', 'brown', 'rice', 'brunch', 'brussel', 'sprout', 'buckwheat', 'bun', 'burrito', 'butter', 'cake',
                    'calori', 'candi', 'cantaloup', 'caper', 'caramel', 'carbohydr', 'carrot', 'cashew', 'cassava', 'casserol', 'cater', 'cauliflow', 'cayenn', 'pepper', 'celeri',
                    'cereal', 'chard', 'cheddar', 'chees', 'cheesecak', 'chef', 'cherri', 'chew', 'chicken', 'chick', 'pea', 'chili', 'chip', 'chive', 'chocol', 'chopstick',
                    'chow', 'chutney', 'cilantro', 'cinnamon', 'citron', 'citru', 'clam', 'clove', 'cobbler', 'coconut', 'cod', 'coffe', 'coleslaw', 'collard', 'green', 'cook', 'cooki',
                    'corn', 'cornflak', 'cornmeal', 'cottag', 'chees', 'crab', 'cracker', 'cranberri', 'cream', 'cream', 'chees', 'crepe', 'crisp', 'crunch', 'crust', 'cucumb', 'cuisin',
                    'cupboard', 'cupcak', 'curd', 'current', 'curri', 'custard', 'daikon', 'dairi', 'dandelion', 'green', 'danish', 'pastri', 'date', 'dessert', 'diet', 'digest',
                    'digest', 'system', 'dill', 'dine', 'diner', 'dinner', 'dip', 'dish', 'dough', 'doughnut', 'dragonfruit', 'dress', 'dri', 'drink', 'dri', 'durian', 'eat',
                    'edam', 'chees', 'egg', 'eggplant', 'elderberri', 'endiv', 'entre', 'fast','fava', 'ban', 'fed', 'feed', 'fennel', 'fig', 'fillet', 'fire', 'fish', 'flan',
                    'flax', 'flour', 'food', 'food', 'pyramid', 'fork', 'freezer', 'french', 'fri', 'fri', 'fritter', 'frost', 'fruit', 'fri', 'garlic', 'gastronomi', 'gelatin',
                    'ginger', 'gingeral', 'gingerbread', 'glass', 'gouda', 'chees', 'grain', 'granola', 'grape', 'grapefruit', 'grate', 'gravi', 'greenbean', 'green', 'gyro', 'guava',
                    'herb', 'halibut', 'ham', 'hamburg', 'hash', 'hazelnut', 'herb', 'honey', 'honeydew', 'horseradish', 'hot', 'hot', 'dog', 'hot', 'sauc', 'hummu', 'hunger', 'hungri',
                    'ice', 'iceberg', 'lettuc', 'ice', 'tea', 'ice', 'ice', 'cream', 'ice', 'cream', 'cone', 'jackfruit', 'jalapeno', 'jam', 'jelli', 'jellybean', 'jicama', 'jimmi',
                    'jordan', 'almond', 'jug', 'juic', 'kale', 'kebab', 'ketchup', 'kettl', 'kidney', 'bean', 'kitchen', 'kiwi', 'knife', 'kohlrabi', 'kumquat', 'ladl', 'lamb',
                    'lard', 'lasagna', 'legum', 'lemon', 'lemonad', 'lentil', 'lettuc', 'licoric', 'lima', 'bean', 'lime', 'liver', 'loaf', 'lobster', 'lollipop', 'loquat', 'lox',
                    'lunch', 'lunchmeat', 'lyche', 'macaroni', 'macaroon', 'main', 'cours', 'maiz', 'mandarin', 'orang', 'mango', 'mapl', 'syrup', 'margarin', 'marionberri',
                    'marmalad', 'marshmallow', 'mash', 'mayonnais', 'meat', 'meatbal', 'meatloaf', 'melon', 'menu', 'meringu', 'milk', 'milkshak', 'millet', 'mincemeat',
                    'miner', 'mint', 'mint', 'molass', 'mozzarella', 'muffin', 'mug', 'munch', 'mushroom', 'mussel', 'mustard', 'mustard', 'green', 'mutton', 'napkin',
                    'nectar', 'nectarin', 'nibbl', 'noodl', 'nosh', 'nourish', 'nourish', 'nut', 'nutmeg', 'oat', 'oatmeal', 'oil', 'okra', 'oleo', 'oliv', 'omelet',
                    'omnivor', 'onion', 'orang', 'order', 'oregano', 'oven', 'oyster', 'pan', 'pancak', 'papaya', 'parsley', 'parsnip', 'pasta', 'pastri', 'pate',
                    'patti', 'pattypan', 'squash', 'peach', 'peanut', 'peanutbutt', 'pea', 'pear', 'pecan', 'peapod', 'pepper', 'pepperoni', 'persimmon', 'pickl',
                    'picnic', 'pie', 'pilaf', 'pineappl', 'pita', 'bread', 'pitcher', 'pizza', 'plate', 'platter', 'plum','poach', 'pomegran', 'pomelo', 'pop',
                    'popsicl', 'popcorn', 'popov', 'pork', 'pork', 'chop', 'pot', 'potato', 'preserv', 'pretzel', 'protein', 'prune', 'pud', 'pumpernickel', 'pumpkin',
                    'punch', 'quich', 'quinoa', 'radish', 'raisin', 'raspberri', 'ravioli', 'recip', 'refriger', 'relish', 'restaur', 'rhubarb', 'rib', 'rice', 'roast',
                    'roll', 'roll', 'pin', 'romain', 'rosemari', 'rye', 'saffron', 'sage', 'salad', 'salami', 'salmon', 'salsa', 'salt', 'sandwich', 'sauc', 'sauerkraut',
                    'sausag', 'savori', 'scallop', 'scrambl', 'seawe', 'seed', 'sesam', 'seed', 'shallot', 'sherbet', 'shish', 'kebab', 'shrimp', 'slaw', 'slice', 'smoke', 'soda',
                    'sole', 'sorbet', 'sorghum', 'sorrel', 'soup', 'sour', 'sour', 'cream', 'soy', 'soybean', 'soysauc', 'spaghetti', 'sparerib', 'spatula', 'spice', 'spinach', 'spoon',
                    'spork', 'sprinkl', 'sprout', 'spud', 'squash', 'squid', 'steak', 'stew', 'stir-fri', 'stomach', 'stove', 'straw', 'strawberri', 'string', 'bean', 'stringi', 'strudel',
                    'succotash', 'sugar', 'summer', 'squash', 'sunda', 'sunflow', 'supper', 'sushi', 'sweet', 'sweet', 'potato', 'swiss', 'chard', 'syrup', 'taco', 'take-out', 'tamal', 'tangerin',
                    'tapioca', 'taro', 'tarragon', 'tart', 'tea', 'teapot', 'teriyaki', 'thyme', 'toast', 'toaster', 'toffe', 'tofu', 'tomatillo', 'tomato',
                    'tort', 'tortilla', 'tuber', 'tuna', 'turkey', 'turmer', 'turnip', 'ugli', 'fruit', 'unleaven', 'utensil', 'vanilla', 'veal', 'veget', 'venison', 'vinegar', 'vitamin', 'wafer', 'waffl',
                    'walnut', 'wasabi', 'water', 'water', 'chestnut', 'watercress', 'watermelon', 'wheat', 'whey', 'whip', 'cream', 'wok', 'yam', 'yeast', 'yogurt', 'yolk', 'zucchini']

transport_vocab = ['aircraft', 'aircraft', 'carrier', 'airplan', 'ambul', 'amphibi', 'vehicl', 'armor', 'car', 'auto', 'automobil', 'babi', 'carriag',
                        'balloon', 'bathyscaph', 'barg', 'battleship', 'bicycl', 'bike', 'biplan', 'blimp', 'boat', 'bobsl', 'bomber', 'boxcar', 'broomstick', 'buggi', 'bulldoz',
                        'bullet', 'train', 'bu', 'cab', 'cabin', 'cruiser', 'cabl', 'car', 'caboos', 'camper', 'cano', 'car', 'caravan', 'caravel', 'cargo', 'ship', 'carriag', 'carrier',
                        'cart', 'catamaran', 'chair', 'lift', 'chariot', 'chopper', 'clipper', 'ship', 'clunker', 'coach', 'compact', 'car', 'combin', 'compact', 'car', 'conestoga',
                        'wagon', 'contain', 'ship', 'convert', 'convey', 'conveyor', 'belt', 'convoy', 'coup', 'cover', 'wagon', 'crane', 'crop', 'duster', 'cruis', 'ship', 'cruiser',
                        'cutter', 'cycl', 'deliveri', 'truck', 'deliveri', 'van', 'destroy', 'diesel', 'truck', 'dinghi', 'dirig', 'dirt', 'bike', 'dive', 'bell', 'dog', 'cart',
                        'dogsl', 'donkey', 'cart', 'dray', 'driver', 'dugout', 'cano', 'dump', 'truck', 'earth', 'mover', 'eighteen-wheel', 'electr', 'car', 'elev', 'railroad',
                        'elev', 'engin', 'escal', 'express', 'train', 'ferri', 'fireboat', 'fire', 'engin', 'fish', 'boat', 'flatb', 'truck', 'forklift', 'four-wheel', 'drive',
                        'freighter', 'freight', 'train', 'frigat', 'funicular', 'railway', 'galleon', 'garbag', 'truck', 'glider', 'go-cart', 'golf', 'cart', 'gondola', 'gondola',
                        'lift', 'gridlock', 'handcar', 'hang', 'glider', 'hansom', 'cab', 'harvest', 'haul', 'hay', 'wagon', 'hears', 'helicopt', 'hook', 'and', 'ladder', 'truck',
                        'hovercraft', 'hors', 'carriag', 'hot-air', 'balloon', 'hot', 'rod', 'houseboat', 'hull', 'humve', 'hybrid', 'hydrofoil', 'hydroplan', 'ice', 'boat', 'ice',
                        'breaker', 'jeep', 'jet', 'jet', 'boat', 'jetlin', 'journey', 'jet', 'pack', 'jet', 'ski', 'jumbo', 'jet', 'junk', 'kayak', 'ketch', 'land', 'craft',
                        'lifeboat', 'life', 'raft', 'light', 'rail', 'limo', 'limousin', 'litter', 'locomot', 'lorri', 'magic', 'carpet', 'maglev', 'mast', 'minesweep', 'minibu',
                        'minivan', 'model', 'T', 'monorail', 'mope', 'motor', 'motorboat', 'motorcycl', 'motor', 'home', 'mountain', 'bike', 'narrowboat', 'oar', 'ocean', 'liner',
                        'off-road', 'vehicl', 'oil', 'tanker', 'outboard', 'motor', 'outrigg', 'cano', 'oxcart', 'paddl', 'paddlewheel', 'parachut', 'passeng', 'patrol', 'car', 'pedal',
                        'boat', 'pickup', 'truck', 'pilot', 'plane', 'polic', 'car', 'power', 'boat', 'prairi', 'schooner', 'propel', 'PT', 'boat', 'pumper', 'truck', 'punt', 'push',
                        'cart', 'racecar', 'raft', 'railroad', 'railway', 'rapid', 'transit', 'recreat', 'vehicl', 'rickshaw', 'ride', 'riverboat', 'roadster', 'rocket', 'rover',
                        'rowboat', 'rudder', 'runabout', 'RV', 'sail', 'sailboat', 'satellit', 'school', 'bu', 'schooner', 'scooter', 'scull', 'seaplan', 'sedan', 'sedan', 'chair',
                        'segway', 'semi', 'ship', 'side', 'wheeler', 'skiff', 'ski', 'lift', 'sled', 'sledg', 'sleigh', 'snow', 'cat', 'snowmobil', 'snowplow', 'spaceship', 'space', 'shuttl',
                        'speedboat', 'squad', 'car', 'sst', 'stagecoach', 'station', 'wagon', 'steamboat', 'steamship', 'stock', 'car', 'stroller', 'submarin',
                        'submers', 'subway', 'surrey', 'suv', 'tank', 'tanker', 'taxi', 'taxicab', 'thresher', 'tire', 'toboggan', 'town', 'car', 'tow', 'truck',
                        'tractor', 'tractor-trail', 'trail', 'bike', 'trailer', 'train', 'tram', 'transit', 'trawler', 'tricycl', 'trolley', 'truck', 'tugboat', 'u-boat',
                        'ultralight', 'craft', 'unicycl', 'van', 'vehicl', 'vespa', 'vessel', 'wagon', 'warship', 'wheel', 'wheelbarrow', 'wheelchair', 'windjamm', 'wreck',
                        'yacht', 'zamboni', 'zeppelin']


demo_index = {}
for word in words:
    if word in INDEX:
        sub_index = {}
        for url in INDEX[word]:
                if not url.startswith("https://en.wikipedia.org"):
                        sub_index[url] = INDEX[word][url]
        demo_index[word] = sub_index


for word in food_vocab+transport_vocab:
        if word in INDEX:
                sub_index = {}
                for url in INDEX[word]:
                        if not url.startswith("https://en.wikipedia.org"):
                                sub_index[url] = INDEX[word][url]
                demo_index[word] = sub_index 


print(demo_index)
print("")
for i in demo_index:
        print(i)


with open('demo_INDEX.json', 'w') as fp:
      json.dump(demo_index, fp)