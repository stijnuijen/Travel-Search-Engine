import nltk

food_vocab = ['acorn', 'squash', 'alfalfa', 'sprouts', 'almond', 'anchovy', 'anise', 'appetizer', 'appetite', 'apple', 'apricot', 'artichoke', 'asparagus', 'aspic', 'ate', 'avocado', 'bacon', 'bagel', 'bake', 'bamboo', 'shoots', 'banana', 'barbecue', 'barley', 'basil', 'batter', 'beancurd', 'beans', 'beef', 'beet', 'bell', 'pepper', 'berry', 'biscuit', 'bitter', 'blackbeans', 'blackberry', 'black-eyed', 'peas', 'bland', 'blood', 'orange', 'blueberry', 'boil', 'bowl', 'boysenberry', 'bran', 'bread', 'breadfruit', 'breakfast', 'broccoli', 'broil', 'brownie', 'brown', 'rice', 'brunch', 'Brussels', 'sprouts', 'buckwheat', 'buns', 'burrito', 'butter', 'cake', 'calorie', 'candy', 'cantaloupe', 'capers', 'caramel', 'carbohydrate', 'carrot', 'cashew', 'cassava', 'casserole', 'cater', 'cauliflower', 'cayenne', 'pepper', 'celery', 'cereal', 'chard', 'cheddar', 'cheese', 'cheesecake', 'chef', 'cherry', 'chew', 'chicken', 'chick',
                'peas', 'chili', 'chips', 'chives', 'chocolate', 'chopsticks', 'chow', 'chutney', 'cilantro', 'cinnamon', 'citron', 'citrus', 'clam', 'cloves', 'cobbler', 'coconut', 'cod', 'coffee', 'coleslaw', 'collard', 'greens', 'cook', 'cookie', 'corn', 'cornflakes', 'cornmeal', 'cottage', 'cheese', 'crab', 'crackers', 'cranberry', 'cream', 'cream', 'cheese', 'crepe', 'crisp', 'crunch', 'crust', 'cucumber', 'cuisine', 'cupboard', 'cupcake', 'curds', 'currents', 'curry', 'custard', 'daikon', 'dairy', 'dandelion', 'greens', 'Danish', 'pastry', 'dates', 'dessert', 'diet', 'digest', 'digestive', 'system', 'dill', 'dine', 'diner', 'dinner', 'dip', 'dish', 'dough', 'doughnut', 'dragonfruit', 'dressing', 'dried', 'drink', 'dry', 'durian', 'eat', 'Edam', 'cheese', 'egg', 'eggplant', 'elderberry', 'endive', 'entree', 'fast', 'fava', 'bans', 'fed', 'feed', 'fennel', 'fig', 'fillet', 'fire', 'fish', 'flan', 'flax', 'flour', 'food', 'food', 'pyramid', 'fork', 'freezer', 'French', 'fries', 'fried', 'fritter', 'frosting', 'fruit', 'fry', 'garlic', 'gastronomy', 'gelatin', 'ginger', 'gingerale', 'gingerbread', 'glasses', 'Gouda', 'cheese', 'grain', 'granola', 'grape', 'grapefruit', 'grated', 'gravy', 'greenbean', 'greens', 'gyro', 'guava', 'herbs', 'halibut', 'ham', 'hamburger', 'hash', 'hazelnut', 'herbs', 'honey', 'honeydew', 'horseradish', 'hot', 'hot', 'dog', 'hot', 'sauce', 'hummus', 'hunger', 'hungry', 'ice', 'iceberg', 'lettuce', 'iced', 'tea', 'icing', 'ice', 'cream', 'ice', 'cream', 'cone', 'jackfruit', 'jalapeno', 'jam', 'jelly', 'jellybeans', 'jicama', 'jimmies', 'Jordan', 'almonds', 'jug', 'juice', 'kale', 'kebab', 'ketchup', 'kettle', 'kidney', 'beans', 'kitchen', 'kiwi', 'knife', 'kohlrabi', 'kumquat', 'ladle', 'lamb', 'lard', 'lasagna', 'legumes', 'lemon', 'lemonade', 'lentils', 'lettuce', 'licorice', 'Lima', 'beans', 'lime', 'liver', 'loaf', 'lobster', 'lollipop', 'loquat', 'lox', 'lunch', 'lunchmeat', 'lychee', 'macaroni', 'macaroon', 'main', 'course', 'maize', 'mandarin', 'orange', 'mango', 'maple', 'syrup',
                'margarine', 'marionberry', 'marmalade', 'marshmallow', 'mashed', 'mayonnaise', 'meat', 'meatballs', 'meatloaf', 'melon', 'menu', 'meringue', 'milk', 'milkshake', 'millet', 'mincemeat', 'minerals', 'mint', 'mints', 'molasses', 'mozzarella', 'muffin', 'mug', 'munch', 'mushroom', 'mussels', 'mustard', 'mustard', 'greens', 'mutton', 'napkin', 'nectar', 'nectarine', 'nibble', 'noodles', 'nosh', 'nourish', 'nourishment', 'nut', 'nutmeg', 'oats', 'oatmeal', 'oil', 'okra', 'oleo', 'olive', 'omelet', 'omnivore', 'onion', 'orange', 'order', 'oregano', 'oven', 'oyster', 'pan', 'pancake', 'papaya', 'parsley', 'parsnip', 'pasta', 'pastry', 'pate', 'patty', 'pattypan', 'squash', 'peach', 'peanut', 'peanutbutter', 'pea', 'pear', 'pecan', 'peapod', 'pepper', 'pepperoni', 'persimmon', 'pickle', 'picnic', 'pie', 'pilaf', 'pineapple', 'pita', 'bread', 'pitcher', 'pizza', 'plate', 'platter', 'plum', 'poached', 'pomegranate', 'pomelo', 'pop', 'popsicle', 'popcorn', 'popovers', 'pork', 'pork', 'chops', 'pot', 'potato', 'preserves', 'pretzel', 'protein', 'prune', 'pudding', 'pumpernickel', 'pumpkin', 'punch', 'quiche', 'quinoa', 'radish', 'raisin', 'raspberry', 'ravioli', 'recipe', 'refrigerator', 'relish', 'restaurant', 'rhubarb', 'ribs', 'rice', 'roast', 'roll', 'rolling', 'pin', 'romaine', 'rosemary', 'rye', 'saffron', 'sage', 'salad', 'salami', 'salmon', 'salsa', 'salt', 'sandwich', 'sauce', 'sauerkraut', 'sausage', 'savory', 'scallops', 'scrambled', 'seaweed', 'seeds', 'sesame', 'seed', 'shallots', 'sherbet', 'shish', 'kebab', 'shrimp', 'slaw', 'slice', 'smoked', 'soda', 'sole', 'sorbet', 'sorghum', 'sorrel', 'soup', 'sour', 'sour', 'cream', 'soy', 'soybeans', 'soysauce', 'spaghetti', 'spareribs', 'spatula', 'spices', 'spinach', 'spoon', 'spork', 'sprinkles', 'sprouts', 'spuds', 'squash', 'squid', 'steak', 'stew', 'stir-fry', 'stomach', 'stove', 'straw', 'strawberry', 'string', 'bean', 'stringy', 'strudel', 'succotash', 'sugar', 'summer', 'squash', 'sundae', 'sunflower', 'supper', 'sushi', 'sweet', 'sweet', 'potato', 'Swiss', 'chard', 'syrup', 'taco', 'take-out', 'tamale', 'tangerine', 'tapioca', 'taro', 'tarragon', 'tart', 'tea', 'teapot', 'teriyaki', 'thyme', 'toast', 'toaster', 'toffee', 'tofu', 'tomatillo', 'tomato', 'torte', 'tortilla', 'tuber', 'tuna', 'turkey', 'turmeric', 'turnip', 'ugli', 'fruit', 'unleavened', 'utensils', 'vanilla', 'veal', 'vegetable', 'venison', 'vinegar', 'vitamins', 'wafer', 'waffle', 'walnut', 'wasabi', 'water', 'water', 'chestnut', 'watercress', 'watermelon', 'wheat', 'whey', 'whipped', 'cream', 'wok', 'yam', 'yeast', 'yogurt',
                'yolk', 'zucchini']

