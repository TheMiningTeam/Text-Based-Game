#! python3
"""
Text Based RPG Game by TheMiningTeam.

This game is a text based RP-- Adventure game that uhh... Is in beta, demo and
early access all at the same time. Don't think too hard about it, ok?

You "spawn" in the center of the town and you are able to walk around, interact
and look at items and ehm... idk. I wasted a lot of my time trying to figure
out how PyGame worked, and now I am here. My deadline for this game is tomorrow,
and it was supposed to be displayed in PyGame (wich I regret). This was
all too much for me to do with only four weeks where I am supposed to do
this at school, but ended up doing more at home.
"""

from dicts.npcs import worldNPCS
from dicts.rooms import worldRooms
from dicts.items import worldItems
from dicts.triggers import worldTriggers
from dicts.player import player

"""
Helper Variables
"""
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
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
USABLE = 'usable'
DAMAGE = 'damage'
DEFENCE = 'defence'
BUYPRICE = 'buyprice'
SELLABLE = 'sellable'
SELLPRICE = 'sellprice'
EDIBLE = 'edible'
DRINKABLE = 'drinkable'
STATUSEFFECT = 'statuseffect'
DESCWORDS = 'descwords'
VISIBLE = 'visible'
LOOKTRIGGER = 'looktrigger'
NAME = 'name'

NPCS = 'npcs'
NPCNAME = 'npcname'
NPCGREETING = 'npcgreeting'
NPCOPTIONS = 'npcoptions'
NPCDIALOG = 'npcdialog'
DIALOG = 'dialog'
TRIGGER = 'trigger'
NOTRIGGER = 'notrigger'
SECRET = 'secret'
ONE = 'one'
TWO = 'two'
THREE = 'three'
FOUR = 'four'
FIVE = 'five'
SIX = 'six'
NPCGOODBYE = 'npcgoodbye'
ACTIVE = 'active'
HIDDEN = 'hidden'

LVL = 'lvl'
NEXTLVL = 'nextlvl'
XP = 'xp'
XPDROP = 'xpdrop'
STATS = 'stats'
MAXHP = 'maxhp'
HP = 'hp'
ATK = 'atk'
DEF = 'def'
MONEY = 'money'

HEALTHBOOST = 'healthboost'
SMALLHEAL = 'smallheal'
HALFHEAL = 'halfheal'
FULLHEAL = 'fullheal'


SCREEN_WIDTH = 80

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f'{bcolors.WARNING}Welcome to the Text Based Game!')
answer = ''
while answer != 'y':
	player[NAME] = input('Before we start, please state your name, brave adventurer. \n>')
	if player[NAME] == '':
		continue
	answer = input("\nAre you sure that '%s' is your name? Y/N. \n>" % (player[NAME])).lower()





from lib import cmd, textwrap
import sys


dogeMessage = [
	'much awsomness', # 0
	'much pain', # 1
	'much sad', # 2
	'many wow', # 3
	'such amaze', # 4
	'such way', # 5
	'such numbers', # 6
	'such delishus', # 7
	'such skill', # 8
	'so currency', # 9
	'so shine', # 10
	'so talent', # 11
	'so talent', # 12
	'how pronounce', # 13
]
errorMessage = 'Sorry, I don\'t quite understand'
worldMap = """
                      Barrier
                      |=====|
            ###########     #############################
            #  GM's   #  N  #           #				#
            #  House  |     |   Armory  #	Election-	#
            #         #     #           #	room		#
    ###################     #####ー########ー#############
    #       #                           				#
    #  Home #  W     Town Square   E         ############
    #       |                                |          #
    ##############ー####    #####ー###########  Weapo-  #
             #  hhgr-  |  S |                #   nry    #
             #  egg    #    #      Store     ############
             #         #    #                #
             ###########    ##################
    
                       Dungeon
"""
location = 'Town Square'
inventory = ['Junk', 'Spirit']
weapon, armor = [], []
equipment = [armor, weapon]
userConfirmation = None


