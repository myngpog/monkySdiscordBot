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
                          f" READ the corresponding docs for further instructions. After you're done, please type 'APPLY' to begin your application process."
                          f" ** If i send 2 questions at a time, ANSWER THEM BOTH IN ONE MESSAGE to prevent an error.**")


# APPLY
@client.event
async def on_message(message):
    if message.guild is None:
        if str(message.content) == 'APPLY':
            def check(no):
                return no.channel == message.channel
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
            await message.author.send("Lastly, please type 'DONE' to submit your application, or type 'CANCEL' to cancel lmao.")

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
                await channel2.send(f'New application pog! {NASA1}, {NASA2}, {NASA3}, {NASA4}. App from {newapplicant}')
                await message.channel.send('Thank you for your application! We\'ll get back to you ASAP!')

                # expose dms
                counter = 0
                channelbruh = message.channel
                async for message in channelbruh.history(limit=12, oldest_first=True).flatten():
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


            # final step







# Run command: important always keep at the end
client.run(token)