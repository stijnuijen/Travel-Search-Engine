# this file is for search
import csv
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import numpy as np
import math
import json
import operator
import time


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


culture_vocab = ['french', 'paleo-indian', 'assyrian', 'alfr', 'kinship', 'schema', 'pufendorf', 'music', 'spencer', 'growingli', 'cultivar', 'environment', 'flawless', 
                'tillag', 'belief', 'crop', 'countercultur', 'morgan', 'heritag', 'weimar', 'psychogenesi', 'today', 'paleocontact', 'structur', 'societi', 'architectur',
                'worldview', 'encultur', 'japan', 'hegemoni', 'ethno', 'monetari', 'supremac', 'compatriot', 'industri', 'rousseau', 'individu', 'human', 'such', 'economi', 
                'theme', 'forwax', 'japanophilia', 'philistin', 'accultur', 'discours', 'innov', 'relativ', 'femin', 'genet', 'consum', 'syncret', 'modern', 'analysi', 'corn', 
                'left-w', 'cult', 'burgeon', 'deracin', 'sensibl', 'monocultur', 'spiritu', 'correct', 'overcrop', 'museum', 'mass', 'aegean', 'weber', 'class', 'mindset', 'letter', 
                'circl', 'austro-hungarian', 'bro', 'naturalist', 'puritan', 'territori', 'germin', 'get', 'system', 'film', 'describ', 'conscious', 'manag', 'america', 'gener', 
                'subcultur', 'perspect', 'edward', 'classic', 'hord', 'stuart', 'idea', 'cultic', 'alethophobia', 'rice', 'thompson', 'civil', 'artifact', 'valu', 'philosoph', 'ritual',
                'latitudinarian', 'tylor', 'milieu', 'homogeni', 'henri', 'understand', 'nobl', 'common', 'fals', 'teeth', 'overgrow', 'dongyi', 'cultur', 'holism', 'materi', 'art', 
                'zionism', 'mcrobbi', 'burnett', 'romantic', 'georg', 'sunni', 'age', 'shelter', 'cultiv', 'immigr', 'gain', 'agrarian', 'vinicultur', 'julia', 'write', 'transcultur', 
                'aesthet', 'jean-jacqu', 'genr', 'foremost', 'philosophi', 'chang', 'william', 'histori', 'frankfurt', 'written', 'flourish', 'ontogenet', 'foodway', 'psycholog', 'malthusian', 
                'minor', 'ceremoni', 'photographi', 'epistemolog', 'rule', 'linguist', 'hebdig', 'althuss', 'ultra', 'kant', 'japanif', 'richard', 'peoplehood', 'origin', 'crescent', 'popular', 
                'rural', 'undevelop', 'herder', 'intercrop', 'pot', 'institut', 'stereotyp', 'yellow', 'hybrid', 'hous', 'terror', 'known', 'particularli', 'medicin', 'product', 'sanskrit', 
                'serer', 'forthwax', 'pentecost', 'degrowth', 'rustic', 'univers', 'shintoism', 'western', 'matur', 'hobb', 'oral', 'ethic', 'compar', 'count', 'ethnic', 'rome', 
                'tradit', 'von', 'ontogenesi', 'media', 'danc', 'gottfri', 'hamburg', 'folkway', 'intang', 'nationalist', 'artisanship', 'religion', 'ingrow', 'ungrown', 'hoggart', 'oyster', 
                'turn', 'teleolog', 'gilroy', 'ist', 'psych', 'overyield', 'especi', 'phenomenon', 'evolv', 'civilis', 'nowaday', 'appreci', 'morphogenesi', 'etho', 'development', 'accret', 
                'chauvin', 'refin', 'melt', 'homogen', 'network', 'sophist', 'relat', 'anthropolog', 'institution', 'big', 'latin', 'fashion', 'postmodern', 'francophil', 'parochi', 'in', 
                'intergrown', 'hinduism', 'raimon', 'life', 'symbol', 'decad', 'import', 'develop', 'e.', 'marxist', 'noun', 'fandom', 'cycl', 'grow', 'rais', 'classicist', 'fundament', 'op', 
                'indigen', 'bodi', 'islam', 'innat', 'sunday', 'view', 'nettleb', 'root', 'excresc', 'field', 'most', 'famou', 'feminist', 'samuel', 'everyday', 'franz', 'archeolog',
                'contemporari', 'auxesi', 'outgrow', 'indian', 'lifestyl', 'doctrin', 'tast', 'polit', 'expans', 'flower', 'durkheim', 'mongolian', 'more', 'p.', 'willi', 'enlighten',
                'dysplasia', 'johann', 'permiss', 'beanfield', 'herbert', 'perfect', 'paleo-amerind', 'forgrow', 'invent', 'tea', 'formalist', 'peasant', 'experi', 'cytogenesi', 'nation', 
                'iconographi', 'ontogeni', 'tumor', 'elit', 'hairstyl', 'japanes', 'commun', 'maizefield', 'wilhelm', 'archaeolog', 'arnold', 'vernacular', 'angela', 'critic', 'growth', 
                'minoan', 'jewelri', 'birmingham', 'griselda', 'influenc', 'discern', 'countri', 'clannish', 'loui', 'exampl', 'cranberri', 'hellad', 'folklor', 'geographi', 'kristeva', 
                'cosmolog', 'kind', 'paleo-american', 'movement', 'matthew', 'idiom', 'formal', 'hall', 'bildung', 'lewi', 'concept', 'particular', 'ethnocentr', 'polish', 'world', 'centr', 
                'multicultur', 'nomad', 'metaphor', 'diaspora', 'karl', 'outgrowth', 'islamist', 'compani', 'thrive', 'diffus', 'authent', 'mosaic', 'barbarian', 'tradition', 'till', 'superfici', 
                'confucianist', 'religi', 'paddi', 'canada', 'global', 'meme', 'ne', 'germani', 'econom', 'savag', 'misgrow', 'non-materi', 'cloth', 'assimil', 'languag', 'kalashnikov', 'westernis', 
                'thoma', 'colon', 'content', 'adolf', 'gender', 'disputation', 'viticultur', 'veget', 'marx', 'starter', 'preval', 'group', 'percept', 'vulgar', 'entrepreneuri', 'overwax', 'liber', 
                'treasur', 'gentil', 'taoism', 'technolog', 'atlant', 'other', 'kimono', 'bohemian', 'underdevelop', 'husbandri', 'cook', 'growabl', 'patriarch', 'ism', 'cybercultur', 'hypertrophi', 
                'organ', 'attitud', 'macumba','denomination', 'style', 'neo', 'of', 'biolog', 'metalinguist', 'druidism', 'state', 'urban', 'foreign', 'exclusion', 'low', 'landscap', 'grang', 
                'raymond', 'simmel', 'panikkar', 'evolutionari', 'knowledg', 'mean', 'evolut', 'boa', 'dialect', 'scienc', 'well', 'eurocentr', 'interact', 'refer', 'emot', 'social', 'regard', 'plu', 
                'max', 'nativ', 'humboldt', 'empir', 'intergrow', 'sabaean', 'mycenaean', 'cuisin', 'cognit', 'grower', 'agroecosystem', 'commerci', 'great', 'agricultur', 'power', 'divers', 'hindu', 
                'hered', 'patriot', 'agriculturist', 'aspect', 'dick', 'ingrowth', 'pagan', 'psychoanalysi', 'learn', 'aftergrowth', 'histor', 'interest', 'cultist', 'sociolinguist', 'stratif', 'uniqu', 
                'emphasi', 'immanuel', 'haut', 'peopl', 'actor', 'primitiv', 'coloni', 'mental', 'sociolog', 'hermetic', 'cosmopolitan', 'polyp', 'regrow', 'hedon', 'uncultiv', 'insular', 'inspir', 
                'orient', 'wheel', 'german', 'ancient', 'hebraic', 'studi', 'modif', 'mytholog', 'tusculana', 'theori', 'disciplin', 'for', 'english', 'object', 'bastian', 'environ', 'popul', 'high', 
                'literatur', 'besid', 'unit', 'bed', 'chines', 'kingdom', 'finish', 'european', 'hindustan', 'provinci', 'pollock', 'snobbism', 'paul', 'humanist', 'capit', 'behavior', 'intellectu', 
                'folk', 'farmer', 'invest', 'cicero', 'school', 'marxism', 'ideolog', 'the', 'marriag', 'context', 'darwin', 'americana', 'ice', 'taoist', 'exclus', 'indu', 'prolifer', 'consumer', 
                'natur', 'literari', 'anarchi', 'heathen', 'nationwid']

