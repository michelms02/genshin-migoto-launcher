import os

def main():
    if (launching_migoto()):
        launch_migoto()
    
    launch_genshin_impact()

def launching_migoto():
    launch = ""

    while(launch.lower() not in ["y", "n", "yes", "no"]):
        launch = input("Would you like to launch Genshin Impact with 3DMigoto? Y/N (Default: Y)\n")

        if (launch == ""):
            break

    return launch == "" or launch.casefold() == "y" or launch.casefold() == "yes"

def launch_migoto():
    migoto_path = "C:\\Path\\to\\3DMigoto Loader.exe"

    # Set working directory to 3DMigoto's path in order to load .ini and .dll files
    os.chdir(migoto_path.replace("\\3DMigoto Loader.exe", ""))

    # Launch 3DMigoto
    os.startfile(migoto_path)

def launch_genshin_impact():
    # Launch Genshin Impact (non-steam added game)
    # os.system("start steam://rungameid/123456789")

    # Launch Genshin Impact (non-steam)
    print("You may keep this window open for a steam in-game status. \nThis window will automatically close when Genshin Impact is exited. \nGenshin Impact is now running.")
    genshin_path = "C:\\Path\\to\\GenshinImpact.exe"
    genshin_args = "-popupwindow -screen-height 1080 -screen-width 1920"
    
    os.system('"' + genshin_path + '"' + " " + genshin_args)

if __name__ == "__main__":
    main()
