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

    if message_id == 740298503854751815:
        await member.send(f"Here is the link to the tests: https://drive.google.com/drive/folders/15_QheyCOo_Xrzfrju7cKkXMPL854p8L8?usp=sharing ," 
                          f" READ the corresponding docs for further instructions. After you're done, please type 'APPLY' to begin your application process.")


# APPLY
@client.event
async def on_message(message):
    if message.guild is None:
        if str(message.content) == 'APPLY':
            def check(no):
                return no.channel == message.channel
            ao3pog = await message.author.send('Application process started~')
            await message.author.send('What role(s) are you interested in applying for?')
            # Chapters
            await client.wait_for('message', check=check)
            await message.author.send('How many chapters can you do per week?')
            # Volunteer
            await client.wait_for('message', check=check)
            await message.author.send('Do you understand that this is volunteer work?')
            # Link
            await client.wait_for('message', check=check)
            await message.author.send('Link your test or past work (if test, make sure we have edit/suggestion perms)')
            # Finale
            await client.wait_for('message', check=check)
            await message.author.send("Lastly, please type 'DONE' to submit your application, or type 'CANCEL' to cancel lmao. If I don't respond with a confirmation after your reply, redo the app process again by typing 'APPLY'.")

            # 2nd bruh bc im dumb but idk waht this is for
            def check(s):
                return (s.author == message.author and s.channel == message.channel)

            bruh = await client.wait_for('message', check=check)

            # if DONE
            if str(bruh.content) == 'DONE':
                newapplicant = message.author.mention
                NASA1 = client.get_user(315869723373862917)
                NASA2 = client.get_user(208108164061593600)
                NASA3 = client.get_user(472238811691352065)
                NASA4 = client.get_user(564523794920767488)
                test = client.get_channel(738107566692761721)
                (await message.channel.send('Thank you for your application! We will get back to you ASAP!'))
                (await test.send(f'New application pog! {NASA1.mention}, {NASA2.mention}, {NASA3.mention}, {NASA4.mention}. App from {newapplicant}'))

                # expose dms
                dm = []
                channelbruhbruh = client.get_channel(738107566692761721)
                counter = 0
                channelbruh = message.channel
                messages = await channelbruh.history(limit=10, after=ao3pog).flatten()
                if message.author == client.user:
                    counter += 1
                    messages = message.content.split('\n')
                for message in messages:
                    dm.append(message.content)
                final = "```" + '\n\n'.join([''.join(map(str, item)) for item in dm]) + "```"
                await channelbruhbruh.send(final)

            # if CANCEL
            if str(bruh.content) == 'CANCEL':
                await message.channel.send('Sorry to see you go D^: we hope you continue to support us!')

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


    # Variables because APCSP is actually good for something
    abb = ("**Series abbreviations:** \n**TMM** for Take My Money \n**APITS** for A Place in the Sun \n**IAM** for I am Han Sanqian"
            "\n**OG** for Ordinary Girl (*on haitus*) "
            "\n**BTY** for Blind to You \n -drive to get drive link")
    droppedseries = ('**Dropped series -** One Plus One, Someday I want to die, Young Lady')
    TMM = ("https://drive.google.com/drive/folders/1b39GLkqvf6O3e4oF8YHpvTyNZI877evH?usp=sharing")
    BTY = ("https://drive.google.com/drive/folders/1AjlmzrOdsbh7D4RlzPpWppiYl7bJMOk9?usp=sharing")
    APITS = ("https://drive.google.com/drive/folders/1Z9-22iD9S-njMatW2XCILqTF1zM4XENF?usp=sharing")
    IAM = ("https://drive.google.com/drive/folders/1E5b4fz7OEGC-MnMxScd4SZo5zLwj3z4I?usp=sharing")
    DIE = ("dropped, the raws page was taken down")
    OG = ("**ON CONFIRMED HIATUS** https://drive.google.com/drive/folders/1c4z_7VA4vFgBNPb2bnlGKsHZcdqfGbBN?usp=sharing")
    drive = ('https://drive.google.com/drive/folders/1gBRNYPAqWtQ26j1uCoCqioWBoAg0nXJa?usp=sharing')
    YL = ('**YL Collab -** https://drive.google.com/drive/folders/1C8hDP_3_JtU6QGCA9y9CaIlYumRqrOvc **Sheets -** https://docs.google.com/spreadsheets/d/1YPVqFFnnsiMeURTpDW056atqII4S5SPWMjBG7JwmeQc/edit#gid=0')
    sheets = ('UPDATE THE SHEETS PLS ISTG https://docs.google.com/spreadsheets/d/1s_k8RTbT5VBCd3yvSH353OX4AlewhfAlVg8uLk3iJT4/edit?usp=sharing')
    BUD = ('https://drive.google.com/drive/folders/1A0soi1Yz2BWQ9dspi7khoTw7jPz3qVyJ?usp=sharing')
    bot_help = ("```Thank you for using the bot~\n"
                "-halp for bot help lol\n"
                "-abb for series abbreviations\n"
                "-[Series abbreviation] for the link to the series drive\n"
                "-sheets for link to sheets\n"
                "-drive for link to drive\n"
                "-dropped for our dropped series\n"
                "-hiatusadd [name] to add yourself to our hiatus list\n"
                "-hiatusremove [name on hiatus list] to remove yourself from our hiatus list```")


