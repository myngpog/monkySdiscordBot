import discord

#id: 736704193905164438

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines [0].strip()

token = read_token()

client = discord.Client()

#Welcome
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
                          f" READ the corresponding docs for further instructions. After you're done, fill out this form: https://forms.gle/sJab4HYuxdH6p9aP6 "
                          f"& REPLY TO ME (yes this bot) WITH 'DONE' (caps matter) for a faster response time. Thank you for your interest! -NASA Space Monks!")
# Reply and notify NASA Space Monks
@client.event
async def on_message(message):
    if message.guild is None:
        test = client.get_channel(738107566692761721)
        NASA1 = client.get_user(315869723373862917)
        NASA2 = client.get_user(208108164061593600)
        NASA3 = client.get_user(472238811691352065)
        NASA4 = client.get_user(564523794920767488)
        if message.content.startswith('DONE'):
            await message.author.send('Thank you for applying! We will get back to you asap! -NASA Space Monks')
            # Forward app to NASA Space Monks
            await test.send(f'New app has been submitted {NASA1.mention}, {NASA2.mention}, {NASA3.mention}, {NASA4.mention}')


# Run command: important always keep at the end
client.run(token)