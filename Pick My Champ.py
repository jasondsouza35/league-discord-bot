import random
import discord

client = discord.Client()


champ = ['Aatrox', ' Akali', ' Aurelion Sol', ' Ahri', ' Alistar', ' Amumu', ' Anivia', ' Annie', ' Ashe', ' Azir',
         ' Bard', ' Blitzcrank', ' Brand', ' Braum', ' Camille', ' Caitlyn', ' Cassiopeia', ' Cho Gath', ' Corki',
         ' Darius', ' Dr. Mundo', ' Diana', ' Draven', ' Ekko', ' Elise', ' Evelynn', ' Ezreal', ' Fiddlesticks',
         ' Fiora', ' Fizz', ' Galio', ' Gangplank', ' Garen', ' Gnar', ' Gragas', ' Graves', ' Hecarim',
         ' Heimerdinger', ' Irelia', ' Ivern', ' Illaoi', ' Janna', ' Jarvan IV', ' Jax', ' Jayce', ' Jhin', ' Jinx',
         ' Karma', ' Kalista', ' Karthus', ' Kassadin', ' Kai Sa', ' Katarina', ' Kayn', ' Kayle', ' Kennen',
         ' Kha Zix', ' Kog Maw', ' Kled', ' Kindred', ' LeBlanc', ' Lee Sin', ' Leona', ' Lucian', ' Lissandra',
         ' Lulu', ' Lux', ' Malphite', ' Malzahar', ' Maokai', ' Master Yi', ' Miss Fortune', ' Mordekaiser',
         ' Morgana', ' Nami', ' Nasus', ' Nautilus', ' Neeko', ' Nidalee', ' Nocturne', ' Nunu and Willump', ' Olaf',
         ' Ornn', ' Orianna', ' Pantheon', ' Poppy', ' Pyke', ' Quinn', ' Rammus', ' Rakan', ' Rek Sai', ' Renekton',
         ' Rengar', ' Riven', ' Rumble', ' Ryze', ' Sejuani', ' Shaco', ' Shen', ' Shyvana', ' Singed', ' Sion',
         ' Sivir', ' Skarner', ' Sona', ' Soraka', ' Swain', ' Syndra', ' Sylas', ' Talon', ' Taliyah', ' Taric',
         ' Tahm Kench', ' Thresh', ' Teemo', ' Tristana', ' Trundle', ' Tryndamere', ' Twisted Fate', ' Twitch',
         ' Udyr', ' Urgot', ' Varus', ' Vayne', ' Veigar', ' Vel Koz', ' Vi', ' Viktor', ' Vladimir', ' Volibear',
         ' Warwick', ' Wukong', ' Xayah', ' Xerath', ' Xin Zhao', ' Yasuo', ' Yorick', ' Zac', ' Zed', ' Ziggs',
         ' Zilean', ' Zoe', ' Zyra', ' Yuumi', ' Tibbers', ' Senna', ' Qiana', ' Sett', ' Aphelios', ' Lillia',
         ' Yone']

runes = ['Precision', 'Domination', 'Sorcery', 'Resolve', 'Inspiration']

pkeystone = ['Press the Attack','Lethal Tempo', 'Fleet Footwork', 'Conqueror']
pheroism = ['Overheal', 'Triumph', 'Presence of Mind']
plegend = ['Alacrity', 'Tenacity', 'Bloodline']
pcombat = ['Coup de Grace', 'Take Down', 'Last Stand']

dkeystone = ['Electrocute', 'Domination', 'Dark Harvest', 'Hail of Blades']
dmalice = ['Cheap Shot', 'Taste of Blood', 'Sudden Impact']
dtracking = ['Zombie Ward', 'Ghost Poro', 'Eyeball Collection']
dhunter = ['Ravenous Hunter', 'Ingenious Hunter', 'Relentless Hunter', 'Ultimate Hunter']

skeystone = ['Summon Aery', 'Arcane Comet', 'Phase Rush']
sartifact = ['Nullifying Orb', 'Manaflow Band', 'Nimbus Cloak']
sexcellence = ['Transcendence', 'Celerity', 'Absolute Focus']
spower = ['Scorch', 'Waterwalking', 'Gathering Storm']

rkeystone = ['Grasp of the Undying', 'Aftershock', 'Guardian']
rstrength = ['Demolish', 'Font of Life', 'Shield Bash']
rresistance = ['Conditioning', 'Second Wind', 'Bone Plating']
rvitality = ['Overgrowth', 'Revitalize', 'Unflinching']

ikeystones = ['Glacial Augment', 'Unsealed Spellbook','Prototype: Omnistone']
icontraptions = ['Hextech Flashtraption', 'Magical Footwear', 'Perfect Timing']
itomorrow = ["Future's Market", 'Minion Dematerializer', 'Biscuit Delivery']
ibeyond = ['Cosmic Insight', 'Approach Velocity', 'Time Warp Tonic']



@client.event
async def on_message(message):
    if message.content.startswith('.pickmychamp') or message.content.startswith('.pmc'):
        await message.channel.send(random.choice(champ))
    elif message.content.startswith('.pickmyrune') or message.content.startswith('.pmr'):
        randomrune = random.choice(runes)
        await message.channel.send(randomrune)
        if randomrune == ('Precision'):
            runepage = [random.choice(pkeystone),random.choice(pheroism), random.choice(plegend), random.choice(pcombat)]
            await message.channel.send(', '.join(runepage))
        elif randomrune == ('Domination'):
            runepage = [random.choice(dkeystone),random.choice(dmalice),random.choice(dtracking),random.choice(dhunter)]
            await message.channel.send(', '.join(runepage))
        elif randomrune == ('Sorcery'):
            runepage = [random.choice(skeystone),random.choice(sartifact),random.choice(sexcellence),random.choice(spower)]
            await message.channel.send(', '.join(runepage))
        elif randomrune == ('Resolve'):
            runepage = [random.choice(rkeystone),random.choice(rstrength),random.choice(rresistance),random.choice(rvitality)]
            await message.channel.send(', '.join(runepage))
        elif randomrune == ('Inspiration'):
            runepage = [random.choice(ikeystones),random.choice(icontraptions),random.choice(itomorrow),random.choice(ibeyond)]
            await message.channel.send(', '.join(runepage))


client.run('Hidden Key') #Hidden key to protect bot from potential changes