#should also look into changing on_message() to prefixes
# should look to changing these into function with parameters
    #staff shenanimonks
    if message.channel == ss:
        if str(message.content) == "-abb":
            await ss.send(abb)
        if str(message.content) == "-halp":
            await ss.send(bot_help)
        if message.content.startswith("-whalecum"):
            user = message.mentions[0]
            await ss.send(f"Welcome " + user.mention + "! To start off, please put your email under {email.mention} for future references."
        f"** Fill out the staff spreadsheet** under {links.mention}, **our scans drive link is also under there**."
        f" After you're done with a chapter, please update under {updates.mention} and *update the sheets*."
        f" To see what stuff you're assigned, look at the sheets or get a link to the sheets through our bot under {not_bot.mention} by doing -halp."
        f" Once again, welcome!")


    #actual work channel
    if message.channel == actual_work:
        if str(message.content) == "-abb":
            await actual_work.send (abb)
        if str(message.content) == '-dropped':
            await actual_work.send(droppedseries)
        if str(message.content) == '-TMM':
            await actual_work.send(TMM)
        if str(message.content) == '-BTY':
            await actual_work.send(BTY)
        if str(message.content) == '-APITS':
            await actual_work.send(APITS)
        if str(message.content) == '-IAM':
            await actual_work.send(IAM)
        if str(message.content) == '-DIE':
            await actual_work.send(DIE)
        if str(message.content) == '-OG':
            await actual_work.send(OG)
        if str(message.content) == '-drive':
            await actual_work.send(drive)
        if str(message.content) == '-YL':
            await actual_work.send(YL)
        if str(message.content) == '-sheets':
            await actual_work.send(sheets)
        if str(message.content) == '-BUD':
            await actual_work.send(BUD)
        if str(message.content) == "-halp":
            await actual_work.send(bot_help)
        if message.content.startswith("-whalecum"):
            user = message.mentions[0]
            await actual_work.send(f"Welcome " + user.mention + f"! To start off, please put your email under {email.mention} for future references."
        f"** Fill out the staff spreadsheet** under {links.mention}, **our scans drive link is also under there**."
        f" After you're done with a chapter, please update under {updates.mention} and *update the sheets*."
        f" To see what stuff you're assigned, look at the sheets or get a link to the sheets through our bot under {not_bot.mention} by doing -halp."
        f" Once again, welcome!")



    #not_bot channel
    if message.channel == not_bot:
        if str(message.content) == "-abb":
            await not_bot.send (abb)
        if str(message.content) == '-dropped':
            await not_bot.send(droppedseries)
        if str(message.content) == '-TMM':
            await not_bot.send(TMM)
        if str(message.content) == '-BTY':
            await not_bot.send(BTY)
        if str(message.content) == '-APITS':
            await not_bot.send(APITS)
        if str(message.content) == '-IAM':
            await not_bot.send(IAM)
        if str(message.content) == '-DIE':
            await not_bot.send(DIE)
        if str(message.content) == '-OG':
            await not_bot.send(OG)
        if str(message.content) == '-drive':
            await not_bot.send(drive)
        if str(message.content) == '-YL':
            await not_bot.send(YL)
        if str(message.content) == '-sheets':
            await not_bot.send(sheets)
        if str(message.content) == '-BUD':
            await not_bot.send(BUD)
        if str(message.content) == "-halp":
            await not_bot.send(bot_help)

    #monky shrine
    if message.channel == monky_shrine:
        if str(message.content) == "-abb":
            await monky_shrine.send(abb)
        if str(message.content) == '-dropped':
            await monky_shrine.send(droppedseries)
        if str(message.content) == '-TMM':
            await monky_shrine.send(TMM)
        if str(message.content) == '-BTY':
            await monky_shrine.send(BTY)
        if str(message.content) == '-APITS':
            await monky_shrine.send(APITS)
        if str(message.content) == '-IAM':
            await monky_shrine.send(IAM)
        if str(message.content) == '-DIE':
            await monky_shrine.send(DIE)
        if str(message.content) == '-OG':
            await monky_shrine.send(OG)
        if str(message.content) == '-drive':
            await monky_shrine.send(drive)
        if str(message.content) == '-YL':
            await monky_shrine.send(YL)
        if str(message.content) == '-sheets':
            await monky_shrine.send(sheets)
        if str(message.content) == '-BUD':
            await monky_shrine.send(BUD)

    await client.process_commands(message)

#hiatus family tingz
hiatus_List = []
test = client.get_channel(738107566692761721)
@client.command()
async def hiatusadd(ctx, arg):
    if ctx.channel == test:
        messages = await ctx.send(f'{arg} has been added to the hiatus list! To remove please do -hiatusremove {arg}')
        for ctx.message in messages:
            hiatus_List.append(arg)


hiatus_Final = (f'**Staff on hiatus/quit:**' + '\n'.join([''.join(map(str, item)) for item in hiatus_List]))

@client.command()
async def hiatus(ctx):
    if ctx.channel == test:
        await ctx.send(hiatus_Final)







# bot playing game
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="wear a mask and wash your hands kekw + we're recruiting!"))


# update the sheets image
async def update_your_sheets():
    await client.wait_until_ready()
    staff_shenanimonks = client.get_channel(736735728364683264)
    while not client.is_closed():
        images = ("https://i.imgur.com/CxgOaFc.png", "https://i.imgur.com/00mZeGt.png", "https://i.imgur.com/efwN7Sc.jpg", "https://i.imgur.com/G4FPSnw.jpg")
        await staff_shenanimonks.send(random.choice(images))
        # frequency is every 2 days
        await asyncio.sleep(172800)


# penguin penguin penguin


# Run command: important always keep at the end
client.loop.create_task(update_your_sheets())
client.run(token)