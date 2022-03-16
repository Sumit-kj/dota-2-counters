# dota-2-counters
Scrapes counters for each hero from dota2.fandom and provides a visual representation of counters to each opponent's pick.
This is a FastAPI based backend repository, deployed on https://dota-2-picker.herokuapp.com .

###API
https://dota-2-picker.herokuapp.com/get_counters?picks=Axe,BB,ES,WW,Invo.

Here picks are the picks that opponent is making.
####Note :  It can have up to 5 picks.

###Alias
####The mapping to the heroes are as follows:<br/>
"ABADDON": "Abaddon",<br/> 
"ALCHEMIST": "Alchemist",<br/> 
"ALCH": "Alchemist",<br/>
"ANCIENT APPARITION": "Ancient Apparition",<br/>
"ANCIENT": "Ancient Apparition",<br/>
"AA": "Ancient Apparition",<br/>
"ANTI-MAGE": "Anti-Mage",<br/>
"AM": "Anti-Mage",<br/>
"ARC WARDEN": "Arc Warden",<br/>
"AW": "Arc Warden",<br/>
"ARC": "Arc Warden",<br/>
"AXE": "Axe",<br/>
"BANE": "Bane",<br/>
"BATRIDER": "Batrider",<br/>
"BR": "Batrider",<br/>
"BAT": "Batrider",<br/>
"BEASTMASTER": "Beastmaster",<br/>
"BEAST": "Beastmaster",<br/>
"BLOODSEEKER": "Bloodseeker",<br/>
"BS": "Bloodseeker",<br/>
"BOUNTY HUNTER": "Bounty Hunter",<br/>
"BOUNTY": "Bounty Hunter",<br/>
"BH": "Bounty Hunter",<br/>
"BREWMASTER": "Brewmaster",<br/>
"BREW": "Brewmaster",<br/>
"BRISTLEBACK": "Bristleback",<br/>
"BB": "Bristleback",<br/>
"BROODMOTHER": "Broodmother",<br/>
"BROOD": "Broodmother",<br/>
"CENTAUR WARRUNNER": "Centaur Warrunner",<br/>
"CENTAUR": "Centaur Warrunner",<br/>
"CW": "Centaur Warrunner",<br/>
"CHAOS KNIGHT": "Chaos Knight",<br/>
"CK": "Chaos Knight",<br/>
"CHEN": "Chen",<br/>
"CLINKZ": "Clinkz",<br/>
"CL": "Clinkz",<br/>
"CLOCKWERK": "Clockwerk",<br/>
"CLOCK": "Clockwerk",<br/>
"CRYSTAL MAIDEN": "Crystal Maiden",<br/>
"CM": "Crystal Maiden",<br/>
"DARK SEER": "Dark Seer",<br/>
"SEER": "Dark Seer",<br/>
"DS": "Dark Seer",<br/>
"DARK WILLOW": "Dark Willow",<br/>
"WILLOW": "Dark Willow",<br/>
"DW": "Dark Willow",<br/>
"DAWNBREAKER": "Dawnbreaker",<br/>
"DAWN": "Dawnbreaker",<br/>
"DB": "Dawnbreaker",<br/>
"DAZZLE": "Dazzle",<br/>
"DEATH PROPHET": "Death Prophet",<br/>
"DP": "Death Prophet",<br/>
"DISRUPTOR": "Disruptor",<br/>
"DOOM": "Doom",<br/>
"DRAGON KNIGHT": "Dragon Knight",<br/>
"DK": "Dragon Knight",<br/>
"DROW RANGER": "Drow Ranger",<br/>
"DROW": "Drow Ranger",<br/>
"DR": "Drow Ranger",<br/>
"EARTH SPIRIT": "Earth Spirit",<br/>
"EARTH": "Earth Spirit",<br/>
"EARTHSHAKER": "Earthshaker",<br/>
"ES": "Earthshaker",<br/>
"ELDER TITAN": "Elder Titan",<br/>
"ET": "Elder Titan",<br/>
"EMBER SPIRIT": "Ember Spirit",<br/>
"EMBER": "Ember Spirit",<br/>
"ENCHANTRESS": "Enchantress",<br/>
"ENIGMA": "Enigma",<br/>
"FACELESS VOID": "Faceless Void",<br/>
"FACELESS": "Faceless Void",<br/>
"FV": "Faceless Void",<br/>
"GRIMSTROKE": "Grimstroke",<br/>
"GYROCOPTER": "Gyrocopter",<br/>
"GYRO": "Gyrocopter",<br/>
"HOODWINK": "Hoodwink",<br/>
"HUSKAR": "Huskar",<br/>
"INVOKER": "Invoker",<br/>
"JOKER": "Invoker",<br/>
"INVO": "Invoker",<br/>
"IO": "Io",<br/>
"JAKIRO": "Jakiro",<br/>
"JUGGERNAUT": "Juggernaut",<br/>
"JUGG": "Juggernaut",<br/>
"KEEPER OF THE LIGHT": "Keeper of the Light",<br/>
"KOTL": "Keeper of the Light",<br/>
"KUNKKA": "Kunkka",<br/>
"LEGION COMMANDER": "Legion Commander",<br/>
"LEGION": "Legion Commander",<br/>
"LC": "Legion Commander",<br/>
"LESHRAC": "Leshrac",<br/>
"LICH": "Lich",<br/>
"LIFESTEALER": "Lifestealer",<br/>
"LS": "Lifestealer",<br/>
"LINA": "Lina",<br/>
"LION": "Lion",<br/>
"LONE DRUID": "Lone Druid",<br/>
"LONE": "Lone Druid",<br/>
"DRUID": "Lone Druid",<br/>
"LD": "Lone Druid",<br/>
"LUNA": "Luna",<br/>
"LYCAN": "Lycan",<br/>
"MAGNUS": "Magnus",<br/>
"MARS": "Mars",<br/>
"MEDUSA": "Medusa",<br/>
"MEEPO": "Meepo",<br/>
"MIRANA": "Mirana",<br/>
"MONKEY KING": "Monkey King",<br/>
"MK": "Monkey King",<br/>
"WUKONG": "Monkey King",<br/>
"MORPHLING": "Morphling",<br/>
"MORPH": "Morphling",<br/>
"NAGA SIREN": "Naga Siren",<br/>
"NAGA": "Naga Siren",<br/>
"NATURE'S PROPHET": "Nature's Prophet",<br/>
"NP": "Nature's Prophet",<br/>
"NECROPHOS": "Necrophos",<br/>
"NIGHT STALKER": "Night Stalker",<br/>
"NS": "Night Stalker",<br/>
"NYX ASSASSIN": "Nyx Assassin",<br/>
"NYX": "Nyx Assassin",<br/>
"OGRE MAGI": "Ogre Magi",<br/>
"OGRE": "Ogre Magi",<br/>
"OMNIKNIGHT": "Omniknight",<br/>
"OMNI": "Omniknight",<br/>
"ORACLE": "Oracle",<br/>
"OUTWORLD DESTROYER": "Outworld Destroyer",<br/>
"OD": "Outworld Destroyer",<br/>
"PANGOLIER": "Pangolier",<br/>
"PANGO": "Pangolier",<br/>
"PHANTOM ASSASSIN": "Phantom Assassin",<br/>
"PA": "Phantom Assassin",<br/>
"PHANTOM LANCER": "Phantom Lancer",<br/>
"PL": "Phantom Lancer",<br/>
"PHOENIX": "Phoenix",<br/>
"PUCK": "Puck",<br/>
"PUDGE": "Pudge",<br/>
"PUGNA": "Pugna",<br/>
"QUEEN OF PAIN": "Queen of Pain",<br/>
"QOP": "Queen of Pain",<br/>
"RAZOR": "Razor",<br/>
"RIKI": "Riki",<br/>
"RUBICK": "Rubick",<br/>
"SAND KING": "Sand King",<br/>
"SK": "Sand King",<br/>
"SHADOW DEMON": "Shadow Demon",<br/>
"SD": "Shadow Demon",<br/>
"SHADOW FIEND": "Shadow Fiend",<br/>
"SF": "Shadow Fiend",<br/>
"SHADOW SHAMAN": "Shadow Shaman",<br/>
"SHAMAN": "Shadow Shaman",<br/>
"SILENCER": "Silencer",<br/>
"SKYWRATH MAGE": "Skywrath Mage",<br/>
"MAGE": "Skywrath Mage",<br/>
"SKYWRATH": "Skywrath Mage",<br/>
"SKY": "Skywrath Mage",<br/>
"SLARDAR": "Slardar",<br/>
"SLARK": "Slark",<br/>
"SNAPFIRE": "Snapfire",<br/>
"SNIPER": "Sniper",<br/>
"SNIP": "Sniper",<br/>
"SPECTRE": "Spectre",<br/>
"SPEC": "Spectre",<br/>
"SPIRIT BREAKER": "Spirit Breaker",<br/>
"SB": "Spirit Breaker",<br/>
"BARA": "Spirit Breaker",<br/>
"STORM SPIRIT": "Storm Spirit",<br/>
"STORM": "Storm Spirit",<br/>
"SS": "Storm Spirit",<br/>
"SVEN": "Sven",<br/>
"TECHIES": "Techies",<br/>
"TECH": "Techies",<br/>
"TEMPLAR ASSASSIN": "Templar Assassin",<br/>
"TA": "Templar Assassin",<br/>
"TERRORBLADE": "Terrorblade",<br/>
"TB": "Terrorblade",<br/>
"TIDEHUNTER": "Tidehunter",<br/>
"TIDE": "Tidehunter",<br/>
"TH": "Tidehunter",<br/>
"TIMBERSAW": "Timbersaw",<br/>
"TIMBER": "Timbersaw",<br/>
"TINKER": "Tinker",<br/>
"TINY": "Tiny",<br/>
"TREANT PROTECTOR": "Treant Protector",<br/>
"TREANT": "Treant Protector",<br/>
"TROLL WARLORD": "Troll Warlord",<br/>
"TROLL": "Troll Warlord",<br/>
"TUSK": "Tusk",<br/>
"UNDERLORD": "Underlord",<br/>
"UNDYING": "Undying",<br/>
"URSA": "Ursa",<br/>
"VENGEFUL SPIRIT": "Vengeful Spirit",<br/>
"VENGE": "Vengeful Spirit",<br/>
"VENOMANCER": "Venomancer",<br/>
"VENO": "Venomancer",<br/>
"VIPER": "Viper",<br/>
"VISAGE": "Visage",<br/>
"VOID SPIRIT": "Void Spirit",<br/>
"VOID": "Void Spirit",<br/>
"WARLOCK": "Warlock",<br/>
"WEAVER": "Weaver",<br/>
"WINDRANGER": "Windranger",<br/>
"WR": "Windranger",<br/>
"WINTER WYVERN": "Winter Wyvern",<br/>
"WINTER": "Winter Wyvern",<br/>
"WW": "Winter Wyvern",<br/>
"WITCH DOCTOR": "Witch Doctor",<br/>
"WD": "Witch Doctor",<br/>
"WITCH": "Witch Doctor",<br/>
"WRAITH KING": "Wraith King",<br/>
"WK": "Wraith King",<br/>
"ZEUS": "Zeus"<br/>