transport_vocab = """
aircraft
aircraft carrier
airplane
ambulance
amphibious vehicle
armored car
auto
automobile


baby carriage
balloon
bathyscaphe
barge
battleship
bicycle
bike
biplane
blimp
boat
bobsled
bomber
boxcar
broomstick
buggy
bulldozer
bullet train
bus


cab
cabin cruiser
cable car
caboose
camper
canoe
car
caravan
caravel
cargo ship
carriage
carrier
cart
catamaran
chair lift
chariot
chopper
clipper ship
clunker
coach
compact car
combine
compact car
Conestoga wagon
container ship
convertible
conveyance
conveyor belt
convoy
coupe
covered wagon
crane
crop duster
cruise ship
cruiser
cutter
cycle


delivery truck
delivery van
destroyer
diesel truck
dinghy
dirigible
dirt bike
diving bell
dog cart
dogsled
donkey cart
dray
driver
dugout canoe
dump truck


earth mover
eighteen-wheeler
electric car
elevated railroad
elevator
engine
escalator
express train


ferry
fireboat
fire engine
fishing boat
flatbed truck
forklift
four-wheel drive
freighter
freight train
frigate
funicular railway


galleon
garbage truck
glider
go-cart
golf cart
gondola
gondola lift
gridlock


handcar
hang glider
hansom cab
harvester
haul
hay wagon
hearse
helicopter
hook and ladder truck
hovercraft
horse carriage
hot-air balloon
hot rod
houseboat
hull
humvee
hybrid
hydrofoil
hydroplane


ice boat
ice breaker


jeep
jet
jet boat
jetliner
journey
jet pack
jet ski
jumbo jet
junk


kayak
ketch


landing craft
lifeboat
life raft
light rail
limo
limousine
litter
locomotive
lorry


magic carpet
maglev
mast
minesweeper
minibus
minivan
model T
monorail
moped
motor
motorboat
motorcycle
motor home
mountain bike


narrowboat


oar
ocean liner
off-road vehicle
oil tanker
outboard motor
outrigger canoe
oxcart


paddle
paddlewheeler
parachute
passenger
patrol car
pedal boat
pickup truck
pilot
plane
police car
power boat
prairie schooner
propeller
PT boat
pumper truck
punt
push cart


racecar
raft
railroad
railway
rapid transit
recreational vehicle
rickshaw
ride
riverboat
roadster
rocket
rover
rowboat
rudder
runabout
RV


sail
sailboat
satellite
school bus
schooner
scooter
scull
seaplane
sedan
sedan chair
Segway
semi
ship
side wheeler
skiff
ski lift
sled
sledge
sleigh
snow cat
snowmobile
snowplow
spaceship
space shuttle
speedboat
squad car
SST
stagecoach
station wagon
steamboat
steamship
stock car
stroller
submarine
submersible
subway
surrey
SUV


tank
tanker
taxi
taxicab
thresher
tire
toboggan
town car
tow truck
tractor
tractor-trailer
trail bike
trailer
train
tram
transit
trawler
tricycle
trolley
truck
tugboat


U-boat
ultralight craft
unicycle


van
vehicle
vespa
vessel


wagon
warship
wheel
wheelbarrow
wheelchair
windjammer
wreck


yacht


Zamboni
zeppelin
""" 

