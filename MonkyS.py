import discord, asyncio, random
from discord.ext import commands


#id: 739660030512595054

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = "-", intents = discord.Intents.all())

# Recruitment - Msg + Reactions
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id

    apply = payload.emoji

    channel5 = client.get_channel(738107566692761721)
    member = payload.member

    if message_id == 858559645618667520:
        await member.send("**Hello!**\n> 1) Here is the link to the tests: https://drive.google.com/drive/folders/15_QheyCOo_Xrzfrju7cKkXMPL854p8L8?usp=sharing\n> 2) **__READ__ the corresponding docs for further instructions**\n> 3) After you're done, please type **'APPLY'** to begin your application process.")


# APPLY
@client.event
async def on_message(message):
    if message.guild is None:
        if str(message.content) == 'APPLY':
            def check(no):
                return no.channel == message.channel
            ao3pog = await message.author.send('**Application process started ~ Make sure to answer all questions**')
            await message.author.send('What **role(s)** are you interested in applying for?')
            # Chapters
            await client.wait_for('message', check=check)
            await message.author.send('How many **chapters **can you do per week?')
            # Volunteer
            await client.wait_for('message', check=check)
            await message.author.send('Do you understand that this is volunteer work?')
            # Link
            await client.wait_for('message', check=check)
            await message.author.send('**Link** your __test__ or __past work__ (if test, **make sure we have edit/suggestion perms**)')
            # Finale
            await client.wait_for('message', check=check)
            await message.author.send("Lastly, please type **'DONE'** to **__submit__** your application, or type **'CANCEL'** to __cancel__ lmao. *If I don't respond with a confirmation after your reply, redo the app process again by typing 'APPLY'.*")

            # 2nd bruh bc im dumb but idk waht this is for
            def check(s):
                return (s.author == message.author and s.channel == message.channel)

            bruh = await client.wait_for('message', check=check)

            # if DONE
            if str(bruh.content) == 'DONE':
                newapplicant = message.author.mention
                manjuu = client.get_user(854543883845632000)
                sen = client.get_user(208108164061593600)
                aoieuy = client.get_user(472238811691352065)
                Peng = client.get_user(523966739810091029)
                test = client.get_channel(738107566692761721)
                (await message.channel.send('Thank you for your application! We will get back to in **2 days** max. If we take longer, then DM one of the NASA space monks the test link and let us know the bot may possibly be broken. Thanks again !'))

                #STARING HERE: THIS DOES NOT WORK
                (await test.send(f'New application pog! {manjuu.mention}, {aoieuy.mention}, {sen.mention}, {Peng.mention}. App from {newapplicant}'))

                # expose dms
                dm = []
                counter = 0
                channelbruh = message.channel
                messages = await channelbruh.history(limit=10, after=ao3pog).flatten()
                if message.author == client.user:
                    counter += 1
                    messages = message.content.split('\n')
                for message in messages:
                    dm.append(message.content)
                final = '\n\n'.join([''.join(map(str, item)) for item in dm])

                #embed
                applicationembed = discord.Embed(
                    title=('New Applicant! Pog'),
                    color=discord.Colour.blue()
                )

                applicationembed.set_footer(text='Respond to them ASAP')
                applicationembed.set_thumbnail(url='https://i.imgur.com/dtRtTAZ.jpg')
                applicationembed.add_field(name='Interview', value=final, inline=True)

                #SEND MESSAGE TO CHANNEL
                await test.send(embed=applicationembed)
                #STOPPING HERE, THIS DOES NOT WORK

            # if CANCEL
            if str(bruh.content) == 'CANCEL':
                await message.channel.send('Sorry to see you go D^: we hope you continue to support us though!')

            # Else
            else:
                pass

    # Staff welcome message
    actual_work = client.get_channel(750183897165463653)
    monky_shrine = client.get_channel(736704193905164441)
    not_bot = client.get_channel(736741523051511851)
    email = client.get_channel(736992278308192326)
    links = client.get_channel(736741434652360765)
    updates = client.get_channel(736747148263292929)
    ss = client.get_channel(736735728364683264)
    staffintro = client.get_channel(736794148320968744)


    # Variables because APCSP is actually good for something
    TMM = ("https://drive.google.com/drive/folders/1b39GLkqvf6O3e4oF8YHpvTyNZI877evH?usp=sharing")
    BTY = ("https://drive.google.com/drive/folders/1AjlmzrOdsbh7D4RlzPpWppiYl7bJMOk9?usp=sharing")
    OG = ("**ON CONFIRMED HIATUS** https://drive.google.com/drive/folders/1c4z_7VA4vFgBNPb2bnlGKsHZcdqfGbBN?usp=sharing")
    drive = ('https://drive.google.com/drive/folders/1gBRNYPAqWtQ26j1uCoCqioWBoAg0nXJa?usp=sharing')
    sheets = ('UPDATE THE SHEETS PLS ISTG https://docs.google.com/spreadsheets/d/1s_k8RTbT5VBCd3yvSH353OX4AlewhfAlVg8uLk3iJT4/edit?usp=sharing')
    BUD = ('https://drive.google.com/drive/folders/1A0soi1Yz2BWQ9dspi7khoTw7jPz3qVyJ?usp=sharing')
    guide = ('https://drive.google.com/drive/folders/1RVCtqUmUpESvCVHv8wEiQqGHqWrmhaVZ?usp=sharing')
    LSD = ('https://drive.google.com/drive/folders/1Y0I4CV6hqv0_RG3WVhfKlul9JY7g7_w3?usp=sharing')


