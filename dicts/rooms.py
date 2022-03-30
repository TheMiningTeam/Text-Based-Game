DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
CHEST = 'chest'
SHOP = 'shop'
NPCS = 'npcs'

worldRooms = {
	# ===== Town ===== #
	'Town Square' : {
		DESC: 'The town square has a large open space with a fountain in the center. Streets lead in all directions. There is a little garden area with benches for everyone to use and a playground for the kids.',
		NORTH: 'North Street',
		EAST: 'East Street',
		SOUTH: 'South Street',
		WEST: 'West Street',
		NPCS: ['Greg'],
		GROUND: ['Welcome Sign', 'Fountain']
		},
	'North Street': {
		DESC: 'The Northern Street is as cozy as ever. The tiles are better here than in the rest of town. This street has a barrier preventing people from leaving town. To your left is the GM\'s house with a doormat infront of the door, but it is locked at all times so that no one can enter. The armory, on the other hand, is unlocked and open for all to stop by and peruse.',
		EAST: 'Armory',
		SOUTH: 'Town Square',
		NPCS: [],
		GROUND: ['Do Not Pass Sign', 'GM House Doormat', 'GM House Key', 'Town Barrier', 'Ground Tiles']
		},
	'GM House': {
		DESC: 'The GMs house is filled with weeb stuff. Walls have posters of LEGAL loli girls, a desk full of Figurines, and in the middle of the room, a gigantic 1:1 Kanna Figurine that is half your height. And then there is all the spirit laying all around the room. Truly a masterpiece.',
		SOUTH: 'West Street',
		EAST: 'North Street',
		NPCS: [],
		GROUND: ['Astolfo Figurine', 'Ainz Ooal Gown Figurine', 'Spirit', 'Spirit', 'Spirit'] # Add some money on the ground here
		},
	'Armory': {
		DESC: 'Shiny armor pieces are on display around the armory.  It\'s a little bit of a small place, but the warm air and smell of iron being melted fill you with a comforting warmth.  The metal countertop has a great look to it, and a giant white shield with the sword as a side feature was nice too.',
		WEST: 'North Street',
		SOUTH: 'East Street',
		NPCS: [],
		GROUND: [] # Some money # REQUIRED
		},
	'West Street': {
		DESC: 'The beautiful west street, filled with lots of different colored flowers and a lot of lovely buildings such as the hhgregg store and your house.  You can\'t brag too much about it being so nice since it is mainly hhgregg\'s employees who decorate the street. The GM sometimes even stops by to help them out whit their Appapplianceses since they tend to be a little heavy. Though, he is extremely weak, and can\'t do that much.',
		EAST: 'Town Square',
		SOUTH: 'hhgregg',
		WEST: 'Home',
		NPCS: ['Hilda'],
		GROUND: []
		},
	'Home': {
		DESC: 'Your house. It is as ugly as ever, and it becomes even uglier when you ente-- I mean It becomes remarkably prettier when you enter. There is a is a chest that you can use for storing items. Just use "store"',
		EAST: 'West Street',
		NPCS: [],
		GROUND: ['Junk', 'Junk', 'Bed', 'Junk', 'Junk', 'Junk'],
		CHEST: ['Pant', 'Junk', 'Spirit']
		},
	'East Street': {
		DESC: 'The most heavily guarded part of the town, east street. It is guarded so that the monsters from the forest don\'t come and ravage the town. This street has access to both of the adventurer shops; The Armory and The Weaponry. Quality items are sold at both paces at reasonable prices. Near the edge ',
		NORTH: 'Armory',
		EAST: 'Election Room',
		WEST: 'Town Square',
		SOUTH: 'Weaponry',
		NPCS: [],
		GROUND: []
		},
	'Weaponry': {
		DESC: 'Weapons hang all over the walls in the Weaponry. Many different types of weapons are on display. Each of the weapons in the Weaponry has its unique appearance.',
		NORTH: 'East Street',
		# SHOP: ['Copper Sword', 'Iron Sword', 'Gold Sword', 'Tungsten Sword', 'Platinum Sword', 'Mythril Sword', 'Orichalcum Sword', 'Adamantite Sword', 'Titanium Sword'], # REQUIRED
		NPCS: [],
		GROUND: [] # REQUIRED
		},
	'hhgregg': {
		DESC: 'hhgregg has Appapplianceses like Refrididigererators, Washashing Machinines, Furnurnitures like Couchoucheses, Tabables and don\'t forget their great Appapparellels like Panantans, Tee-Tee Shirshirturtses and Ninylonen Jackackacketses. hhgregg "We\'ve got ALL the thhingingses"',
		NORTH: 'West Street',
		EAST: 'South Street',
		SHOP: [], # REQUIRED
		NPCS: [],
		GROUND: [] # REQUIRED
		},
	'South Street': {
		DESC: 'The only street that [something someting], south street. People tend to rush down this street when there is a special "Town Sale". Whenever there is a Town Sale, all stores set down their prices by 50%. How are they still in business? The GM help fund this. And since not that many people in this town are adventurers, they mostly buy food, appapplianceses, furnurnitures, and other everyday necessities. South of this street is the Dungeon. That is the hardest place in this ga-- Uhm, I mean The most terrifying place in the world!', # REQUIRED | We cannot have [Something something] when we are done.
		NORTH: 'Town Square',
		EAST: 'Store',
		WEST: 'hhgregg',
		NPCS: [],
		GROUND: []
		},
	'Election Room': {
		DESC: 'There is a big room filled with chairs and a pedestal. A poster on the wall reads "THE BIG ELECTION IS TODAY". The Store manager is standing near the pedestal.',
		WEST: 'East Street',
		NPCS: ['Manager'],
		GROUND: []
		},
	'Store': {
		DESC: 'The Store is filled with different kinds of wares. All the shelves are fully stocked and the floor as clean as can. Soft music is playing in the background. The smell of fresh air from the AC is comforting. The music carries you into the store of great joy.',
		NORTH: 'East Street',
		EAST: 'Pant Room',
		WEST: 'South Street',
		UP: 'Managers Office',
		SHOP: ['Spirit'], # Add stuff to purchase
		NPCS: [],
		GROUND: ['Managers Office Key', 'Wet Floor Sign']
		},
	'Pant Room': {
		DESC: 'The holy room where all pant is recycled. You even receive money just for putting pant inside of the HUGE machine. You can feel a force pulling you towards it, wanting you to stuff it with pant.',
		WEST: 'Store',
		NPCS: [],
		GROUND: ['Swedish Pant', 'Swedish Pant', 'Pant Note']
		},
	'Managers Office': {
		DESC: 'You walk into the manager\'s office. The room has multiple filing cabinets and comfortable carpet flooring. On my desk are multiple sheets of paper. The one that caught your attention was the one that had the word "Classified" written over it. ',
		DOWN: 'Store',
		NPCS: [],
		GROUND: ['Papers']
		},
	}