def displayLocation(loc):
	"""A helper function for displaying an area's description and exits."""
	print(loc)
	print('=' * len(loc))

	# Print the room's description (using textwrap.wrap())
	print('\n'.join(textwrap.wrap(worldRooms[loc][DESC], SCREEN_WIDTH)))

	if len(worldRooms[loc][GROUND]) > 0:
		print()
		for item in worldRooms[loc][GROUND]:
			if worldItems[item].get(TAKEABLE, True) == False or worldItems[item].get(VISIBLE, True) == False:
				continue
			print(worldItems[item][GROUNDDESC])

	# Print all the exits.
	exits = []
	for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
		if direction in worldRooms[loc].keys():
			exits.append(direction.title())
	print()
	for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
		if direction in worldRooms[location]:
			print('To your %s, you see %s.' % (direction.title(), worldRooms[location][direction]))

def moveDirection(direction):
	"""A helper function that changes the location of the player."""
	global location

	if direction in worldRooms[location]:
		print('You move to the %s.' % direction)
		location = worldRooms[location][direction]
		displayLocation(location)
	else:
		print(errorMessage)

def getAllDescWords(itemList):
	"""Returns a list of "description words" for each item named in itemList."""
	itemList = list(set(itemList)) # make itemList unique
	descWords = []
	for item in itemList:
		descWords.extend(worldItems[item][DESCWORDS])
	return list(set(descWords))

def getAllFirstDescWords(itemList):
	"""Returns a list of the first "description word" in the list of
	description words for each item named in itemList."""
	itemList = list(set(itemList)) # make itemList unique
	descWords = []
	for item in itemList:
		descWords.append(worldItems[item][DESCWORDS][0])
	return list(set(descWords))

def getFirstItemMatchingDesc(desc, itemList):
	itemList = list(set(itemList)) # make itemList unique
	for item in itemList:
		if desc in worldItems[item][DESCWORDS]:
			return item
	return None

def getAllItemsMatchingDesc(desc, itemList):
	itemList = list(set(itemList)) # make itemList unique
	matchingItems = []
	for item in itemList:
		if desc in worldItems[item][DESCWORDS]:
			matchingItems.append(item)
	return matchingItems

def getFirstNPC(npcName, npcList):
	npcList = list(set(npcList)) # make itemList unique
	matchingNames = []
	for name in npcList: # Checking all NPCs in the list (list is current locations NPCs)
		for npcAlias in worldNPCS[name][NPCNAME]: # Checking all NPC aliases
			matchingNames.append(npcAlias)
			return matchingNames
	return matchingNames

def listNPCOptions(npc):
	optionNum = 1
	for option in npc[NPCOPTIONS]:
		if npc[NPCOPTIONS][option].get(HIDDEN, False) == False:
			print('%s. %s' % (optionNum, npc[NPCOPTIONS][option][DIALOG]))
			optionNum += 1
	return

class TextAdventureCmd(cmd.Cmd):
	prompt = '\n>'

	# The default() method is called when none of the other do_*() command methods match.
	def default(self, arg):
		print(errorMessage)

	def do_quit(self, arg):
		"""Quit the game."""
		return True # this exits the Cmd application loop in TextAdventureCmd.cmdloop()

	def do_help(self, arg):
		print('Help list:')
		print('==========')
		print('Directions: North, East, South, West, Up, Down')
		print('Look   Use   Take   Talk   Map   Drink   Eat')
		print('Inventory   Balance   Buy   Sell   List\n')

	def help_store(self):
		print('There are three stores in the town; The Store, The Armory and The Weaponry.')
		print('\nYou can buy and sell certain items. To learn more about the commands, do "help buy" or "help sell". "List" is used to list the shops items.')

	def do_north(self, arg):
		"""Go to the area to the north, if possible."""
		moveDirection('north')

	def do_south(self, arg):
		"""Go to the area to the south, if possible."""
		moveDirection('south')

	def do_east(self, arg):
		"""Go to the area to the east, if possible."""
		moveDirection('east')

	def do_west(self, arg):
		"""Go to the area to the west, if possible."""
		moveDirection('west')

	def do_up(self, arg):
		"""Go to the area upwards, if possible."""
		moveDirection('up')

	def do_down(self, arg):
		"""Go to the area downwards, if possible."""
		moveDirection('down')


	do_North = do_north
	do_N = do_north
	do_n = do_north
	do_East = do_east
	do_E = do_east
	do_e = do_east
	do_West = do_west
	do_W = do_west
	do_w = do_west
	do_South = do_south
	do_S = do_south
	do_s = do_south
	do_Up = do_up
	do_U = do_up
	do_u = do_up
	do_Down = do_down
	do_D = do_down
	do_d = do_down
	
