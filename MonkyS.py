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
                          f" READ the corresponding docs for further instructions. After you're done, please respond to me with 'APPLY' to begin your application process."
                          f" ** If i somehow malfunction during application process, answer all the questions in it's corresponding order and it'll still work**")


# APPLY
@client.event
async def on_message(message):
    if message.guild is None:
        if message.content.startswith('APPLY'):
            def check(no):
                return no.channel == message.channel
            await message.author.send('What role(s) are you interested in applying for?')
            # Chapters
            await client.wait_for('message', check=check)
            if True: await message.author.send('How many chapters can you do per week?')
            # Volunteer
            await client.wait_for('message', check=check)
            if True: await message.author.send('Do you understand that this is volunteer work?')
            # Link
            await client.wait_for('message', check=check)
            if True: await message.author.send('Link your test or past work (if test, make sure we have edit/suggestion perms)')
            # Finale
            await client.wait_for('message', check=check)
            if True: await message.author.send("Lastly, please type 'DONE' to submit your application, or don't reply to not submit lmao.")

            # 2nd bruh bc im dumb
            def check(s):
                return (s.author == message.author and s.channel == message.channel)
            E = 'DONE'
            N = 'CANCEL'

            bruh = await client.wait_for('message', check=check)

            if str(bruh.content) == E:
                await message.channel.send('Thank you for your application! We\'ll get back to you ASAP!')
            if str(bruh.content) == N:
                await message.channel.send('Sorry to see you go D^: we hope you continue to support us!')

            else:
                pass


            # final step







# Run command: important always keep at the end
client.run(token)