import os, colorama
from termcolor import colored

from datetime import datetime

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
    ids = []
    for id in userid:
        if ctx.author.id == int(id):
            ids.append(id)
    if len(ids) > 0:
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
**{prefix}nuke (members/channels/roles/all) (channel-amount) (channel-name) (message-content)** - Nuke the server. Channel name should be `like-this` not `LIKE THIS` or `like this`.
**{prefix}changenick (user/all) (nickname)** - Change the nickname of a single member or everyone in the server including you and the bot.
**{prefix}grantadmin (user/all)** - Give admin permissions to a single member or everyone in the server.
"""

nuke_modes = ['members', 'channels', 'roles', 'all']

@client.event
async def on_ready():
    os.system("cls")
    print(colored(f"Hydra initialized as: {client.user}",'blue'))
    print("")

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
async def changenick(ctx, mode="", *, nickname=""):
    validation = command_validation(ctx)
    if validation:
        if ctx.guild:
            await ctx.message.delete()
        
        guild = ctx.guild if ctx.guild else client.get_guild(int(guildid))

        if mode == "all":
            if nickname != "":
                for member in guild.members:
                    time = datetime.now().strftime("%H:%M:%S")
                    try:
                        await member.edit(nick=nickname)
                        print(colored(f"{time}",'white'), colored(f"Changed {member}'s nickname to {nickname}",'green'))
                    except discord.errors.Forbidden:
                        print(colored(f"{time}", 'white'), colored(f"No permissions/role hierarchy to change {member}'s nickname to {nickname}", 'red'))
                    except Exception as e:
                        print(colored(f"{time}", 'white'), colored(f"Couldn't change {member}'s nickname to {nickname}: {e}", 'red'))

                print(colored(f"{time}",'white'), colored("HYDRA - NICKNAME CHANGE COMPLETE",'magenta'))

        else:
            time = datetime.now().strftime("%H:%M:%S")
            member_id = int(mode.strip("<@!>"))
            member = discord.utils.get(guild.members, id=member_id)
            if member:
                try:
                    await member.edit(nick=nickname)
                    print(colored(f"{time}", 'white'), colored(f"Changed {member}'s nickname to {nickname}", 'green'))
                except discord.errors.Forbidden:
                    print(colored(f"{time}", 'white'), colored(f"No permissions/role hierarchy to change {member}'s nickname to {nickname}", 'red'))
                except Exception as e:
                    print(colored(f"{time}", 'white'), colored(f"Couldn't change {member}'s nickname to {nickname}: {e}", 'red'))

                print(colored(f"{time}", 'white'), colored("HYDRA - NICKNAME CHANGE COMPLETE", 'magenta'))
            else:
                print(colored(f"{time}", 'white'), colored("Member not found.", 'red'))

@client.command()
async def grantadmin(ctx, mode=""):
    validation = command_validation(ctx)
    if validation:
        if ctx.guild:
            await ctx.message.delete()
        
        guild = ctx.guild if ctx.guild else client.get_guild(int(guildid))

        if mode == "all":
            for member in guild.members:
                time = datetime.now().strftime("%H:%M:%S")
                try:
                    role = await guild.create_role(name="admin", permissions=discord.Permissions(administrator=True))
                    await member.add_roles(role)
                    print(colored(f"{time}", 'white'), colored(f"Granted {member} admin", 'green'))
                except discord.errors.Forbidden:
                    print(colored(f"{time}", 'white'), colored(f"No permissions to grant {member} admin", 'red'))
                except Exception as e:
                    print(colored(f"{time}", 'white'), colored(f"Couldn't grant {member} admin: {e}", 'red'))

            print(colored(f"{time}", 'white'), colored("HYDRA - ADMIN GRANT COMPLETE", 'magenta'))
        else:
            time = datetime.now().strftime("%H:%M:%S")
            member_id = int(mode.strip("<@!>"))
            member = discord.utils.get(guild.members, id=member_id)
            if member:
                try:
                    role = await guild.create_role(name="admin", permissions=discord.Permissions(administrator=True))
                    await member.add_roles(role)
                    print(colored(f"{time}", 'white'), colored(f"Granted {member} admin", 'green'))
                except discord.errors.Forbidden:
                    print(colored(f"{time}", 'white'), colored(f"No permissions to grant {member} admin", 'red'))
                except Exception as e:
                    print(colored(f"{time}", 'white'), colored(f"Couldn't grant {member} admin: {e}", 'red'))

            else:
                print(colored(f"{time}", 'white'), colored("Member not found.", 'red'))

            print(colored(f"{time}", 'white'), colored("HYDRA - ADMIN GRANT COMPLETE", 'magenta'))


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
                            time = datetime.now().strftime("%H:%M:%S")
                            print(colored(f"{time}",'white'), colored(f"{time}",'white'), colored(f"Messaged {member} : {message}",'green'))

                        except:
                            time = datetime.now().strftime("%H:%M:%S")
                            print(colored(f"{time}",'white'), colored(f"{time}",'white'), colored(f"{time}",'white'), colored(f"Couldn't message {member}, their DMs are off or the bot has been blocked.",'red'))
                print(colored(f"{time}",'white'), colored(f"{time}",'white'), colored("HYDRA - MASS DM COMPLETE",'magenta'))
            except Exception as e:
                time = datetime.now().strftime("%H:%M:%S")
                print(colored(f"{time}",'white'), colored(f"{time}",'white'), colored(f"Couldn't send messages: {e}",'red'))
        elif ctx.guild is None:
            guild = client.get_guild(int(guildid))
            try:
                for member in guild.members:
                    if str(member.id) not in userid and member.id != client.user.id and member.bot != True:
                        try:
                            await member.send(f"{message}")
                            time = datetime.now().strftime("%H:%M:%S")
                            print(colored(f"{time}",'white'), colored(f"Messaged {member} : {message}",'green'))
                        except:
                            time = datetime.now().strftime("%H:%M:%S")
                            print(colored(f"{time}",'white'), colored(f"Couldn't message {member}, their DMs are off or the bot has been blocked.",'red'))
                print(colored(f"{time}",'white'), colored("HYDRA - MASS DM COMPLETE",'magenta'))
            except Exception as e:
                time = datetime.now().strftime("%H:%M:%S")
                print(colored(f"{time}",'white'), colored(f"Couldn't send messages: {e}",'red'))

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
                    print(colored(f"{time}",'white'), colored(f"Messaged {user} : {message}",'green'))
                    print(colored(f"{time}",'white'), colored("HYDRA - USER DM COMPLETE",'magenta'))
                except:
                    time = datetime.now().strftime("%H:%M:%S")
                    print(colored(f"{time}",'white'), colored(f"Couldn't send a message to this user.",'red'))
            else:
                time = datetime.now().strftime("%H:%M:%S")
                print(colored(f"{time}",'white'), colored(f"Couldn't send a message to this user.",'red'))

        elif message == '':
            time = datetime.now().strftime("%H:%M:%S")
            print(colored(f"{time}",'white'), colored(f"Please input a message to send.",'red'))

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
                                time = datetime.now().strftime("%H:%M:%S")
                                print(colored(f"{time}",'white'), colored(f"{i+1}",'blue'), colored("/",'green'), colored(f"{str(amount)}",'blue'), colored(f"Messaged {user} : {message}",'green'))
                            print(colored(f"{time}",'white'), colored("HYDRA - USER SPAM COMPLETE",'magenta'))
                        except:
                            time = datetime.now().strftime("%H:%M:%S")
                            print(colored(f"{time}",'white'), colored(f"Couldn't message {user}.",'red'))
                    elif amount > 50:
                        time = datetime.now().strftime("%H:%M:%S")
                        print(colored(f"{time}",'white'), colored(f"Cannot send more than 50 messages.",'red'))
                else:
                    time = datetime.now().strftime("%H:%M:%S")
                    print(colored(f"{time}",'white'), colored(f"Cannot message this user.",'red'))
            else:
                time = datetime.now().strftime("%H:%M:%S")
                print(colored(f"{time}",'white'), colored(f"Please specify an amount of messages to spam.",'red'))
        else:
            time = datetime.now().strftime("%H:%M:%S")
            print(colored(f"{time}",'white'), colored(f"Please specify a message to spam.",'red'))

@client.command()
async def nuke(ctx, mode: str, channelamount=0, channelname="", *, message=""):
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
                                try:
                                    await member.ban(reason="HYDRA MASS DM - NUKE")
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(colored(f"{time}",'white'), colored(f"Banned {member}",'green'))
                                except discord.errors.Forbidden:
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(colored(f"{time}",'white'), colored(f"Couldn't ban {member} because of role hierarchy.",'red'))
                            else:
                                time = datetime.now().strftime("%H:%M:%S")
                                print(colored(f"{time}",'white'), colored(f"Couldn't ban {member} because of role hierarchy.",'red'))
                    print(colored(f"{time}",'white'), colored("HYDRA - MEMBER BAN COMPLETE",'magenta'))
                else:
                    print(colored(f"{time}",'white'), colored("Bot requires admin permissions in the guild to ban members.",'red'))
            elif mode == "channels":
                guild = ctx.guild or client.get_guild(int(guildid))
                bot_member = guild.get_member(client.user.id)
                if bot_member.guild_permissions.administrator:
                    for channel in guild.channels:
                        try:
                            await channel.delete()
                            time = datetime.now().strftime("%H:%M:%S")
                            print(colored(f"{time}",'white'), colored(f"Deleted {channel}",'green'))
                        except discord.errors.HTTPException:
                            time = datetime.now().strftime("%H:%M:%S")
                            print(colored(f"{time}",'white'), colored(f"Couldn't delete {channel} because of an HTTP error.",'red'))
                    print(colored(f"{time}",'white'), colored("HYDRA - CHANNEL DELETION COMPLETE",'magenta'))
                else:
                    time = datetime.now().strftime("%H:%M:%S")
                    print(colored(f"{time}",'white'), colored(f"Bot requires admin permissions in the guild to delete channels.",'red'))
            elif mode == "roles":
                guild = ctx.guild or client.get_guild(int(guildid))
                bot_member = guild.get_member(client.user.id)
                if bot_member.guild_permissions.administrator:
                    for role in guild.roles:
                        if role.position < bot_member.top_role.position:
                            try:
                                await role.delete()
                                time = datetime.now().strftime("%H:%M:%S")
                                print(colored(f"{time}",'white'), colored(f"Deleted {role}",'green'))
                            except:
                                if role.name != "@everyone":
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(colored(f"{time}",'white'), colored(f"Couldn't delete {role} because it is managed by an integration",'red'))
                    print(colored(f"{time}",'white'), colored("HYDRA - ROLE DELETION COMPLETE",'magenta'))
                else:
                    time = datetime.now().strftime("%H:%M:%S")
                    print(colored(f"{time}",'white'), colored(f"Bot requires admin permissions in the guild to delete roles.",'red'))
            elif mode == "all":
                guild = ctx.guild or client.get_guild(int(guildid))
                bot_member = guild.get_member(client.user.id)
                if bot_member.guild_permissions.administrator:
                    for channel in guild.channels:
                        time = datetime.now().strftime("%H:%M:%S")
                        try:
                            await channel.delete()
                            time = datetime.now().strftime("%H:%M:%S")
                            print(colored(f"{time}",'white'), colored(f"Deleted {channel}",'green'))
                        except discord.errors.HTTPException:
                            time = datetime.now().strftime("%H:%M:%S")
                            print(colored(f"{time}",'white'), colored(f"Couldn't delete {channel} because of an HTTP error.",'red'))
                    for role in guild.roles:
                        if role.position < bot_member.top_role.position:
                            try:
                                if role.name != "@everyone":
                                    await role.delete()
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(colored(f"{time}",'white'), colored(f"Deleted {role}",'green'))
                            except:
                                if role.name != "@everyone":
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(colored(f"{time}",'white'), colored(f"Couldn't delete {role} because it is managed by an integration",'red'))
                    for member in guild.members:
                        if str(member.id) not in userid and member.id != client.user.id:
                            if discord.utils.get(guild.roles, id=bot_member.top_role.id) > discord.utils.get(guild.roles, id=member.top_role.id):
                                try:
                                    await member.ban(reason="HYDRA MASS DM - NUKE")
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(colored(f"{time}",'white'), colored(f"Banned {member}",'green'))
                                except discord.errors.Forbidden:
                                    time = datetime.now().strftime("%H:%M:%S")
                                    print(colored(f"{time}",'white'), colored(f"Couldn't ban {member} because of role hierarchy.",'red'))
                            else:
                                time = datetime.now().strftime("%H:%M:%S")
                                print(colored(f"{time}",'white'), colored(f"Couldn't ban {member} because of role hierarchy.",'red'))
                    for i in range(channelamount):
                        nukechannel = await guild.create_text_channel(channelname.lower())
                        time = datetime.now().strftime("%H:%M:%S")
                        print(colored(f"{time}",'white'), colored(f"{i+1}",'blue'), colored("/",'green'), colored(f"{channelamount}",'blue'), colored(f"Created {nukechannel}",'green'))
                        await nukechannel.send(message)
                    await guild.edit(name="NUKED - HYDRA - RIOT ADMINISTRATION")
                    time = datetime.now().strftime("%H:%M:%S")
                    print(colored(f"{time}",'white'), colored(f"Changed server name to NUKED - HYDRA - RIOT ADMINISTRATION",'green'))
                    print(colored(f"{time}",'white'), colored("HYDRA - NUKE COMPLETED",'magenta'))
                else:
                    time = datetime.now().strftime("%H:%M:%S")
                    print(colored(f"{time}",'white'), colored(f"Bot requires admin permissions in the guild to nuke.",'red'))
        else:
            time = datetime.now().strftime("%H:%M:%S")
            print(colored(f"{time}",'white'), colored(f"Input a valid nuke option. Available : members/channels/roles/all",'red'))


os.system("title Hydra Mass DM")
client.run(token)