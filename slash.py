import discord
from discord.ext import commands
import datetime

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith(',hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith(',who'):
        await client.send_message(message.channel, "I was made by Zorio#5213")
    elif message.content.upper().startswith(',PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    elif message.content.upper().startswith(',SAY'):
        args = message.content.split(" ")
        #args[0] = !SAY
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    elif message.content.startswith(',help'):
        await client.send_message(message.author, "Commands:\n" \
                                                  "• ,help - Sends the user a DM with all of the commands\n" \
                                                  "• ,hello - Responds with Hello and pings the user\n" \
                                                  "• ,ping - Pings the bot to see if it is online and recieving commands\n" \
                                                  "• ,say - Add a sentence or letter to the end and the bot will repeat it\n" \
                                                  "• ,who - Tells the user who created the bot")
    # Allows owner to set the game status of the bot
    elif message.content.startswith('o'
                                    ',shutdown') and message.author.id == '210372181794881546':
        await client.send_message(message.channel, 'Shutting down. Bye!')
        await client.logout()
        await client.close()
    elif message.content.startswith(',status') and message.author.id == '210372181794881546' or message.content.startswith(',status') and message.author.id == '242991640078188545':
        await client.change_presence(game=discord.Game(name=message.content[7:]))

@client.event
async def on_message(message):
    if message.content.startswith(',apply'):
        await client.send_message(message.channel, "Thank you for your application,! Spamming this command will result in a ban.")
        appl = '{0.author.mention} Has applied to be a Freelancer'.format(message)
        await client.send_message(client.get_channel('477862038220177411'), appl)

    elif message.content.startswith(',pwu') and message.author.id == '210372181794881546':
        emb = (discord.Embed(description='Please welcome <@!210372181794881546> to the staff team!', colour=0x3DF270))
        wel = emb.set_author(name='Staff Announcement')
        await client.send_message(client.get_channel('477524889188827161'), embed=emb)

@client.event
async def on_member_join(member):
    emb = (discord.Embed(description='Welcome to the server {0}! Please read <#477525877618638861> before continuing on to chat. If you would like to apply for a Freelancer position please type `,apply`. Enjoy your time here :thumbsup:'.format(member.mention, member.server.name), colour=0x3DF270))
    wel = emb.set_author(name='Member Join', icon_url='https://cdn.discordapp.com/attachments/243356707080634368/477532339988332554/SlashSetups2cubicwhite.png')
    await client.send_message(client.get_channel('477526414346944523'), embed=emb)

@client.event
async def on_message(message):
    if 'prefix' in message.content:
        await client.send_message(message.channel, 'Type `,` then your message to talk to me')
        return

    elif message.content.startswith(',clear') and message.author.id == '210372181794881546':
        tmp = await client.send_message(message.channel, 'Clearing messages...')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)

    elif message.content.startswith(',rules') and message.author.id == '210372181794881546':
        emb = (discord.Embed(description='1. Be polite/respectful. No slurs (this includes casual conversation)\n'
                                         '2. No advertisements / Posting links without permission\n'
                                         '3. No ban/mute dodges.\n'
                                         '4. Keep channels free of conversation not related to that genre.\n'
                                         '5. No Drama\n'
                                         '6. English only unless in <#477871691175821313> channel\n'
                                         '7. No spamming/mic spam  Breaking any of these rules may get you banned.', colour=0x3DF270))
        wel = emb.set_author(name='The Rules')
        await client.send_message(client.get_channel('477524889188827161'), embed=emb)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDc3NTM0MDE0NjU2NDc5MjQz.Dk9i6g.Af46vcFVlg1VhYX3p7dlyNxrriE')
