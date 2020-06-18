# HaloMCC-DiscordRPC
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

A python script that grabs your XBL status for Halo MCC and shows it as a Discord rich presence status.

![image](https://i.imgur.com/51Zdnv9l.png)

![image](https://user-images.githubusercontent.com/25113575/79253406-024b9e80-7e38-11ea-800f-2445d05d835e.png)

<h2>How to use</h2>

1. Install both requirements using pip
2. Update discord_client_id with your valid application's client ID from the [Discord developer portal](https://discordapp.com/developers).  

3. Run the latest [release](https://github.com/kay-el-zed/HaloMCC-DiscordRPC/releases). 

	
	1. Input your xbox sign on account. (Data is stored in AppData/Local/OpenXbox/xbox)
 	2. When prompted, enter your valid application's CID(client ID) from the [Discord developer portal](https://discord.com/developers/applications), along with a small and large image. (If you don't know how to do this, leave the option blank and default settings will be used.)
 	3. It will wait until it sees Halo MCC in your Xbox Live presence to display a rich status on Discord.

<h2>Requirements for Building</h2>

* [pypresence](https://github.com/qwertyquerty/pypresence)
* [xbox-webapi-python](https://github.com/openxbox/xbox-webapi-python)
* A client ID for an application created in the [Discord developer portal](https://discordapp.com/developers) 
* Sample images for 'cover' and 'win10' as shown above are provided for creating your own application.
* [pyinstaller](https://www.pyinstaller.org/downloads.html) for building the executable.


<h2>To-dos</h2>

* Add better checks for if the user is playing on either Xbox or PC.
* Clean up code.
* Add session timer tracking, i.e. How long a multiplayer session has run for
* Reduce debugging output.
* Possibly perform better detection for Halo MCC on PC by checking for processes(?)

<h2>Credits</h2>

<b>[pypresence](https://github.com/qwertyquerty/pypresence)</b> - Written by: [qwertyquerty](https://github.com/qwertyquerty) and [LewdNeko](https://github.com/lewdneko) Notable Contributors: [GiovanniMCMXCIX](https://github.com/GiovanniMCMXCIX), [GhostofGoes](https://github.com/GhostofGoes)

<b>[xbox-webapi-python](https://github.com/openxbox/xbox-webapi-python)</b> - uses parts of [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template. The authentication code is based on [joealcorn/xbox](https://github.com/joealcorn/xbox)

<b>[Gurrman375](https://github.com/Gurrman375)</b> - Major contributor to the repo. Most of the commits come from them.
