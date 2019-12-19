# HaloMCC-DiscordRPC
A python script that grabs your XBL status for Halo MCC and shows it as a Discord rich presence status.


<h2>Requirements</h2>

* [pypresence](https://github.com/qwertyquerty/pypresence)
* [xbox-webapi](https://github.com/openxbox/xbox-webapi-python)

<h2>How to use</h2>

1. Install both requirements using pip
2. Run `xbox-authenticate` in cmd to create your token for connecting to XBL via xbox-webapi
3. Run the script. It will wait until you launch Halo MCC to display a status on Discord.

<h2>To-dos</h2>

* Add better checks for if the user is playing on either Xbox or PC.
* Clean up code.
* Add session timer tracking, i.e. How long a multiplayer session has run for
* Reduce debugging output.
* Possibly perform better detection for Halo MCC on PC by checking for processes(?)