# Inventory Stuff
	def do_inventory(self, arg):
		"""Display a list of the items in your possession."""

		if len(inventory) == 0:
			print('Inventory:\n  (nothing)')
			return

		itemCount = {}
		for item in inventory:
			if item in itemCount.keys():
				itemCount[item] += 1
			else:
				itemCount[item] = 1

		# get a list of inventory items with duplicates removed:
		print('Inventory:')
		for item in set(inventory):
			if itemCount[item] > 1:
				print('  %s x %s' % (item, itemCount[item]))
			else:
				print('  ' + item)

	do_inv = do_inventory

	def do_talk(self, arg):
		""""talk <person>" - Talk to someone if they are within range."""

		npcToTalkTo = arg.title()

		if npcToTalkTo == '':
			print(errorMessage)
			return

		if npcToTalkTo in getFirstNPC(npcToTalkTo, worldRooms[location][NPCS]):
			TalkingToNPC.active = worldNPCS[npcToTalkTo]
			listNPCOptions(TalkingToNPC.active)
			TalkingToNPC().cmdloop()
			return

		print(errorMessage)

	def do_take(self, arg):
		""""take <item>" - Take an item on the ground."""

		itemToTake = arg.lower()

		if itemToTake == '':
			print(errorMessage)
			return

		for item in getAllItemsMatchingDesc(itemToTake, worldRooms[location][GROUND]):
			if worldItems[item].get(TAKEABLE, True) == False or worldItems[item].get(VISIBLE, True) == False:
				continue
			print(f'You take {bcolors.ENDC}' + (worldItems[item][SHORTDESC] + f'{bcolors.WARNING}'))
			worldRooms[location][GROUND].remove(item)
			inventory.append(item)
			return

		print(errorMessage)
			
	def do_give(self, arg): # REQUIRED | Remove before publishing!!!
		""""give <item>" - Gives you an item."""

		itemToGive = arg.lower()

		if itemToGive == '':
			print(errorMessage)
			return

		for item in getAllItemsMatchingDesc(itemToGive, worldItems):
			print('You get %s.' % (worldItems[item][SHORTDESC]))
			inventory.append(item)
			return

		print('You cannot get "%s".' % (itemToGive))

	def do_store(self, arg):
		""""store <item>" - Store an item from your inventory when you are in your house."""

		if worldRooms[location] != worldRooms['Home']:
			print('Sorry, but you need to be at Home store items. Your house is in the western part of the Town')
			return

		itemToDrop = arg.lower()

		invDescWords = getAllDescWords(inventory)

		if itemToDrop not in invDescWords:
			print(errorMessage)
			return

		item = getFirstItemMatchingDesc(itemToDrop, inventory)
		if item != None:
			print('You store %s.' % (worldItems[item][SHORTDESC]))
			inventory.remove(item)
			worldRooms[location][GROUND].append(item)

