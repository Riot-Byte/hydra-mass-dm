import os, colorama
from termcolor import colored

colorama.init()

try:
    import discord
    from discord.ext import commands
except:
    os.system("python -m pip install discord")
    import discord
    from discord.ext import commands

token = "{bottoken}"
prefix = "{cmdprefix}"
guildid = "{gid}"
userid = []
with open('modules\whitelists.txt', 'r') as file:
    for line in file:
        userid.append(line.strip())


client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
client.remove_command("help")


def command_validation(ctx):
    for id in userid:
        if ctx.author.id == int(id):
            return True
        else:
            return False

help_menu = f"""
Available commands for the Hydra Mass DM bot :

**{prefix}help** - Show this message.

:green_circle: Activations

**{prefix}massdm (message)** - Send a single message DM to everyone in the server.
**{prefix}dm (user) (message)** - Send a single message to a specific user.
**{prefix}spamuser (user) (amount) (message)** - Spam a specific user.
**{prefix}nuke (members/channels/roles/all)** - Nuke the server.
"""

nuke_modes = ['members', 'channels', 'roles', 'all']

@client.event
async def on_ready():
    os.system("cls")
    print(colored(f"Hydra initialized as: {client.user}",'blue'))
    print("")

# funcs

# commands

@client.command()
async def help(ctx):
    validation = command_validation(ctx)
    if validation:
        print(colored("HYDRA - HELP MENU RECEIVED",'magenta'))
        if ctx.guild:
            await ctx.message.delete()
        try:
            await ctx.author.send(help_menu)
        except:
            await ctx.send(help_menu)

@client.command()
async def massdm(ctx, *, message: str):
    validation = command_validation(ctx)
    if validation:
        if ctx.guild:
            await ctx.message.delete()
        if ctx.guild is not None:
            try:
                for member in ctx.guild.members:
                    if str(member.id) not in userid and member.id != client.user.id and member.bot != True:
                        try:
                            await member.send(f"{message}")
                            print(colored(f"Messaged {member} : {message}",'green'))
                        except:
                            print(colored(f"Couldn't message {member}, their DMs are off or the bot has been blocked.",'red'))
                print(colored("HYDRA - MASS DM COMPLETE",'magenta'))
            except Exception as e:
                print(colored(f"Couldn't send messages: {e}",'red'))
        elif ctx.guild is None:
            guild = client.get_guild(int(guildid))
            try:
                for member in guild.members:
                    if str(member.id) not in userid and member.id != client.user.id and member.bot != True:
                        try:
                            await member.send(f"{message}")
                            print(colored(f"Messaged {member} : {message}",'green'))
                        except:
                            print(colored(f"Couldn't message {member}, their DMs are off or the bot has been blocked.",'red'))
                print(colored("HYDRA - MASS DM COMPLETE",'magenta'))
            except Exception as e:
                print(colored(f"Couldn't send messages: {e}",'red'))

@client.command()
async def dm(ctx, user: discord.Member, *, message: str):
    validation = command_validation(ctx)
    if validation:
        if ctx.guild:
            await ctx.message.delete()
        if message != '':
            if str(user.id) not in userid and user.id != client.user.id and user.bot != True:
                try:
                    await user.send(f"{message}")
                    print(colored(f"Messaged {user} : {message}",'green'))
                    print(colored("HYDRA - USER DM COMPLETE",'magenta'))
                except:
                    print(colored("Couldn't send a message to this user.",'red'))
            else:
                print(colored("Couldn't send a message to this user.",'red'))

        elif message == '':
            print(colored("Please input a message to send.",'red'))

