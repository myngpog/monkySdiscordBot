from discord.ext import commands
import discord, asyncio, random
from discord import File


#id: 736704193905164438

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

bot = commands.Bot(command_prefix='.')

client = discord.Client()

# Welcome
@client.event
async def on_member_join(member):
    channel = client.get_channel(736726612070105171)
    channel2 = client.get_channel(736727913793192026)
    channel3 = client.get_channel(736739974153633843)
    await channel.send(f"Welcome to the jungle {member.mention}! Please look under {channel2.mention} for rules, then {channel3.mention} to be freed into the wild aha haa. pls stay")

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

            # 2nd bruh bc im dumb
            def check(s):
                return (s.author == message.author and s.channel == message.channel)

            bruh = await client.wait_for('message', check=check)

            # if DONE
            if str(bruh.content) == 'DONE':
                channel2 = client.get_channel(738107566692761721)
                newapplicant = message.author.mention
                NASA1 = client.get_user(315869723373862917)
                NASA2 = client.get_user(208108164061593600)
                NASA3 = client.get_user(472238811691352065)
                NASA4 = client.get_user(564523794920767488)
                await channel2.send(f'New application pog! {NASA1.mention}, {NASA2.mention}, {NASA3.mention}, {NASA4.mention}. App from {newapplicant}')
                await message.channel.send('Thank you for your application! We\'ll get back to you ASAP!')

                # expose dms
                counter = 0
                channelbruh = message.channel
                async for message in channelbruh.history(limit=10, after=ao3pog):
                    if message.author == client.user:
                        counter += 1
                    channelbruhbruh = client.get_channel(738107566692761721)
                    await channelbruhbruh.send(message.content)


            # if CANCEL
            if str(bruh.content) == 'CANCEL':
                await message.channel.send('Sorry to see you go D^: we hope you continue to support us!')

            # Else
            else:
                pass


# bot playing game
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='monkyS is looking for new recruits aha haa'))
# upload image
    @client.loop
    async def bacground_task():
        await client.wait_until_ready()
        counter = 0
        ao3 = client.get_channel(738107566692761721)
        while not client.is_closed():
            counter +=1
            images = ("https://i.imgur.com/CxgOaFc.png", "https://i.imgur.com/00mZeGt.png")
            await ao3.send(random.choice(images))
            await asyncio.sleep(10)

    client.loop.create_task(bacground_task())


# Run command: important always keep at the end
client.run(token)