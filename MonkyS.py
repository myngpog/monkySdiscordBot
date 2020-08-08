import discord

#id: 736704193905164438

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

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
                          f" READ the corresponding docs for further instructions. After you're done, please respond to me with 'APPLY' to begin your application process.")


# APPLY
@client.event
async def on_message(message):
    if message.guild is None:
        if message.content.startswith('APPLY'):
            await message.author.send('What role(s) are you interested in applying for?')
            # Chapters
            await client.wait_for('message', check=None)
            if True: await message.author.send('How many chapters can you do per week?')
            # Volunteer
            await client.wait_for('message', check=None)
            if True: await message.author.send('Do you understand that this is volunteer work?')
            # Link
            await client.wait_for('message', check=None)
            if True: await message.author.send('Link your test or past work (if test, make sure we have edit/suggestion perms)')
            # Finale
            await client.wait_for('message', check=None)
            if True: await message.author.send("Lastly, please react with '👍' to submit your application, or type 'CANCEL' to cancel.")

            # DONE or CANCEL NEEDS WORKING


            await client.wait_for('reaction_add', timeout=60.0, check=None)
            channel = client.get_channel(738107566692761721)
            NASA1 = client.get_user(315869723373862917)
            NASA2 = client.get_user(208108164061593600)
            NASA3 = client.get_user(472238811691352065)
            NASA4 = client.get_user(564523794920767488)
            if True: await message.author.send('Thank you for your application! We\'ll get back to you ASAP!')
            await channel.send(f'New Monky pog! {NASA1}, {NASA2}, {NASA3}, {NASA4}')

            await client.wait_for('message = CANCEL', check=None)
            if True: await message.author.send('Sorry to see you go D^: we hope you continue to support us!')






# Run command: important always keep at the end
client.run(token)