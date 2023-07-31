import os,time,shutil

try:
    import colorama
    from termcolor import colored
except:
    os.system("pip install -r requirements.txt")
    import colorama
    from termcolor import colored

colorama.init()

def cls():
    os.system("cls")

def pause():
    os.system("pause")

class InitiateBot:
    def __init__(self, token, prefix, userid, guildid):
        self.token = str(token)
        self.prefix = str(prefix)
        self.userid = userid
        self.guildid = str(guildid)
    def setup(self):
        if os.path.exists("modules\start.py"):
            os.remove("modules\start.py")
        shutil.copyfile("modules\sample.py", "modules\start.py")

        with open("modules\whitelists.txt", "w") as file:
            for id in self.userid:
                file.write(f"{id}\n")

        with open("modules\start.py", "r") as file:
            content = file.read()

        new_content = content.replace("{bottoken}", self.token)
        new_content = new_content.replace("{cmdprefix}", self.prefix)
        new_content = new_content.replace("{gid}", self.guildid)

        with open("modules\start.py", "w") as file:
            file.write(new_content)

        with open("start_bot.bat","w+") as file:
            file.write("""cls
python modules\start.py
""")
        cls()
        print(colored("""A file "start_bot.bat" has been created. Whenever you want to launch the bot, open that. If you want to reconfigure your bot, run "build_bot.bat". Do not change those files whatsoever, they are crucial.""",'green'))
        print("")
        pause()
        cls()
        try:
            print(colored("Starting Hydra...",'green'))
            os.system("python modules\start.py")
        except Exception as e:
            print(colored(f"Error trying to run bot: {e}",'red'))
            pause()
            main()
            


def main():
    cls()
    os.system("title Hydra Mass DM Bot by RIOT Administration")
    print(colored("WARNING: Enable all 3 privileged gateway intents on the bot's page.",'red'))
    print(colored("WARNING: Turn on developer mode from SETTINGS > Advanced > Developer mode",'red'))
    print(colored("WARNING: Ensure the bot is invited in the server you are mass DMing members from.",'red'))
    print("")
    pause()
    cls()
    print(colored("  ___ ___            .___              ",'green'))
    print(colored(" /   |   \ ___.__. __| _/___________   ",'green'))
    print(colored("/    ~    <   |  |/ __ |\_  __ \__  \  ",'green'))
    print(colored("\    Y    /\___  / /_/ | |  | \// __ \_",'green'))
    print(colored(" \___|_  / / ____\____ | |__|  (____  /",'green'))
    print(colored("       \/  \/         \/            \/ ",'green'))
    print("")
    print("")
    prefix = input(colored("What prefix would you like for the bot? => ",'blue'))
    print("")
    token = input(colored("Bot token => ",'blue'))
    print("")
    userid = input(colored("User IDs of the whitelisted people (separate by comma) => ",'blue'))
    whitelists = userid.split(",")
    whitelists = [whitelist.strip() for whitelist in whitelists]
    print("")
    guildid = input(colored("What is the ID of the guild you want to spam? => ",'blue'))
    print("")
    cls()
    print(colored(f"""
Bot token: {token}
Bot prefix: {prefix}
Your user ID: {userid}
Default guild ID: {guildid}
""",'green'))
    print("")
    choice = input(colored("Is this correct? (Y/N) => ",'blue'))
    if choice.lower() == "n":
        cls()
        print(colored("You have invalidated your setup, program restarting...",'red'))
        for i in range(3):
            print(f"{3-i}")
            time.sleep(1)
        main()
    cls()
    print(colored("Initiating bot, please wait.",'green'))
    botinit = InitiateBot(token=token, prefix=prefix, userid=whitelists, guildid=guildid)
    botinit.setup()

if __name__ == '__main__':
    main()