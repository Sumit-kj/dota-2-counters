# dota-2-counters
Scrapes counters for each hero from dota2.fandom and provides a visual representation of counters to each opponent's pick.
This is a FastAPI based backend repository, deployed on https://dota-2-picker.herokuapp.com .

### API
```
https://dota-2-picker.herokuapp.com/get_counters?picks=Axe,BB,ES,WW,Invo
```
Here picks are the picks that opponent is making.
#### Note :  It can have from 1 to 5 picks, separated by comma(,).

### Alias
#### The mapping to the heroes are as follows:<br/>
```
"ABADDON": "Abaddon", 
"ALCHEMIST": "Alchemist", 
"ALCH": "Alchemist",
"ANCIENT APPARITION": "Ancient Apparition",
"ANCIENT": "Ancient Apparition",
"AA": "Ancient Apparition",
"ANTI-MAGE": "Anti-Mage",
"AM": "Anti-Mage",
"ARC WARDEN": "Arc Warden",
"AW": "Arc Warden",
"ARC": "Arc Warden",
"AXE": "Axe",
"BANE": "Bane",
"BATRIDER": "Batrider",
"BR": "Batrider",
"BAT": "Batrider",
"BEASTMASTER": "Beastmaster",
"BEAST": "Beastmaster",
"BLOODSEEKER": "Bloodseeker",
"BS": "Bloodseeker",
"BOUNTY HUNTER": "Bounty Hunter",
"BOUNTY": "Bounty Hunter",
"BH": "Bounty Hunter",
"BREWMASTER": "Brewmaster",
"BREW": "Brewmaster",
"BRISTLEBACK": "Bristleback",
"BB": "Bristleback",
"BROODMOTHER": "Broodmother",
"BROOD": "Broodmother",
"CENTAUR WARRUNNER": "Centaur Warrunner",
"CENTAUR": "Centaur Warrunner",
"CW": "Centaur Warrunner",
"CHAOS KNIGHT": "Chaos Knight",
"CK": "Chaos Knight",
"CHEN": "Chen",
"CLINKZ": "Clinkz",
"CL": "Clinkz",
"CLOCKWERK": "Clockwerk",
"CLOCK": "Clockwerk",
"CRYSTAL MAIDEN": "Crystal Maiden",
"CM": "Crystal Maiden",
"DARK SEER": "Dark Seer",
"SEER": "Dark Seer",
"DS": "Dark Seer",
"DARK WILLOW": "Dark Willow",
"WILLOW": "Dark Willow",
"DW": "Dark Willow",
"DAWNBREAKER": "Dawnbreaker",
"DAWN": "Dawnbreaker",
"DB": "Dawnbreaker",
"DAZZLE": "Dazzle",
"DEATH PROPHET": "Death Prophet",
"DP": "Death Prophet",
"DISRUPTOR": "Disruptor",
"DOOM": "Doom",
"DRAGON KNIGHT": "Dragon Knight",
"DK": "Dragon Knight",
"DROW RANGER": "Drow Ranger",
"DROW": "Drow Ranger",
"DR": "Drow Ranger",
"EARTH SPIRIT": "Earth Spirit",
"EARTH": "Earth Spirit",
"EARTHSHAKER": "Earthshaker",
"ES": "Earthshaker",
"ELDER TITAN": "Elder Titan",
"ET": "Elder Titan",
"EMBER SPIRIT": "Ember Spirit",
"EMBER": "Ember Spirit",
"ENCHANTRESS": "Enchantress",
"ENIGMA": "Enigma",
"FACELESS VOID": "Faceless Void",
"FACELESS": "Faceless Void",
"FV": "Faceless Void",
"GRIMSTROKE": "Grimstroke",
"GYROCOPTER": "Gyrocopter",
"GYRO": "Gyrocopter",
"HOODWINK": "Hoodwink",
"HUSKAR": "Huskar",
"INVOKER": "Invoker",
"JOKER": "Invoker",
"INVO": "Invoker",
"IO": "Io",
"JAKIRO": "Jakiro",
"JUGGERNAUT": "Juggernaut",
"JUGG": "Juggernaut",
"KEEPER OF THE LIGHT": "Keeper of the Light",
"KOTL": "Keeper of the Light",
"KUNKKA": "Kunkka",
"LEGION COMMANDER": "Legion Commander",
"LEGION": "Legion Commander",
"LC": "Legion Commander",
"LESHRAC": "Leshrac",
"LICH": "Lich",
"LIFESTEALER": "Lifestealer",
"LS": "Lifestealer",
"LINA": "Lina",
"LION": "Lion",
"LONE DRUID": "Lone Druid",
"LONE": "Lone Druid",
"DRUID": "Lone Druid",
"LD": "Lone Druid",
"LUNA": "Luna",
"LYCAN": "Lycan",
"MAGNUS": "Magnus",
"MARS": "Mars",
"MEDUSA": "Medusa",
"MEEPO": "Meepo",
"MIRANA": "Mirana",
"MONKEY KING": "Monkey King",
"MK": "Monkey King",
"WUKONG": "Monkey King",
"MORPHLING": "Morphling",
"MORPH": "Morphling",
"NAGA SIREN": "Naga Siren",
"NAGA": "Naga Siren",
"NATURE'S PROPHET": "Nature's Prophet",
"NP": "Nature's Prophet",
"NECROPHOS": "Necrophos",
"NIGHT STALKER": "Night Stalker",
"NS": "Night Stalker",
"NYX ASSASSIN": "Nyx Assassin",
"NYX": "Nyx Assassin",
"OGRE MAGI": "Ogre Magi",
"OGRE": "Ogre Magi",
"OMNIKNIGHT": "Omniknight",
"OMNI": "Omniknight",
"ORACLE": "Oracle",
"OUTWORLD DESTROYER": "Outworld Destroyer",
"OD": "Outworld Destroyer",
"PANGOLIER": "Pangolier",
"PANGO": "Pangolier",
"PHANTOM ASSASSIN": "Phantom Assassin",
"PA": "Phantom Assassin",
"PHANTOM LANCER": "Phantom Lancer",
"PL": "Phantom Lancer",
"PHOENIX": "Phoenix",
"PUCK": "Puck",
"PUDGE": "Pudge",
"PUGNA": "Pugna",
"QUEEN OF PAIN": "Queen of Pain",
"QOP": "Queen of Pain",
"RAZOR": "Razor",
"RIKI": "Riki",
"RUBICK": "Rubick",
"SAND KING": "Sand King",
"SK": "Sand King",
"SHADOW DEMON": "Shadow Demon",
"SD": "Shadow Demon",
"SHADOW FIEND": "Shadow Fiend",
"SF": "Shadow Fiend",
"SHADOW SHAMAN": "Shadow Shaman",
"SHAMAN": "Shadow Shaman",
"SILENCER": "Silencer",
"SKYWRATH MAGE": "Skywrath Mage",
"MAGE": "Skywrath Mage",
"SKYWRATH": "Skywrath Mage",
"SKY": "Skywrath Mage",
"SLARDAR": "Slardar",
"SLARK": "Slark",
"SNAPFIRE": "Snapfire",
"SNIPER": "Sniper",
"SNIP": "Sniper",
"SPECTRE": "Spectre",
"SPEC": "Spectre",
"SPIRIT BREAKER": "Spirit Breaker",
"SB": "Spirit Breaker",
"BARA": "Spirit Breaker",
"STORM SPIRIT": "Storm Spirit",
"STORM": "Storm Spirit",
"SS": "Storm Spirit",
"SVEN": "Sven",
"TECHIES": "Techies",
"TECH": "Techies",
"TEMPLAR ASSASSIN": "Templar Assassin",
"TA": "Templar Assassin",
"TERRORBLADE": "Terrorblade",
"TB": "Terrorblade",
"TIDEHUNTER": "Tidehunter",
"TIDE": "Tidehunter",
"TH": "Tidehunter",
"TIMBERSAW": "Timbersaw",
"TIMBER": "Timbersaw",
"TINKER": "Tinker",
"TINY": "Tiny",
"TREANT PROTECTOR": "Treant Protector",
"TREANT": "Treant Protector",
"TROLL WARLORD": "Troll Warlord",
"TROLL": "Troll Warlord",
"TUSK": "Tusk",
"UNDERLORD": "Underlord",
"UNDYING": "Undying",
"URSA": "Ursa",
"VENGEFUL SPIRIT": "Vengeful Spirit",
"VENGE": "Vengeful Spirit",
"VENOMANCER": "Venomancer",
"VENO": "Venomancer",
"VIPER": "Viper",
"VISAGE": "Visage",
"VOID SPIRIT": "Void Spirit",
"VOID": "Void Spirit",
"WARLOCK": "Warlock",
"WEAVER": "Weaver",
"WINDRANGER": "Windranger",
"WR": "Windranger",
"WINTER WYVERN": "Winter Wyvern",
"WINTER": "Winter Wyvern",
"WW": "Winter Wyvern",
"WITCH DOCTOR": "Witch Doctor",
"WD": "Witch Doctor",
"WITCH": "Witch Doctor",
"WRAITH KING": "Wraith King",
"WK": "Wraith King",
"ZEUS": "Zeus"
```