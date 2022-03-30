NPCNAME = 'npcname'
NPCGREETING = 'npcgreeting'
NPCOPTIONS = 'npcoptions'
NPCDIALOG = 'npcdialog'
DIALOG = 'dialog'
TRIGGER = 'trigger'
SECRET = 'secret'
ONE = 'one'
TWO = 'two'
THREE = 'three'
FOUR = 'four'
FIVE = 'five'
SIX = 'six'
NPCGOODBYE = 'npcgoodbye'

worldNPCS = {
	'Greg' : {
		NPCNAME: ['Greg', 'Fisherman'], # NPC aliases written in title()
		NPCGREETING: 'Morning! Nice day for fishing ain\'t it! Hu ha!',
		NPCGOODBYE: 'Morning! Nice day for fishing ain\'t it! Hu ha!',
		NPCOPTIONS: {
			ONE: {
				DIALOG: 'Morning!',
			},
			TWO: {
				DIALOG: 'Who are you?',
				},
			THREE: {
				DIALOG: 'What is this town?',
				},
			FOUR: {
				DIALOG: 'Are you ok?',
				},
		},
		NPCDIALOG : {
			ONE: 'Morning! Nice day for fishing ain\'t it! Hu ha!',
			TWO: 'Morning! Nice day for fishing ain\'t it! Hu ha!',
			THREE: 'Morning! Nice day for fishing ain\'t it! Hu ha!',
			FOUR: 'Morning! Nice day for fishing ain\'t it! Hu ha!',
		},
	},
	'Hilda' : {
		NPCNAME: ['Hilda', 'Flower Lady', 'Lady', 'Woman'], # NPC aliases written in title()
		NPCGREETING: 'Can you smell it? The flowers here has such a nice smell!',
		NPCGOODBYE: 'Have a nice day.',
		NPCOPTIONS: {
			ONE: {
				DIALOG: 'Who are you?',
			},
			TWO: {
				DIALOG: 'Who do you work for?',
				TRIGGER: 'Hilda Lore'
			},
		},
		NPCDIALOG : {
			ONE: 'My name is Hilda, I am the decorist of this town. This town was all gloomy untill I started decorating it.',
			TWO: 'I am working for The Mayor. He is paying me, though I would like to earn a little more so that I can afford more plants. Luckily the GM is funding me from time to time. He is such a nice person. In fact, I haven\'t seen him leave his house in a while. I hope everything is all right with him.',
		}
	},
	'Manager' : {
		NPCNAME: ['Manager', 'Store Owner', 'Lady', 'Woman'], # NPC aliases written in title()
		NPCGREETING: 'Good day , my fellow citizen',
		NPCGOODBYE: 'Until next time kid.',
		NPCOPTIONS: {
			ONE: {
				DIALOG: 'Who are you?',
			},
			TWO: {
				DIALOG: 'Why are you here?',
			},
			THREE: {
				DIALOG: 'Who else is running for mayor?',
				TRIGGER: 'Manager Lore'
			},
		},
		NPCDIALOG : {
			ONE: 'I manager that is running The Store. Feel free to come down and purchase all the groceries you need and I may give you a price reduction.',
			TWO: 'I\'m waiting for the election to start. We are holding an election over who will be the next mayor. You should vote for me since I am going to renovate this town and make it a little more "modern".',
			THREE: 'There are only two candidates; Me and the GM. I can\'t say that I would like for him to win since all he does is sit inside and play videogames or watch anime. Instead, he could use his wealth for this town. So if you vote for me, I will gladly take a portion of his fortune and use it for OUR future.'
		}
	},
	
}