# Looking stuff
	def do_look(self, arg):
		"""Look at an item, direction, or the area:
"look" - display the current area's description
"look <direction>" - display the description of the area in that direction
"look exits" - display the description of all adjacent areas
"look <item>" - display the description of an item on the ground or in your inventory"""

		lookingAt = arg.lower()
		if lookingAt in ('around', ''):
			displayLocation(location)
			return

		if lookingAt == 'exits':
			for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
				if direction in worldRooms[location]:
					print('%s: %s' % (direction.title(), worldRooms[location][direction]))
			return

		if lookingAt in ('north', 'west', 'east', 'south', 'up', 'down', 'n', 'w', 'e', 's', 'u', 'd'):
			if lookingAt.startswith('n') and NORTH in worldRooms[location]:
				print(worldRooms[location][NORTH])
			elif lookingAt.startswith('w') and WEST in worldRooms[location]:
				print(worldRooms[location][WEST])
			elif lookingAt.startswith('e') and EAST in worldRooms[location]:
				print(worldRooms[location][EAST])
			elif lookingAt.startswith('s') and SOUTH in worldRooms[location]:
				print(worldRooms[location][SOUTH])
			elif lookingAt.startswith('u') and UP in worldRooms[location]:
				print(worldRooms[location][UP])
			elif lookingAt.startswith('d') and DOWN in worldRooms[location]:
				print(worldRooms[location][DOWN])
			else:
				print('There is nothing in that direction.')
			return

		# see if the item is a trigger on the ground at the current location
		for item in getAllItemsMatchingDesc(lookingAt, worldRooms[location][GROUND]):
			if worldTriggers[worldItems[item].get(TRIGGER, NOTRIGGER)][ACTIVE] == None:
				continue
			if item == 'GM House Doormat' and location == 'North Street' and worldTriggers['GM mat w/ Key'][ACTIVE] == False:
				worldTriggers['GM mat w/ Key'][ACTIVE] = True
				worldItems['GM House Key'][VISIBLE] = True
				print('You lift the doormat up and find a key.')
				return

			if item == 'Papers' and location == 'Managers Office' and worldTriggers['Documents Lore'][ACTIVE] == False:
				worldTriggers['Documents Lore'][ACTIVE] = True
				worldItems['Papers'][VISIBLE] = False
				print(worldItems['Papers'][LONGDESC])
				return
				
			return

		item = getFirstItemMatchingDesc(lookingAt, worldRooms[location][GROUND])
		if item != None:
			if worldItems[item].get(VISIBLE, True) == False:
				print(errorMessage)
				return
			print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))
			return

		item = getFirstItemMatchingDesc(lookingAt, inventory)
		if item != None:
			if worldItems[item].get(VISIBLE, True) == False:
				print(errorMessage)
				return
			print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))
			return

		print('You do not see that nearby.')

	def do_map(self, arg):
		""""map" - Displays a map of the Town"""
		print("Map:")
		print("===")
		print(worldMap)

# Use stuff
	def do_use(self, arg):
		""""use <item>" - Use an item on something"""
		
		itemToUse = arg.lower()
		
		item = getFirstItemMatchingDesc(itemToUse, inventory)
		if item != None:
			if worldItems[item].get(USABLE, False) == False:
				print(errorMessage)
				return

			if item == 'Pant' and location == 'Pant Room':
				pantCount = 0
				for item in inventory:
					if item == 'Pant':
						pantCount += 1
						inventory.remove(item)
						inventory.append('Pant Note')
				if pantCount > 1:
					print('You put %s x Pant into the Pant Machine. %s Pant Notes are dispenced out to you.' % (pantCount, pantCount))
				else:
					print('You put the Pant into the Pant Machine. A Pant Note is dispenced out to you.')
				return

		if worldTriggers['GM Door'][ACTIVE] == False: 
			if item == 'GM House Key':
				worldRooms['North Street'][DESC] = 'The Northern Street is as cozy as ever. The tiles are better here than in the rest of town. This street has a barrier preventing people from leaving town. To your left is the GM\'s house. The armory, on the other hand, is unlocked and open for all to stop by and peruse.'
				worldRooms['North Street'][WEST] = 'GM House'
				print('The door to GM\'s House is now unlocked')
				inventory.remove(item)
				return

		item = getFirstItemMatchingDesc(itemToUse, worldRooms[location][GROUND])
		if item != None:
			if worldItems[item].get(USABLE, False) == False:
				print(errorMessage)
				return
			print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))
			return
			
		
		print(errorMessage)
			