#should also look into changing on_message() to prefixes
# should look to changing these into function with parameters
    #staff shenanimonks
    if message.channel == ss:
        if message.content.startswith("-whalecum"):
            user = message.mentions[0]
            await ss.send(f"**Welcome " + user.mention + f"!** \n> To start off, please put your email under {email.mention} for future references."
        f"\n> **Fill out the staff spreadsheet** under {links.mention}, **our scans drive link is also under there**."
        f"\n> After you're done with a chapter, please update under {updates.mention} and *update the sheets*."
        f"\n> To see what stuff you're assigned, look at the sheets or get a link to the sheets through our bot under {not_bot.mention} by doing `-halp`."
        f"\n> Feel free to introduce yourself under {staffintro.mention}."
        f"\n**Once again, welcome! We're glad you're here :D**")


    #actual work channel
    if message.channel == actual_work:
        if str(message.content) == '-TMM':
            await actual_work.send(TMM)
        if str(message.content) == '-BTY':
            await actual_work.send(BTY)
        if str(message.content) == '-OG':
            await actual_work.send(OG)
        if str(message.content) == '-drive':
            await actual_work.send(drive)
        if str(message.content) == '-sheets':
            await actual_work.send(sheets)
        if str(message.content) == '-NFB':
            await actual_work.send(BUD)
        if str(message.content) == '-LSD':
            await not_bot.send(LSD)
        if message.content.startswith("-whalecum"):
            user = message.mentions[0]
            await actual_work.send(f"Welcome " + user.mention + f"! \n> To start off, please put your email under {email.mention} for future references."
        f"\n**> Fill out the staff spreadsheet** under {links.mention}, **our scans drive link is also under there**."
        f"\n> After you're done with a chapter, please update under {updates.mention} and *update the sheets*."
        f"\n> To see what stuff you're assigned, look at the sheets or get a link to the sheets through our bot under {not_bot.mention} by doing `-halp`."
        f"\n> Feel free to introduce yourself under {staffintro.mention}."
        f" Once again, welcome! We're glad you're here :D")
        if str(message.content) == '-guides':
            await actual_work.send(guide)



    #not_bot channel
    if message.channel == not_bot:
        if str(message.content) == '-TMM':
            await not_bot.send(TMM)
        if str(message.content) == '-BTY':
            await not_bot.send(BTY)
        if str(message.content) == '-OG':
            await not_bot.send(OG)
        if str(message.content) == '-drive':
            await not_bot.send(drive)
        if str(message.content) == '-sheets':
            await not_bot.send(sheets)
        if str(message.content) == '-NFB':
            await not_bot.send(BUD)
        if str(message.content) == '-guides':
            await not_bot.send(guide)
        if str(message.content) == '-LSD':
            await not_bot.send(LSD)

    #monky shrine
    if message.channel == monky_shrine:
        if str(message.content) == '-TMM':
            await monky_shrine.send(TMM)
        if str(message.content) == '-BTY':
            await monky_shrine.send(BTY)
        if str(message.content) == '-OG':
            await monky_shrine.send(OG)
        if str(message.content) == '-drive':
            await monky_shrine.send(drive)
        if str(message.content) == '-sheets':
            await monky_shrine.send(sheets)
        if str(message.content) == '-NFB':
            await monky_shrine.send(BUD)
        if str(message.content) == '-guides':
            await monky_shrine.send(guide)
        if str(message.content) == '-LSD':
            await monky_shrine.send(LSD)

    await client.process_commands(message)

#help embed
@client.command()
async def halp(message):
    if(message.channel.id == 750183897165463653 or 750183897165463653 or 736735728364683264):
        helpembed = discord.Embed(
            title= 'Thank you for using the bot!',
            description='What I can do',
            color= discord.Colour.blue()
    )

        helpembed.set_footer(text="Peng wuz here")
        helpembed.set_author(name='Bot commands', icon_url='https://i.imgur.com/177AazQ.jpg')
        helpembed.set_thumbnail(url='https://i.imgur.com/bJYt1Ob.jpg')
        helpembed.add_field(name="Remember to use the not-bot channel and update the sheets!", value=
                "-halp for bot help lol\n"
                "-[Series abbreviation] for the link to the series drive\n"
                "-sheets for link to sheets\n"
                "-drive for link to drive\n"
                "-guides to get our certified monky guides\n"                
                "-series for our **current** series\n"
                "-completed for a list of our **completed** series\n"
                "-dropped for our **dropped** series\n", inline=True)

        await message.send(embed=helpembed)


