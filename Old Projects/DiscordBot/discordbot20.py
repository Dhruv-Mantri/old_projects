import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import time
import asyncio
import threading

prefix = "!"
intents = discord.Intents.all()
intents.members = True
bot = Bot(command_prefix=prefix, intents=intents)

roast_list = ["I hear you come from Loserville","you have a stain on your shirt","nice hairline loser","I would roast you, but my mom told me not to burn trash","you are trash","you can't even get a roblox gf","sorry i can't hear you I have airpods in","you're like the magikarp of people. Useless","You aren't just a clown, you're an entire circus",,"if you had a nickel for every friend you have, you would be homeless","have a nice day","get pinged","it's impossible to underestimate you","you bring everyone joy... when you leave the room","I thought of you today. It reminded me to take out the trash", "If I throw a stick, will you leave?", "Light travels faster than sound, which is why you seemed bright until you spoke.", "Your secrets are always safe with me. I never even listen when you tell me them.", "I’ll never forget the first time we met. But I’ll keep trying.", "Someday you'll go far. And I hope you stay there.", "If laughter is the best medicine, then your face must be curing the world.", "Don’t be ashamed of who you are. That’s your parents’ job.", "When I see your face, there's not a single thing I would change, except the direction I was walking in."]

bot_users = [] # usernames that are allowed to use the bot
bad_users = []
valid_channels = [] # limit quack to certain channels if server chooses
spam_channels = [] #trigger in the spam area where Quack cena spouts nonsense
quackcena_variants = ['QuackCena',"Quackcena","quackcena", "quack cena"]

help_page = ["roast", "enlighten"]

lawyer_pronoun = ["He","Lawyer","They","Books","Have you", "Has the government","It","Are","Answer me", "The"]
lawyer_noun = ["gavels","lemons","promise","tornado","heart","shelf","books","words","car","without permission","briefcase","gorilla","lemons","you","me","fruit","banana"]
lawyer_verb = ["has","opened","walked","stands","eaten","been","sold your","opens","is","only lawyers","may touch"]
lawyer_adj = ["good","broken","next to","too many","hurt","in a","accidental","lungs","a","filled with","Mesothelioma","justice", "good"]

spam_allowed = True

def cooldown(howlong):
    time.sleep(howlong)
    return True

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    botguilds = bot.guilds
    print(botguilds)
    await bot.change_presence(activity=discord.Game("Untitled Goose Game"))

@bot.event
async def on_member_join(member):
    for channel in member.guild.channels: #all the channels in the server
        if str(channel) == "general":
            await bot.send_message(f"""Welcome to the server {member.mention}""")

@bot.event
async def on_message(message):
    print(message.content)

    global_message = str(message.content).lower()
    global_message_words = global_message.split(" ")

    if message.author == bot.user or message.author in bad_users:
        await message.author.send("Frick you")
        return

    if message.content.startswith("hello"):
        await message.channel.send(f'hello {message.author.mention}!')

    # if message.content.count("lol") >= 1:
    #     await message.channel.send('lelelel')

    if "lol" in global_message:
        await message.channel.send("lelelel")
    
    # if "lmao" in global_message:
    #     await message.channel.send('Where is your donkey now?')

    if "bruh" in global_message:
        await message.channel.send('bruh bruh bruh bruh')

    if message.content.startswith("who") or message.content.startswith("what") or message.content.startswith("Who") or message.content.startswith("What"):
        await message.channel.send(f"{message.author.mention} your mom")

    if message.content.startswith("where") or message.content.startswith("Where"):
        await message.channel.send(f"{message.author.mention} your mom's house")

    # for word in bad_word:
    #     if message.content.count(word) > 0:
    #         await message.channel.purge(limit=1)
    #         await message.channel.send(f"no bad words {message.author.mention} you dingus")

    if "indeed" in global_message:
        await message.channel.send(f"{message.author.mention} Indeed.")

    if message.content.startswith("so") or message.content.startswith("So"):
        await message.channel.send(f"{message.author.mention} Indeed.")

    if message.content.startswith("is ") or message.content.startswith("Is"):
        await message.channel.send(f"{message.author.mention} Indeed.")
    
    if message.content.startswith("if") or message.content.startswith("If"):
        await message.channel.send(f"{message.author.mention} Indeed.")

    if message.content.startswith("interesting") or message.content.startswith("Interesting"):
        await message.channel.send(f"{message.author.mention} Indeed.") 

    if message.content.startswith(prefix + "roast"):
        if message.content.count("<@!748249174780280842>") > 0:
            await message.channel.purge(limit=1)
            await message.channel.send(f"Shut your face you piece of doodoo {message.author.mention}")
            return
        # if str(message.author) in bad_users:
        #     await message.channel.send(f"{message.author.mention} nah I'm good")
        #     return
        else:
            await message.channel.purge(limit=1)
    
    # else:
    #     await message.channel.send("Jeez man chill. roast again in "+str(time.time()-t)+" seconds")
        # cooldown_thread.start()
    if message.content == prefix + "help":
        embed = discord.Embed(title="QuackCena Help Page", url="https://SolidTediousImplementation.mandhr.repl.co",description="The useful commands of QuackCena!",color=discord.Color.blue())
        for i, m in enumerate(help_page):
            embed.add_field(name=m, value=f"{m} someone", inline=True)
        await message.channel.send(content=None, embed=embed)

    if message.content.startswith(prefix+"delete") and str(message.author) == "[bot owner id]":
        deletes = int(str(message.content).split(" ")[1])+1
        await message.channel.purge(limit=deletes)
    
    if message.content.startswith("initiate sequence delta53 --! alpha monkey") and str(message.author) in bot_users:
        await message.channel.send("Commencing with Sequence Delta Code 53 Alpha Monkey. All of you are being monitored by the CIA. The FBI has planted bombs outside of your house and your mom's house and they will be activated if you do not comply. Lieutenant John Cena and Zoobamafoo are on patrol duty. You are surrounded. You have no options.")

    if message.content.count("enlighten") >= 1:
        x = random.randint(0,len(lawyer_pronoun)-1)
        y = random.randint(0,len(lawyer_verb)-1)
        z = random.randint(0,len(lawyer_adj)-1)
        w = random.randint(0,len(lawyer_noun)-1)
        await message.channel.send("{} {} {} {}".format(lawyer_pronoun[x],lawyer_verb[y],lawyer_adj[z],lawyer_noun[w]))
        

    await bot.process_commands(message)