# Shop stuff
	def do_list(self, arg): # REQUIRED | Remane do_list
		"""List the items for sale at the current location's shop. "list full" will show details of the items."""
		if SHOP not in worldRooms[location]:
			print(errorMessage)
			return

		arg = arg.lower()

		print('For sale:')
		for item in worldRooms[location][SHOP]:
			print('  - %s' % (item))
			if arg == 'full':
				print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))


	def do_buy(self, arg):
		""""buy <item>" - buy an item at the current location's shop."""
		if SHOP not in worldRooms[location]:
			print(errorMessage)
			return

		itemToBuy = arg.lower()

		if itemToBuy == '':
			print(errorMessage)
			return

		item = getFirstItemMatchingDesc(itemToBuy, worldRooms[location][SHOP])
		if item != None: # REQUIRED | Money section
			# NOTE - If you wanted to implement money, here is where you would add
			# code that checks if the player has enough, then deducts the price
			# from their money.
			print('You have purchased %s' % (worldItems[item][SHORTDESC]))
			inventory.append(item)
			return

		print('"%s" is not sold here. Type "list" or "list full" to see a list of items for sale.' % (itemToBuy))

	def do_sell(self, arg):
		""""sell <item>" - sell an item at the current location's shop."""
		if SHOP not in worldRooms[location]:
			print('This is not a shop.')
			return

		itemToSell = arg.lower()

		if itemToSell == '':
			print(errorMessage)
			return

		for item in inventory:
			if itemToSell in worldItems[item][DESCWORDS]:
				# NOTE - If you wanted to implement money, here is where you would add
				# code that gives the player money for selling the item.
				print('You have sold %s' % (worldItems[item][SHORTDESC]))
				inventory.remove(item)
				return

		print(errorMessage)

	'''			# Money has yet to be implemented
	def do_balance(self, arg):
		""""balance" - Displays your current balance."""
		print('You have %s$.' % (player[MONEY]))
		if player[MONEY] > 10:
			print('Much wow') # REQUIRED | dogeMessage here with math. Maybe improve dogeMessage list?
			return
	do_bal = do_balance
	'''

	def do_eat(self, arg):
		""""eat <item>" - Eat an item from your inventory."""
		itemToEat = arg.lower()

		if itemToEat == '':
			print(errorMessage)
			return

		for item in getAllItemsMatchingDesc(itemToEat, inventory):
			if worldItems[item].get(EDIBLE, False) == False:
				continue
			print('You eat %s' % (worldItems[item][SHORTDESC]))
			inventory.remove(item)
			return

		print(errorMessage)

	def do_drink(self, arg):
		""""drink <item>" - Drink an item from your inventory."""
		itemToDrink = arg.lower()

		if itemToDrink == '':
			print(errorMessage)
			return

		for item in getAllItemsMatchingDesc(itemToDrink, inventory): # REQUIRED | Fix eating all at once. Problem is that it removes 'item', which is 'Spirit', and if there are multiple, all are used/removed at once
			if worldItems[item].get(DRINKABLE, False) == False:
				continue
			print('You drink %s' % (worldItems[item][SHORTDESC]))
			inventory.remove(item)
			inventory.append('Pant')
			return

		print(errorMessage)

	def do_election(self, arg):
		"""Used to start the election when in Election Room. This is irreversible."""
		if location != 'Election Room':
			print(errorMessage)
			return
		print('The election is starting and everyone is gathering.')
		input('\n"Press enter to continue"\n')
		print('The GM is the first on the podium.')
		input('\n"Press enter to continue"\n')
		print('GM: Elect me for mayor plz.')
		input('\n"Press enter to continue"\n')
		print('The GM stands down and up comes the Manager.')
		input('\n"Press enter to continue"\n')
		print('He has a long speech about all the great he will do for the town.')
		input('\n"Press enter to continue"\n')
		print('The odds of the GM being elected are near 0% now. You have to act if you want to help him out.')
		input('\n"Press enter to continue"\n')
		EndingSequence().cmdloop()

		