# beginning of monkaS PLEASE FIX THIS SHITSHOW
def add(para):
    with open('hiatus.txt', 'a') as file:
        file.write(f'{para}\n')
        file.close()

def remove(para2):
    a_file = open("hiatus.txt", "r")
    lines = a_file.readlines()
    a_file.close()

    new_file = open("hiatus.txt", "w")
    for line in lines:
        if line.strip("\n") != f"{para2}":
            new_file.write(line)
    new_file.close()
#end of monkaS xd


#hiatus family tingz FIX

@client.command()
async def hiatusadd(ctx, arg):
    if (ctx.message.channel.id == 736741523051511851):
        add(arg)
        print(f'{arg} has been added to the hiatus list! To remove please do -hiatusremove {arg}')


@client.command()
async def hiatus(message):
    if (message.channel.id == 736741523051511851):
        hiatusembed = discord.Embed(
            title= 'Monks on Hiatus/Quit/MIA',
            description= 'Please put these next to your name if you are:\n'
                         'Missing in action → (?)\n'
                         'Has reason for hiatus → (*)\n'
                         'Wrap your name in " " if there is any spaces in between ur name',
            color= discord.Colour.blue()
    )
        hiatusembed.set_footer(text='To remove yourself from the list, do -hiatusremove [name as it is on the list]')
        hiatusembed.set_author(name='Monks on vacation', icon_url='https://i.imgur.com/HCJ7ABF.jpg')
        hiatusembed.set_thumbnail(url='https://i.imgur.com/XvOQVVb.jpg')
        with open('hiatus.txt', 'r') as file:
            hiatusembed.add_field(name="Come back soon pls", value=(file.read()), inline=True)

        await message.send(embed=hiatusembed)
        file.close()


@client.command()
async def hiatusremove(ctx, arg):
    if (ctx.message.channel.id == 736741523051511851):
        remove(arg)
        print(f'{arg} has been removed from the hiatus list!')



#active series tingz

@client.command()
async def series(message):
    if (message.channel.id == 736741523051511851):
        activeembed = discord.Embed(
            title= 'Active Monky Series',
            color= discord.Colour.blue()
    )

        activeembed.set_author(name='Monky Scnas', icon_url='https://i.imgur.com/mqkwaLh.jpg')
        activeembed.set_thumbnail(url='https://i.imgur.com/nRxOLm0.jpg')
        activeembed.set_footer(text='-[Series abbreviation] for drive link')
        with open('series.txt', 'r') as file:
            activeembed.add_field(name="Da series we work on", value=(file.read()), inline=True)

        await message.send(embed=activeembed)

#dropped series list

@client.command()
async def dropped(message):
    if (message.channel.id == 736741523051511851):
        droppedembed = discord.Embed(
            title= 'Dropped Monky Series',
            color= discord.Colour.blue(),
            description='Never to be opened again'
    )

        droppedembed.set_author(name='Monky Scnas', icon_url='https://i.imgur.com/E7XHm1J.jpg')
        droppedembed.set_thumbnail(url='https://i.imgur.com/dtRtTAZ.jpg')
        with open('dropped.txt', 'r') as file:
            droppedembed.add_field(name="Da series we don't work on no more", value=(file.read()), inline=True)

        await message.send(embed=droppedembed)


#completed series
@client.command()
async def completed(message):
    if (message.channel.id == 736741523051511851):
        completedembed = discord.Embed(
            title= 'Completed Monky Series',
            color= discord.Colour.blue(),
            description='Kreygasmic, really.'
    )

        completedembed.set_author(name='Monky Scnas', icon_url='https://i.imgur.com/i52h9o1.jpg')
        completedembed.set_thumbnail(url='https://i.imgur.com/e5HGWni.jpg')
        with open('completed.txt', 'r') as file:
            completedembed.add_field(name="Da series we poured our blood, sweat, and tears on", value=(file.read()), inline=True)

        await message.send(embed=completedembed)





# bot playing game
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="we're recruiting all roles!"))

# update the sheets image
async def update_your_sheets():
    await client.wait_until_ready()
    staff_shenanimonks = client.get_channel(736735728364683264)
    while not client.is_closed():
        images = ("https://i.imgur.com/CxgOaFc.png", "https://i.imgur.com/00mZeGt.png", "https://i.imgur.com/efwN7Sc.jpg", "https://i.imgur.com/G4FPSnw.jpg", "https://i.imgur.com/XlO9gT1.jpg", "https://i.imgur.com/TxbVnYH.jpg", "https://i.imgur.com/GByLJMH.png")
        await staff_shenanimonks.send(random.choice(images))
        # frequency is every 2 days
        await asyncio.sleep(172800)




# penguin penguin penguin


# Run command: important always keep at the end
client.loop.create_task(update_your_sheets())
client.run(token)