@client.command()
async def spamuser(ctx, user: discord.Member, amount: int, *, message: str):
    validation = command_validation(ctx)
    if validation:
        if ctx.guild:
            await ctx.message.delete()
        if message != '':
            if amount:
                if str(user.id) not in userid and user.id != client.user.id and user.bot != True:
                    if amount < 50:
                        try:
                            for i in range(amount):
                                await user.send(message)
                                print(colored(f"[{i+1}] Messaged {user} : {message}",'green'))
                            print(colored("HYDRA - USER SPAM COMPLETE",'magenta'))
                        except:
                            print(colored(f"Couldn't message {user}.",'red'))
                    elif amount > 50:
                        print(colored("Cannot send more than 50 messages.",'red'))
                else:
                    print(colored("Cannot message this user.",'red'))
            else:
                print(colored("Please specify an amount of messages to spam.",'red'))
        else:
            print(colored("Please specify a message to spam.",'red'))

@client.command()
async def nuke(ctx, mode: str):
    validation = command_validation(ctx)
    if validation:
        if ctx.guild:
            await ctx.message.delete()
        if mode in nuke_modes:
            if mode == "members":
                guild = ctx.guild or client.get_guild(int(guildid))
                bot_member = guild.get_member(client.user.id)
                if bot_member.guild_permissions.administrator:
                    for member in guild.members:
                        if str(member.id) not in userid and member.id != client.user.id:
                            if discord.utils.get(guild.roles, id=bot_member.top_role.id) > discord.utils.get(guild.roles, id=member.top_role.id):
                                await member.ban(reason="HYDRA MASS DM - NUKE")
                                print(colored(f"Banned {member}",'green'))
                            else:
                                print(colored(f"Couldn't ban {member} because of role hierarchy.",'red'))
                    print(colored("HYDRA - MEMBER BAN COMPLETE",'magenta'))
                else:
                    print(colored("Bot requires admin permissions in the guild to ban members.",'red'))
            elif mode == "channels":
                guild = ctx.guild or client.get_guild(int(guildid))
                bot_member = guild.get_member(client.user.id)
                if bot_member.guild_permissions.administrator:
                    for channel in guild.channels:
                        await channel.delete()
                        print(colored(f"Deleted {channel}",'green'))
                    print(colored("HYDRA - CHANNEL DELETION COMPLETE",'magenta'))
                else:
                    print(colored("Bot requires admin permissions in the guild to delete channels.",'red'))
            elif mode == "roles":
                guild = ctx.guild or client.get_guild(int(guildid))
                bot_member = guild.get_member(client.user.id)
                if bot_member.guild_permissions.administrator:
                    for role in guild.roles:
                        if role.position < bot_member.top_role.position:
                            try:
                                await role.delete()
                                print(colored(f"Deleted {role}",'green'))
                            except:
                                if role.name != "@everyone":
                                    print(colored(f"Couldn't delete {role} because it is managed by an integration",'red'))
                    print(colored("HYDRA - ROLE DELETION COMPLETE",'magenta'))
                else:
                    print(colored("Bot requires admin permissions in the guild to delete roles.",'red'))
            elif mode == "all":
                guild = ctx.guild or client.get_guild(int(guildid))
                bot_member = guild.get_member(client.user.id)
                if bot_member.guild_permissions.administrator:
                    for channel in guild.channels:
                        await channel.delete()
                        print(colored(f"Deleted {channel}",'green'))
                    for role in guild.roles:
                        if role.position < bot_member.top_role.position:
                            try:
                                await role.delete()
                                print(colored(f"Deleted {role}",'green'))
                            except:
                                if role.name != "@everyone":
                                    print(colored(f"Couldn't delete {role} because it is managed by an integration",'red'))
                    for member in guild.members:
                        if str(member.id) not in userid and member.id != client.user.id:
                            if discord.utils.get(guild.roles, id=bot_member.top_role.id) > discord.utils.get(guild.roles, id=member.top_role.id):
                                await member.ban(reason="HYDRA MASS DM - NUKE")
                                print(colored(f"Banned {member}",'green'))
                            else:
                                print(colored(f"Couldn't ban {member} because of role hierarchy.",'red'))
                    print(colored("HYDRA - NUKE COMPLETED",'magenta'))
                else:
                    print(colored("Bot requires admin permissions in the guild to nuke.",'red'))
        else:
            print(colored("Input a valid nuke option. Available : members/channels/roles/all",'red'))


os.system("title Hydra Mass DM")
client.run(token)