class TalkingToNPC(cmd.Cmd):
	"""TalkingToNPC.active is created each time when do_talk is called with a valid NPC which is the NPC that the player wants to talk to."""
	prompt = '\n> '

	# The default() method is called when none of the other do_*() command methods match.
	def default(self, arg):
		print(errorMessage)

	def do_quit(self, arg):
		"""Quit the game."""
		return True # This exits the Cmd application loop in TalkingToNPC.cmdloop()
	
	def do_help(self, arg):
		print('Help list:')
		print('==========')
		print('Goodybye   Options')
		print('1    2    3    4   etc.')
		print('==========')
		print('Use the corresponding number to say something to the NPC.\n')

	def do_1(self, arg):
		if 'one' in TalkingToNPC.active[NPCDIALOG]:
			print(TalkingToNPC.active[NPCDIALOG][ONE])
			if TalkingToNPC.active[NPCOPTIONS][ONE].get(TRIGGER, None) != None: # Check if there is a trigger
				worldTriggers[TalkingToNPC.active[NPCOPTIONS][ONE][TRIGGER]][ACTIVE] = True
			return
		print(errorMessage)

	def do_2(self, arg):
		if 'two' in TalkingToNPC.active[NPCDIALOG]:
			print(TalkingToNPC.active[NPCDIALOG][TWO])
			if TalkingToNPC.active[NPCOPTIONS][TWO].get(TRIGGER, None) != None: # Check if there is a trigger
				worldTriggers[TalkingToNPC.active[NPCOPTIONS][TWO][TRIGGER]][ACTIVE] = True
			return
		print(errorMessage)

	def do_3(self, arg):
		if 'three' in TalkingToNPC.active[NPCDIALOG]:
			print(TalkingToNPC.active[NPCDIALOG][THREE])
			if TalkingToNPC.active[NPCOPTIONS][THREE].get(TRIGGER, None) != None: # Check if there is a trigger
				worldTriggers[TalkingToNPC.active[NPCOPTIONS][THREE][TRIGGER]][ACTIVE] = True
			return
		print(errorMessage)
		
	def do_4(self, arg):
		if 'four' in TalkingToNPC.active[NPCDIALOG]:
			print(TalkingToNPC.active[NPCDIALOG][FOUR])
			if TalkingToNPC.active[NPCOPTIONS][FOUR].get(TRIGGER, None) != None: # Check if there is a trigger
				worldTriggers[TalkingToNPC.active[NPCOPTIONS][FOUR][TRIGGER]][ACTIVE] = True
			return
		print(errorMessage)
		
	def do_5(self, arg):
		if 'five' in TalkingToNPC.active[NPCDIALOG]:
			print(TalkingToNPC.active[NPCDIALOG][FIVE])
			if TalkingToNPC.active[NPCOPTIONS][FIVE].get(TRIGGER, None) != None: # Check if there is a trigger
				worldTriggers[TalkingToNPC.active[NPCOPTIONS][FIVE][TRIGGER]][ACTIVE] = True
			return
		print(errorMessage)
		
	def do_6(self, arg):
		if 'six' in TalkingToNPC.active[NPCDIALOG]:
			print(TalkingToNPC.active[NPCDIALOG][SIX])
			if TalkingToNPC.active[NPCOPTIONS][SIX].get(TRIGGER, None) != None: # Check if there is a trigger
				worldTriggers[TalkingToNPC.active[NPCOPTIONS][SIX][TRIGGER]][ACTIVE] = True
			return
		print(errorMessage)

	def do_options(self, arg):
		listNPCOptions(TalkingToNPC.active)

	def do_goodbye(self, arg):
		print(TalkingToNPC.active[NPCGOODBYE])
		displayLocation(location)
		return True # Return to the game loop
	
	do_one = do_1
	do_One = do_1
	do_two = do_2
	do_Two = do_2
	do_three = do_3
	do_Three = do_3
	do_four = do_4
	do_Four = do_4
	do_five = do_5
	do_Five = do_5
	do_Goodbye = do_goodbye
	do_bye = do_goodbye
	do_Bye = do_goodbye
	do_later = do_goodbye
	do_Later = do_goodbye
	do_opt = do_options
	do_Opt = do_options
	do_Options = do_options

