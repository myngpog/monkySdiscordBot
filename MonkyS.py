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
                          f" READ the corresponding docs for further instructions. After you're done, please type 'APPLY' to begin your application process."
                          f" ** Please bold your responses so blind ao3 (aoi) can see them better when we read over your app or else she'll berate you.**")


# APPLY
@client.event
async def on_message(message):
    if message.guild is None:
        if str(message.content) == 'APPLY':
            def check(no):
                return no.channel == message.channel
            ao3pog = await message.author.send('Application process started~')
            await message.author.send('*What role(s) are you interested in applying for?*')
            # Chapters
            await client.wait_for('message', check=check)
            await message.author.send('*How many chapters can you do per week?*')
            # Volunteer
            await client.wait_for('message', check=check)
            await message.author.send('*Do you understand that this is volunteer work?*')
            # Link
            await client.wait_for('message', check=check)
            await message.author.send('*Link your test or past work (if test, make sure we have edit/suggestion perms)*')
            # Finale
            await client.wait_for('message', check=check)
            await message.author.send("Lastly, please type 'DONE' to submit your application, or type 'CANCEL' to cancel lmao **(don't bold it)**. *If i don't respond after your reply, redo the app process again by typing 'APPLY'.*")

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
                (await test.send(f'New application pog! {NASA1}, {NASA2}, {NASA3}, {NASA4}. App from {newapplicant}'))

                # expose dms
                dm = []
                channelbruhbruh = client.get_channel(738107566692761721)
                counter = 0
                channelbruh = message.channel
                messages = await channelbruh.history(limit=10, after=ao3pog).flatten()
                if message.author == client.user:
                    counter += 1
                for message in messages:
                    dm.append(message.content)
                await channelbruhbruh.send(dm)

            # if CANCEL
            if str(bruh.content) == 'CANCEL':
                await message.channel.send('Sorry to see you go D^: we hope you continue to support us!')

            # Else
            else:
                pass

    # Staff welcome message
    welcomepog = client.get_channel(736735728364683264)
    secret = client.get_channel(736704193905164441)
    confused = client.get_channel(736741523051511851)
    email = client.get_channel(736992278308192326)
    links = client.get_channel(736741434652360765)
    updates = client.get_channel(736747148263292929)


    # Variables because APCSP is actually good for something
    helpmepls = ("**Series abbreviations:** **TMM** for Take My Money, **APITS** for A Place in the Sun, **IAM** for I am Han Sanqian, "
            "**OG** for Ordinary Girl (*on haitus*), **DIE** for Someday, I want to die (*hiatus?*), "
            "**BTY** for Blind to You, **ATL** for A Tail Love **-drive to get drive link**")
    droppedseries = ('**Dropped series -** One Plus One')
    TMM = ("https://drive.google.com/drive/folders/1b39GLkqvf6O3e4oF8YHpvTyNZI877evH?usp=sharing")
    BTY = ("https://drive.google.com/drive/folders/1AjlmzrOdsbh7D4RlzPpWppiYl7bJMOk9?usp=sharing")
    APITS = ("https://drive.google.com/drive/folders/1Z9-22iD9S-njMatW2XCILqTF1zM4XENF?usp=sharing")
    IAM = ("https://drive.google.com/drive/folders/1E5b4fz7OEGC-MnMxScd4SZo5zLwj3z4I?usp=sharing")
    DIE = ("it's been on hiatus for how long? https://drive.google.com/drive/folders/17owmv_ccNQydyq52-V2q74C4g7zQreBl?usp=sharing")
    OG = ("**ON CONFIRMED HIATUS** https://drive.google.com/drive/folders/1c4z_7VA4vFgBNPb2bnlGKsHZcdqfGbBN?usp=sharing")
    drive = ('https://drive.google.com/drive/folders/1gBRNYPAqWtQ26j1uCoCqioWBoAg0nXJa?usp=sharing')
    YL = ('**YL Collab -** https://drive.google.com/drive/folders/1C8hDP_3_JtU6QGCA9y9CaIlYumRqrOvc **Sheets -** https://docs.google.com/spreadsheets/d/1YPVqFFnnsiMeURTpDW056atqII4S5SPWMjBG7JwmeQc/edit#gid=0')
    sheets = ('UPDATE THE SHEETS PLS ISTG https://docs.google.com/spreadsheets/d/1s_k8RTbT5VBCd3yvSH353OX4AlewhfAlVg8uLk3iJT4/edit?usp=sharing')
    BUD = ('https://drive.google.com/drive/folders/1A0soi1Yz2BWQ9dspi7khoTw7jPz3qVyJ?usp=sharing')
    welcome = (
        f"Welcome! To start off, please put your email under {email.mention} for future references."
        f"** Fill out the staff spreadsheet** under {links.mention}, **our scans drive link is also under there**."
        f" After you're done with a chapter, please update under {updates.mention} and *update the sheets*."
        f" To see what stuff you're assigned, look at the sheets or get a link to the sheets through our bot under {confused.mention}."
        f" Once again, welcome!")


    #staff shenanimonks
    if message.channel == welcomepog:
        if str(message.content) == "-halp":
            await welcomepog.send (helpmepls)
        if str(message.content) == '-dropped':
            await welcomepog.send(droppedseries)
        if str(message.content) == '-TMM':
            await welcomepog.send(TMM)
        if str(message.content) == '-BTY':
            await welcomepog.send(BTY)
        if str(message.content) == '-APITS':
            await welcomepog.send(APITS)
        if str(message.content) == '-IAM':
            await welcomepog.send(IAM)
        if str(message.content) == '-DIE':
            await welcomepog.send(DIE)
        if str(message.content) == '-OG':
            await welcomepog.send(OG)
        if str(message.content) == '-drive':
            await welcomepog.send(drive)
        if str(message.content) == '-YL':
            await welcomepog.send(YL)
        if str(message.content) == '-sheets':
            await welcomepog.send(sheets)
        if str(message.content) == '-BUD':
            await welcomepog.send(BUD)
        if str(message.content) == '-whalecum':
            await welcomepog.send(welcome)

        #hiatus
        if str(message.content) == '-hiatus':
            await welcomepog.send('**Hiatus people: ** idfk ill fix this later')


    #confused channel
    if message.channel == confused:
        if str(message.content) == "-halp":
            await confused.send (helpmepls)
        if str(message.content) == '-dropped':
            await confused.send(droppedseries)
        if str(message.content) == '-TMM':
            await confused.send(TMM)
        if str(message.content) == '-BTY':
            await confused.send(BTY)
        if str(message.content) == '-APITS':
            await confused.send(APITS)
        if str(message.content) == '-IAM':
            await confused.send(IAM)
        if str(message.content) == '-DIE':
            await confused.send(DIE)
        if str(message.content) == '-OG':
            await confused.send(OG)
        if str(message.content) == '-drive':
            await confused.send(drive)
        if str(message.content) == '-YL':
            await confused.send(YL)
        if str(message.content) == '-sheets':
            await confused.send(sheets)
        if str(message.content) == '-BUD':
            await confused.send(BUD)
        if str(message.content) == '-hiatus':
            await confused.send('**Hiatus people: **')

    #monky shrine
    if message.channel == secret:
        if str(message.content) == "-halp":
            await welcomepog.send(helpmepls)
        if str(message.content) == '-dropped':
            await secret.send(droppedseries)
        if str(message.content) == '-TMM':
            await secret.send(TMM)
        if str(message.content) == '-BTY':
            await secret.send(BTY)
        if str(message.content) == '-APITS':
            await secret.send(APITS)
        if str(message.content) == '-IAM':
            await secret.send(IAM)
        if str(message.content) == '-DIE':
            await secret.send(DIE)
        if str(message.content) == '-OG':
            await secret.send(OG)
        if str(message.content) == '-drive':
            await secret.send(drive)
        if str(message.content) == '-YL':
            await secret.send(YL)
        if str(message.content) == '-sheets':
            await secret.send(sheets)
        if str(message.content) == '-BUD':
            await secret.send(BUD)
        if str(message.content) == '-hiatus':
            await secret.send('**Hiatus people: **')



# bot playing game
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="wear a mask and wash your hands kekw + we're recruiting!"))


# upload image
async def update_your_sheets():
    await client.wait_until_ready()
    ao3 = client.get_channel(736735728364683264)
    while not client.is_closed():
        images = ("https://i.imgur.com/CxgOaFc.png", "https://i.imgur.com/00mZeGt.png", "https://i.imgur.com/efwN7Sc.jpg", "https://i.imgur.com/G4FPSnw.jpg")
        await ao3.send(random.choice(images))
        await asyncio.sleep(172800)


# penguin penguin penguin


# Run command: important always keep at the end
client.loop.create_task(update_your_sheets())
client.run(token)