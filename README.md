# HaloMCC-DiscordRPC
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

A python script that grabs your XBL status for Halo MCC and shows it as a Discord rich presence status.

![image](https://user-images.githubusercontent.com/25113575/119899512-07629480-bef8-11eb-949b-cb5b6ad568d7.png)

![image](https://user-images.githubusercontent.com/25113575/119900126-ec445480-bef8-11eb-9f87-82e376668f27.png)

<h2>How to use</h2>

Running the Presence:
Run Step 1:
![image](https://user-images.githubusercontent.com/25113575/119243523-51c0cb80-bb1c-11eb-9369-6b0772a0156b.png)

Login and agree to the app getting your data:
![image](https://user-images.githubusercontent.com/25113575/119243543-8cc2ff00-bb1c-11eb-8b4e-e0762584d05e.png)

Copy the link you get:
![image](https://user-images.githubusercontent.com/25113575/119243561-bed46100-bb1c-11eb-8414-1cb560f79f0c.png)

Enter the link in the prompt (The links expire quickly):
![image](https://user-images.githubusercontent.com/25113575/119243702-2b9c2b00-bb1e-11eb-9ae8-eaee95f0a77b.png)

Launch the Rich Presence and enjoy:
![image](https://user-images.githubusercontent.com/25113575/119906785-bbb5e800-bf03-11eb-963a-1a74b833a724.png)

<h2>Requirements for Building</h2>

* [pypresence](https://github.com/qwertyquerty/pypresence)
* [xboxlive-api](https://github.com/XboxReplay/xboxlive-api)
* A client ID for an application created in the [Discord developer portal](https://discordapp.com/developers) 
* Sample images for 'cover' and 'win10' as shown above are provided for creating your own application.
* [pyinstaller](https://www.pyinstaller.org/downloads.html) for building the executable.
* [nodejs](https://nodejs.org/en/download/)
* [python](https://www.python.org/downloads/)


<h2>To-dos</h2>

* Add better checks for if the user is playing on either Xbox or PC.
* Clean up code.
* Add session timer tracking, i.e. How long a multiplayer session has run for
* Reduce debugging output.
* Possibly perform better detection for Halo MCC on PC by checking for processes(?)

<h2>Credits</h2>

<b>[pypresence](https://github.com/qwertyquerty/pypresence)</b> - Written by: [qwertyquerty](https://github.com/qwertyquerty) and [LewdNeko](https://github.com/lewdneko) Notable Contributors: [GiovanniMCMXCIX](https://github.com/GiovanniMCMXCIX), [GhostofGoes](https://github.com/GhostofGoes)

<b>[XboxReplay](https://github.com/XboxReplay)</b> - Written by: [Alexis ize](https://github.com/Alexis-Bize)

<b>[Gurrman375](https://github.com/Gurrman375)</b> - Major contributor to the repo. Most of the commits come from them.
