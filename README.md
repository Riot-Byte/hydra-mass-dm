<p align='center'><img src="https://user-images.githubusercontent.com/71534600/255708800-55bf5018-e8f7-4af3-9829-faa9acdf153c.png" width=500 /></p>

# Hydra Mass DM
> A mass DM discord bot which you can use to mass DM, single DM, spam an user, or nuke the server.

Support server : [https://discord.gg/R5ab7AXpJu](https://discord.gg/4TyqkDXtBa)

## Disclaimer
This tool was made for educational purposes only and self learning. The developer is not responsible for bad actions that originate from this tool. Publishing this tool under your name will result in a DMCA takedown. You can distribute copies of it, but just don't change the code as if it was your own.

## Features
- Mass DM
- DM a single user
- Spam a single user
- Nuke the server
- Grant admin to users
- Change nickname of users

## Installation

You can download this as zip, or the tool can be installed following those steps:

Create a new folder anywhere you'd like, then open a command prompt or powershell inside of it. Then [install git](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line) if you don't already have it.

Then type this command:

```git clone https://github.com/Riot-Byte/hydra-mass-dm.git```

Now do `cd hydra-mass-dm`

After doing all the steps above, you can now run `build_bot.bat`

1. **Warnings**

![image](https://github.com/Riot-Byte/hydra-mass-dm/assets/71534600/94ba199e-0fc3-47da-835a-ffa60f5c0aa0)

When you have checked all of these 3 warnings, continue.

2. **Setup**

Now you will need to get the prefix of the bot, for example something simpler like `!` or `.` could work, but it is personal preference.
Then, you will need the bot token. For this, go to https://discord.com/developers/ and create a new application. After that, go to "Bot" and build a bot. Copy its token after that, then insert it in the console.

![image](https://github.com/Riot-Byte/hydra-mass-dm/assets/71534600/5f038701-666d-41a5-8d13-c1ee44ed671e)

Also ensure that your privileged gateway intents are all enabled ^

You will then need the user ID of everyone you want to allow using your mass DM bot.

![image](https://github.com/Riot-Byte/hydra-mass-dm/assets/71534600/50ae851a-9f21-4e1f-928f-99003308bd0e)

Go to Settings > Advanced > Turn on Developer Mode. Then, copy the user IDs of everyone you want to whitelist and separate it by a comma, like 1,2,3. If you only want yourself to use the bot, only put your user ID.

Now for the guild ID, you will need to go to the default/main guild you want to spam, right click it, and Copy Server ID. Then put it in the console. (the bot will be using that guild by default when you DM it)

Then you can confirm the build. Type `help` for a list of available commands, with your specified prefix, for example `%help`.