class EndingSequence(cmd.Cmd):
	prompt = '\nDo Nothing, or object?\n>'

	# The default() method is called when none of the other do_*() command methods match.
	def default(self, arg):
		print(errorMessage)

	def do_quit(self, arg):
		"""Quit the game."""
		return True

	def do_help(self, arg):
		print(errorMessage)

	def do_objection(self, arg):
		points = 0
		if worldTriggers['Documents Lore'][ACTIVE]:
			print('{}: Objection!'.format(player[NAME]))
			print('\n'.join(textwrap.wrap('{}: I found evidence of the mayor planning to remove the GM from this town bacause of hatred if he ever becomes mayor.'.format(player[NAME]), SCREEN_WIDTH)))
			points += 1
			input('\n"Press enter to continue"\n')
		if worldTriggers['Manager Lore'][ACTIVE]:
			print('{}: Objection!'.format(player[NAME]))
			print('\n'.join(textwrap.wrap('{}: I talked to the mayor and he told me that he want\'s to take money from those with a lot so that he can rebuild the town. Mainly the GM.'.format(player[NAME]), SCREEN_WIDTH)))
			points += 1
			input('\n"Press enter to continue"\n')
		if worldTriggers['Hilda Lore'][ACTIVE]:
			print('{}: Objection!'.format(player[NAME]))
			print('\n'.join(textwrap.wrap('{}: When I talked to Hilda, she said something about hte GM being nice and helping her, as well as the other citizens out.".'.format(player[NAME]), SCREEN_WIDTH)))
			points += 1
			input('\n"Press enter to continue"\n')
		if points == 0:
			print('You have nothing to object with.')
			input('\n"Press enter to continue"\n')
		print('Votes are closed and everone has voted')
		input('\n"Press enter to continue"\n')
		if points >= 2:
			print('\n'.join(textwrap.wrap('The winner is the GM. GG (Don\'t have time to give you a nice ending, but know that I am proud of you for getting this far. Now: Go outseide and touch grass!)', SCREEN_WIDTH)))
			input('\n"Press enter to continue"\n')
			print(f'Good ending. You are a good person (Unless you are a furry, which in that case you should {bcolors.FAIL}PERISH!{bcolors.WARNING}).')
			input('\n"Press enter to continue"\n')
			return True
		print('\n'.join(textwrap.wrap('You did not convince the people of this town, and the Manager was elected.', SCREEN_WIDTH)))
		input('\n"Press enter to continue"\n')
		print('\n'.join(textwrap.wrap('The first thing he did was banished the GM to the dungeon where he will spend the rest of his life. The new mayor does as promised and imporoves the towns "modernity" by using the most of the fundings saved up, leaving none for the buisnisses around town. To add onto this, the manager raises taxes for items bough outside of his store.', SCREEN_WIDTH)))
		input('\n"Press enter to continue"\n')
		print('Bad ending. You are a terrible person.')
		input('\n"Press enter to continue"\n')
		return True
			

	def do_nothing(self, arg):
		print('Votes are closed and everone has voted')
		input('\n"Press enter to continue"\n')
		print('The people voted for Magager as mayor.')
		input('\n"Press enter to continue"\n')
		print('\n'.join(textwrap.wrap('Thanks to you not helping, the Manager was elected as mayor and banished the GM to the dungeon where he will spend the rest of his life. The new mayor does as promised and imporoves the towns "modernity" by using the most of the fundings saved up, leaving none for the buisnisses around town. To add onto this, the manager raises taxes for items bough outside of his store.', SCREEN_WIDTH)))
		input('\n"Press enter to continue"\n')
		print('Bad ending. You are a terrible person.')
		return True

	do_object = do_objection

from introSequence import loading

if __name__ == '__main__':
	loading()
	print(f"""{bcolors.WARNING}
	
======================================

(Type "help" for a list of commands.)

======================================
{bcolors.WARNING}""")
	displayLocation(location)
	TextAdventureCmd().cmdloop()
	print('Thank you so much a-for-to playing my game')