culture_vocab = """ society
civilization
philosophy
anthropology
subculture
acculturation
religion
cultivation
nationalism
counterculture
cultural
ideology
art
popular culture
folklore
agriculture
country
writing
music
monoculture
cyberculture
language
social class
high culture
cultural studies
cultural anthropology
cooking
literature
science
growth
tillage
grow
ritual
perfection
development
metaphor
concept
symbol
mythology
gender
tradition
archaeology
clothing
edward burnett tylor
traditions
traditional
western culture
contemporary
multiculturalism
elite
politics
ethnicity
heritage
sociology
modernity
spirituality
marxism
material culture
low culture
mass culture
critical theory
ethos
nationality
humanism
romanticism
finish
polish
refinement
civilisation
traditionalism
genetics
human
learning
interaction
kinship
heredity
marriage
dance
technology
shelter
indigenous peoples of the americas
growing
biology
starter
viticulture
discernment
content
maturation
appreciation
ontogeny
archeology
attitude
taste
letters
institutions
humanities
acculturate
jewelry
flawlessness
perceptiveness
ontogenesis
viniculture
meme
modern
capitalism
clothes
cultures
social
intellectual
especially
nature
religious
rooted
context
cicero
societies
popular
history
literary
roots
influenced
influences
important
geography
historical
folk
particular
origins
phenomenon
teleology
ancient
aspects
perspective
particularly
rousseau
architecture
terror management theory
life
inspired
liberalism
influence
landscape
flourishing
urban
circles
everyday
refers
foremost
ideas
aesthetics
thriving
indigenous
peoples
such
famous
example
latin
known
chinese
describe
nowadays
community
style
knowledge
unique
prevalent
describes
environment
classical
today
common
origin
interests
great
behavioral modernity
most
besides
well
beliefs
importance
emphasis
kind
understanding
themes
genre
political
regarded
idea
schema
barbarian
ruling class
social group
diffusion
hamburger
ethnic
cultivate
colonization
cultural universals
developmental
social organization
paleo-american culture
mycenaean culture
mycenaean civilization
mycenaean civilisation
minoan culture
minoan civilization
minoan civilisation
indus civilization
helladic culture
helladic civilization
helladic civilisation
aegean culture
aegean civilization
aegean civilisation
ne plus ultra
mosaic culture
kalashnikov culture
mental attitude
mental object
cognitive content
western civilization
paleo-indian culture
paleo-amerind culture
biological science
cranberry culture
political organization
bildung
ism
vegetate
agriculturist
regrow
degrowth
germany
outgrowth
structuralism
excrescence
polyp
oral literature
intangible cultural heritage
structuration
grower
the arts
cultivator
naturalism
psychogenesis
outgrow
naturism
cultivable
ontogenetic
folk culture
tumor
zionism
maturational
ingrowth
cultural capital
growthful
body modification
humanist
hindu
heathen
pagan
hebraic
transculturation
media culture
peasant
classicist
nativism
mass production
anarchy
ungrown
mass media
misgrow
intergrown
consumer culture
growingly
ist
patriotism
formalism
farmer
ingrow
philosophic
cult
false consciousness
islamist
growable
evolutionary
underdevelopment
intergrow
social sciences
dysplasia
cultural materialism
germinate
hypertrophy
uncultivated
germination
human evolution
evolution
innate
sophistication
proliferation
sanskrit
cultivar
serer
count noun
civilize
vegetal
hinduism
japan
nationalist
vegetation
gentile
national
doctrine
assyrian
proliferate
bro culture
authenticity
nationally
evolve
cultic
diaspora
aftergrowth
classic
native
agricultural
till
sunni
nation
cultural relativism
morphogenesis
mongolian
ancient rome
taoism
teethe
cosmopolitan
develop
epistemology
husbandry
hindustan
economic
undeveloped
islamic
latitudinarian
americana
mores
folkways
ethic
milieu
mentality
consumerism
individualism
ritualism
sensibility
mindset
cosmopolitanism
cuisine
individualities
syncretism
idiom
attitudes
iconography
psyche
stereotypes
lifestyles
diversity
chauvinism
westernization
materialism
vernacular
perception
homogeneity
otherness
holism
tusculanae disputationes
primitivism
commercialism
superficiality
hedonism
discourse
puritanism
modernism
intellectualism
decadence
exclusiveness
elitism
provincialism
colonialism
experience
rustic
taoist
compatriot
fundamentalism
pentecostalism
agrarian
paganism
nationwide
expansion
rural
sabaean
environmentalism
naturalist
grange
auxesis
kimono
culturize
cytogenesis
samuel pufendorf
formalistic
metalinguistics
overcrop
burgeon
age of enlightenment
crescentic
overgrow
cultural invention
cultist
world population
forgrow
beanfield
overwax
culture change
social structure
flower
aesthete
intercrop
forwax
overyielding
japanophilia
generative actor
paleocontact
forthwax
feminist movement
supremacism
malthusianism
ice age
hermeticism
accretive
francophile
maizefield
alethophobia
diffusion of innovations
nettlebed
japanification
underdevelop
dongyi
clannishness
insularity
hybridity
westernisation
foreignness
worldview
exclusionism
enculturation
ethnocentrism
permissiveness
confucianist
vulgarization
shintoism
indianism
westernism
denominationalism
homogeny
peoplehood
philistinism
entrepreneurialism
deracination
artisanship
eurocentrism
institutionalism
cosmologies
agrarianism
emotiveness
bohemianism
territorialism
foodways
snobbism
parochialism
ethnos
patriarchic
latinization
nomadism
druidism
agroecosystem
sociolinguistics
macumba
durkheim
accrete
cultural assimilation
immanuel kant
johann gottfried herder
wilhelm von humboldt
grow op
austro-hungarian empire
world view
get big
adolf bastian
franz boas
english people
matthew arnold
german people
communication
ethnic group
european classical music
dialect
haute cuisine
rice grow
yellow horde
fashion
psychoanalysis
globalization
company
immigrant
marxist
value
power
hegemony
feminist
film
photography
hairstyle
fandom
philosophical doctrine
life cycle
thomas hobbes
ethnic minority
jean-jacques rousseau
herbert spencer
social darwinism
lewis henry morgan
system theory
cultural evolution
belief system
folk music
indigenous peoples
noble savage
develop product
paddy field
bed in
humanistic discipline
oyster bed
monetary gain
medicine wheel
ethical investment
evolution of religion
political orientation
raise crop
neo druidism
stuart hall
melting pot
traditional art
sunday house
grow corn
national treasure
politically correct
biological anthropology
raymond williams
linguistic anthropology
sociology of culture
georg simmel
non-material culture
weimar germany
alfred weber
cultural turn
postmodern philosophy
cultural analysis
social stratification
social network
social psychology
cognitive science
karl marx
japanese tea ceremony
max weber
relations of production
atlantic canada
richard hoggart
centre for contemporary cultural studies
paul willis
dick hebdige
angela mcrobbie
political economy
social theory
literary theory
media influence
film theory
art history
museum studies
means of production
cultural artifact
raimon panikkar
french feminism
louis althusser
paul gilroy
culture industry
cultural change
frankfurt school
julia kristeva
left-wing politics
university of birmingham
e. p. thompson
united states
united kingdom
comparative literature
comparative cultural studies
griselda pollock
written language
"""






ps = nltk.PorterStemmer()
words=[ps.stem(word) for word in culture_vocab.split()]

print(set(words))
