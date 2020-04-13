# HaloMCC-DiscordRPC
A python script that grabs your XBL status for Halo MCC and shows it as a Discord rich presence status.

![preview image](https://i.imgur.com/6PtvoEy.png)

<h2>Requirements</h2>

* [pypresence](https://github.com/qwertyquerty/pypresence)
* [xbox-webapi](https://github.com/openxbox/xbox-webapi-python)
* A client ID for an application created in the [Discord developer portal](https://discordapp.com/developers) 
  * Sample images for 'cover' and 'win10' as shown above are provided for creating your own application.

<h2>How to use</h2>

1. Install both requirements using pip
2. Run `xbox-authenticate` in cmd to create your token for connecting to XBL via xbox-webapi
3. Update discord_client_id with your valid application's client ID from the [Discord developer portal](https://discordapp.com/developers).  
4. Run the script. It will wait until it sees Halo MCC in your Xbox Live presence to display a rich status on Discord.

<h2>To-dos</h2>

* Add better checks for if the user is playing on either Xbox or PC.
* Clean up code.
* Add session timer tracking, i.e. How long a multiplayer session has run for
* Reduce debugging output.
* Possibly perform better detection for Halo MCC on PC by checking for processes(?)