def l2_norm(a):  
    return math.sqrt(np.dot(a, a))

def cosine_similarity(a, b):
    return np.dot(a,b) / (l2_norm(a) * l2_norm(b))

def Search(query, food = False, transport = False, culture = False):

    JSON_dir = "C:/Users/leonv/Documents/development/Master/Information_retrieval/clean_INDEX.json" 
    with open(JSON_dir) as f:
        INDEX = json.load(f)

    # if food filter is activated:
    food_urls = {} 
    if food == True:
        for food_term in food_vocab:
            try:
                for url in INDEX[food_term]:
                    if url not in food_urls:
                        food_urls[url] = 1
                    else: 
                        food_urls[url] += 1      
            except:
                continue 
    
    for key, value in list(food_urls.items()):
        if value < 100:
            del food_urls[key]
    
    # if transport filter is activated:
    transport_urls = {} 
    if transport == True:
        for transport_term in transport_vocab:
            try:
                for url in INDEX[transport_term]:
                    if url not in transport_urls:
                        transport_urls[url] = 1
                    else: 
                        transport_urls[url] += 1      
            except:
                continue 
    
    for key, value in list(transport_urls.items()):
        if value < 100:
            del transport_urls[key]
    
    # if culture filter is activated:
    culture_urls = {} 
    if culture == True:
        for culture_term in culture_vocab:
            try:
                for url in INDEX[culture_term]:
                    if url not in culture_urls:
                        culture_urls[url] = 1
                    else: 
                        culture_urls[url] += 1      
            except:
                continue 
    
    for key, value in list(culture_urls.items()):
        if value < 100:
            del culture_urls[key]

    # same preprocessing as in index creation:
    text = query.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    ps = nltk.PorterStemmer()
    words = [ps.stem(word) for word in tokens]
    stopset = set(stopwords.words('english'))
    words = [word for word in words if word not in stopset]
    freq_dict = {i:words.count(i) for i in set(words)}

    # create query vector with tfidf values:
    N_docs = 36091
    query_vector = []
    for word in freq_dict:
        tf = freq_dict[word] / len(words)
        try:
            df = len(INDEX[word]) + 1
        except:
            df = 1
        idf = math.log10(N_docs/ df)
        query_vector.append(tf*idf)
    query_vector = np.array(query_vector)

    # determine pages with at least one word from the query
    pages_with_words = []
    for word in freq_dict:
        try:
            for url in INDEX[word]:
                if url not in pages_with_words:
                    pages_with_words.append(url)
        except:
            continue
    
    # create tfidf vectors of those pages and 
    # calculate the cosine simularity
    page_distance_to_query = {}
    for url in pages_with_words:
        page_vector = []
        for word in freq_dict:
            try:
                page_vector.append(float(INDEX[word][url]))
            except:
                page_vector.append(0)
        page_vector = np.array(page_vector)
        page_distance_to_query[url] = cosine_similarity(query_vector, page_vector)

    sorted_pages = sorted(page_distance_to_query.items(), key=operator.itemgetter(1))

    # delete all irrelevant pages if one or multiple checkbox(es) is/are activated
    results = []
    if food == True and transport == True and culture == True:
        for url in sorted_pages:
            if url[0] in food_urls and url[0] in transport_urls and url[0] in culture_urls:
                results.append(url)
        sorted_pages = results

    if food == True and transport == True and culture == False:
        for url in sorted_pages:
            if url[0] in food_urls and url[0] in transport_urls:
                results.append(url)
        sorted_pages = results

    if food == True and transport == False and culture == False:
        for url in sorted_pages:
            if url[0] in food_urls and url[0] in transport_urls:
                results.append(url)
        sorted_pages = results

    if food == True and transport == False and culture == True:
        for url in sorted_pages:
            if url[0] in food_urls and url[0] in culture_urls:
                results.append(url)
        sorted_pages = results

    if food == False and transport == True and culture == True:
        for url in sorted_pages:
            if url[0] in transport_urls and url[0] in culture_urls:
                results.append(url)
        sorted_pages = results

    if food == False and transport == False and culture == True:
        for url in sorted_pages:
            if url[0] in culture_urls:
                results.append(url)
        sorted_pages = results

    if food == False and transport == True and culture == False:
        for url in sorted_pages:
            if url[0] in transport_urls:
                results.append(url)
        sorted_pages = results

    return sorted_pages
    
main_start_time = time.time()
print(Search("South America", food = True))
print("Query took: --- %s seconds ---" % (time.time() - main_start_time))