# @bot.command(name="quack")
# async def activate(ctx, arg):
#     global on
#     if str(ctx.author) in bot_users:
#         if arg == "quack":
#             on = True
#             await ctx.send("activated")
#         elif arg == "goose":
#             on = False
#             await ctx.send("it's nap time byeee")

@bot.command(name="lol")
async def _lol(ctx):
    await ctx.send("lelelel")

@bot.command()
async def repeat(ctx, arg):
    if str(ctx.author) not in bad_users:
        await ctx.send(arg)

@commands.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def roast(ctx, arg):
    if str(ctx.author) not in bad_users:
        await ctx.send("{} {}".format(arg, roast_list[random.randint(0,len(roast_list)-1)]))

@roast.error
async def roast_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = "```Chill with the roasts. Try again in {:.1f}s```".format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error

@commands.command()
async def spam(ctx, arg, argnum = 1):
    if argnum > 1000:
        argnum = 1000
    global spam_allowed
    if str(ctx.channel) in spam_channels:
        if str(arg) == "terminate":
            spam_allowed = False
            await ctx.send("Spam stopped")
        elif str(arg) == "initiate" and str(ctx.author) in bot_users:
            spam_allowed = True
            await ctx.send("Spam recommencing")
        if str(ctx.author) not in bad_users:
            for i in range(0,int(argnum)):
                if spam_allowed:
                    await ctx.send(arg)
        else:
            print("{} is ignored.".format(ctx.author))
    else:
        await ctx.send("go to a spam channel")
        

@commands.command()
async def addspamchannel(ctx, arg):
    if str(ctx.author) == "[bot owner id]":
        spam_channels.append(str(arg))

@commands.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, mute_time : int):
    theguild = ctx.guild
    for role in theguild.roles:
        if role.name == "muted":
            await member.add_roles(role)
            await ctx.send(f"{member.mention} has been muted.")
            await asyncio.sleep(mute_time)
            await member.remove_roles(role)
            await ctx.send(f"{member.mention} is unmuted!")

@commands.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    if str(ctx.author) == "[bot owner id]":
        await member.kick(reason= reason)
        await ctx.send("Member kicked.")
    else:
        await ctx.send(f"{ctx.author.mention}, you have no power. None.")

@commands.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    if str(ctx.author) == "[bot owner id]":
        await member.ban(reason= reason)

@commands.command()
async def ignore(ctx, arg : discord.Member, *, reason=None):
    if str(ctx.author) == "[bot owner id]":
        user_name = arg
        bad_users.append(user_name)
        await arg.send("I'm gonna be giving you the cold shoulder now.")
        await ctx.send(f"{arg.mention} is now being ignored: {reason}")


@commands.command()
async def unignore(ctx, arg : discord.Member, *, reason=None):
    if str(ctx.author) == "[bot owner id]":
        user_name = arg
        bad_users.remove(user_name)
        await arg.send("I believe you have reformed so I will forgive you.")
        await ctx.send(f"{arg.mention} is now not being ignored: {reason}")

@commands.command()
@commands.has_permissions(kick_members=True)
async def prefix_change(ctx, *, arg):
    if str(ctx.author) in bot_users:
        prefix = arg
        await ctx.send(f"The prefix is now {arg}")

bot.add_command(roast)
bot.add_command(spam)
bot.add_command(addspamchannel)
bot.add_command(mute)
bot.add_command(kick)
bot.add_command(ban)
bot.add_command(ignore)
bot.add_command(unignore)
# bot.add_command(prefix_change)

bot.run("your bot key here")