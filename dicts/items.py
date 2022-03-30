from dicts.player import player

GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
DESCWORDS = 'descwords'
TAKEABLE = 'takeable'
USABLE = 'usable'
EDIBLE = 'edible'
DRINKABLE = 'drinkable'
VISIBLE = 'visible'
TRIGGER = 'trigger'
NAME = 'name'

"""
STATUSEFFECT = 'statuseffect'
BUYPRICE = 'buyprice'
SELLABLE = 'sellable'
SELLPRICE = 'sellprice'
"""

worldItems = {
	'Welcome Sign': {
		GROUNDDESC: 'A welcome sign stands in front of the fountain.',
		SHORTDESC: 'the welcome sign', # REQUIRED | change all 'a' to 'the' if game allows
		LONGDESC: 'The welcome sign reads, "Welcome, {}. You can type "help" for a list of commands to use. Good luck on your travels"'.format(player[NAME]), # REQUIRED | Add user input in format spacing
		TAKEABLE: False,
		DESCWORDS: ['welcome', 'sign']
		},
	'Do Not Pass Sign': {
		GROUNDDESC: 'A sign stands on the ground.',
		SHORTDESC: 'the sign',
		LONGDESC: 'The sign reads, "You shall not pass"',
		DESCWORDS: ['sign']
		},
	'Fountain': {
		GROUNDDESC: 'A large fountain is placed in the center of the Town.',
		SHORTDESC: 'the fountain',
		LONGDESC: 'The fountain has water clear water flowing from the top.',
		TAKEABLE: False,
		DESCWORDS: ['fountain']
		},
	'GM House Doormat': {
		GROUNDDESC: 'A Doormat',
		SHORTDESC: 'the doormat',
		LONGDESC: 'The doormat is laying on the ground and has been revealed to have a key under it.',
		TAKEABLE: False,
		TRIGGER: 'GM mat w/ Key',
		DESCWORDS: ['doormat', 'mat']
		},
	'Wet Floor Sign': {
		GROUNDDESC: 'A wet floor sign',
		SHORTDESC: 'the wet floor sign',
		LONGDESC: 'A bright yellow sign that spells out "Wet Floor!". You notice that the floor around it looks a little moist.',
		TAKEABLE: False,
		DESCWORDS: ['sign', 'wet floor sign']
		},
	'GM House Key': {
		GROUNDDESC: 'A key hidden under the doormat for GMs house.',
		SHORTDESC: 'a key to GMs house',
		LONGDESC: 'The key is used for unlocking GMs house. What secrets lie behind his door?',
		USABLE: True,
		VISIBLE: False,
		DESCWORDS: ['house key', 'door key', 'gm key', 'key']
		},
	'Managers Office Key': {
		GROUNDDESC: 'Office key',
		SHORTDESC: 'the office key',
		LONGDESC: 'A key to unlock the office door in the shop',
		DESCWORDS: ['managers key', 'office key', 'key']
		},
	'Papers': {
		GROUNDDESC: 'some papers',
		SHORTDESC: 'the papers',
		TRIGGER: 'Documents Lore',
		LONGDESC: 'Some important papers in a folder that reads "Classified". You take out the documents to read them. "Secret plan change all currencies to pant. If all the currencies are pant, the GM will not manage to live off of others\' money. On average, he earns 200$ a day just from having people give him pant. And he is wasting it on those stupid anemai action figures or whatever they are."',
		DESCWORDS: ['papers', 'documents', 'paper']
		},
	'Astolfo Figurine': {
		GROUNDDESC: 'An anime figurine of Astolfo.',
		SHORTDESC: 'an anime figurine',
		LONGDESC: 'The anime figurine is a character from "Fate/Grand Order" named Astolfo. It has pink hair, purple eyes and is wearing a white and pink sailers uniform. How cute she looks.',
		TAKEABLE: False,
		DESCWORDS: ['astolfo figurine', 'astolfo figure', 'astolfo']
		},
	'Ainz Ooal Gown Figurine': {
		GROUNDDESC: 'An anime figurine of Ainz Ooal Gown.',
		SHORTDESC: 'the Ainz Ooal Gown figurine',
		LONGDESC: 'The anime figurine is a character from "Overlord" named Ainz Ooal Gown. He is an undead who has maxed out his level and equipment in a video game, and then gets transported to the game world where he rules his own dungeon.',
		TAKEABLE: False,
		DESCWORDS: ['ainz figurine', 'ainz ooal gown figurine', 'ainz figure', 'ainz ooal gown figure', 'ainz', 'ainz ooal gown', 'momonga']
		},
	'Kanna Figurine': {
		GROUNDDESC: 'A big anime figurine of Kanna.',
		SHORTDESC: 'a big anime figurine',
		LONGDESC: 'The anime figurine is a character from "Miss Kobayashi\'s Dragon Maid" named Kamui Kanna. The figurine is 1:1 sized meaning it is 1.5m tall. She looks like a cute little girl, but is in fact a dragon who is 7000 years old.',
		TAKEABLE: False,
		DESCWORDS: ['kanna figurine', 'kamui kanna figurine', 'kanna figure', 'kamui kanna figure', 'kanna', 'kamui kanna', 'kanna kamui']
		},
	'Bed': {
		GROUNDDESC: 'A bed',
		SHORTDESC: 'the bed',
		LONGDESC: 'A piece of Furniture for sleep or rest. There is a framework with a mattress.',
		TAKEABLE: False,
		DESCWORDS: ['bed']
		},
	'Junk': {
		GROUNDDESC: 'Some junk',
		SHORTDESC: 'the junk',
		LONGDESC: 'It is the same as a Bri\'ish person.', 
		DESCWORDS: ['junk', 'garbage', 'trash']
		},
	'Swedish Pant': {
		GROUNDDESC: 'A suspicious looking pant',
		SHORTDESC: 'the suspicious pant',
		LONGDESC: 'The Pant, after further inspection, is Swedish Pant. It is therefore useless since it cannot be panted in the Pant machine.',
		DESCWORDS: ['swedish pant', 'fake pant' 'suspicious pant', 'sus pant']
		},
	'Pant': {
		GROUNDDESC: 'A Pant.',
		SHORTDESC: 'the pant',
		LONGDESC: 'The Pant is a sacred item in this town, but that is only true for one person. It can be exchanged for money in the Pant machine in the Pant Room.',
		USABLE: True,
		DESCWORDS: ['pant', 'empty bottle', 'empty spirit', 'spirit']
		},
	'Pant Note': {
		GROUNDDESC: 'A Pant note.',
		SHORTDESC: 'the Pant note',
		LONGDESC: 'An important form of valuta in this town (according to the GM who is the only one who uses it). You buy plastic bottles for 3$ extra, BUT you receive 3$ when returning the bottle. You don\'t earn any money from it? Haha, you only have to get pant from others. That way, they spent the 3$, and you receive it.',
		USABLE: True,
		DESCWORDS: ['pant note', 'note']
		},
	'Spirit': {
		GROUNDDESC: 'A bottle of spirit',
		SHORTDESC: 'the bottle of spirit',
		LONGDESC: 'Spirit, It\'s a sprite-like soda, but cheaper and better tasting. After drinking it, it turns into pant.',
		DRINKABLE: True,
		DESCWORDS: ['spirit', 'soda', 'bottle']
		},
	'Monkey': {
		GROUNDDESC: '???',
		SHORTDESC: 'the monkey?',
		LONGDESC: 'A monkey that... Uhhh. How did you get this? You aren\'t even supposed to be able to obtain this. It belongs to \'RandomBoii\'',
		EDIBLE: True,
		DESCWORDS: ['monkey', 'monk', 'ape']
		},
	'Town Barrier': {
		GROUNDDESC: 'a Barrier',
		SHORTDESC: 'the barrier',
		LONGDESC: 'The barrier is blocking the northern town exit. You think to yourself "This game probably has a lazy developer who doesn\'t care to put something up there, so he just blocks it off with a barricade".',
		TAKEABLE: False,
		DESCWORDS: ['barrier', 'barricade', 'blockade', 'roadblock', 'fence', 'fencing']
		},
	'Ground Tiles': { # REQUIRED | This is a trigger for Finale
		GROUNDDESC: 'tiles',
		SHORTDESC: 'the tiles',
		LONGDESC: 'All the titles on the ground are perfectly aligned. Since the GM cannot stand things that do not look perfect, he takes his time perfecting everything he sees as "unperfect". Title-by-Title. Inch-by-Inch.',
		TAKEABLE: False,
		DESCWORDS: ['tile', 'tile', 'ground', 'ground tiles']
		},
	}