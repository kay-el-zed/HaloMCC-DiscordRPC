# HaloMCC-DiscordRPC
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

A python script that grabs your XBL status for Halo MCC and shows it as a Discord rich presence status.

![preview image](https://i.imgur.com/6PtvoEy.png) ![image](https://user-images.githubusercontent.com/25113575/79253429-0e376080-7e38-11ea-859e-8833482ecd6a.png)

![image](https://user-images.githubusercontent.com/25113575/79253406-024b9e80-7e38-11ea-800f-2445d05d835e.png)

<h2>Requirements</h2>

* [pypresence](https://github.com/qwertyquerty/pypresence)
* A client ID for an application created in the [Discord developer portal](https://discordapp.com/developers) 
  * Sample images for 'cover' and 'win10' as shown above are provided for creating your own application.

<h2>How to use</h2>

1. Install both requirements using pip
2. Update discord_client_id with your valid application's client ID from the [Discord developer portal](https://discordapp.com/developers).  
3. Run [release](https://github.com/Gurrman375/HaloMCC-DiscordRPC/releases) . 
	
	 1. Input your xbox sign on account. (Data is stored in AppData/Local/OpenXbox/xbox)
 	2. Update discord_client_id with your valid application's client ID from the [Discord developer portal] and small Image and Large Image.
 	3. It will wait until it sees Halo MCC in your Xbox Live presence to display a rich status on Discord.

<h2>To-dos</h2>

* Add better checks for if the user is playing on either Xbox or PC.
* Clean up code.
* Add session timer tracking, i.e. How long a multiplayer session has run for
* Reduce debugging output.
* Possibly perform better detection for Halo MCC on PC by checking for processes(?)
