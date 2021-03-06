# HaloMCC-DiscordRPC
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

A python script that grabs your XBL status for Halo MCC and shows it as a Discord rich presence status.

![image](https://i.imgur.com/51Zdnv9l.png) ![image](https://user-images.githubusercontent.com/6400909/85205705-5f117c80-b2f3-11ea-9ede-8af1440e23ca.png)

![image](https://user-images.githubusercontent.com/6400909/85205654-11950f80-b2f3-11ea-8e71-2398b34e2ccb.png)

<h2>How to use</h2>

1. Launch the latest release executable. 
2. Create a token (option 1) for Xbox Live. You will be prompted for your credentials to authenticate your account.
3. Launch the rich presense (option 2). If you would like to use your own discord developer app and use your own images, you can do so here. 
4. It will wait until it sees Halo MCC in your Xbox Live presence to display a rich status on Discord. 

<h2>Requirements for Building</h2>

* [pypresence](https://github.com/qwertyquerty/pypresence)
* [xbox-webapi-python](https://github.com/openxbox/xbox-webapi-python)
* A client ID for an application created in the [Discord developer portal](https://discordapp.com/developers) 
* Sample images for 'cover' and 'win10' as shown above are provided for creating your own application.
* [pyinstaller](https://www.pyinstaller.org/downloads.html) for building the executable.


<h2>To-dos</h2>

All things that we'd like to work on can be found in [this issue](https://github.com/kay-el-zed/HaloMCC-DiscordRPC/issues/5)

<h2>Credits</h2>

<b>[pypresence](https://github.com/qwertyquerty/pypresence)</b> - Written by: [qwertyquerty](https://github.com/qwertyquerty) and [LewdNeko](https://github.com/lewdneko) Notable Contributors: [GiovanniMCMXCIX](https://github.com/GiovanniMCMXCIX), [GhostofGoes](https://github.com/GhostofGoes)

<b>[xbox-webapi-python](https://github.com/openxbox/xbox-webapi-python)</b> - uses parts of [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template. The authentication code is based on [joealcorn/xbox](https://github.com/joealcorn/xbox)

<b>[Gurrman375](https://github.com/Gurrman375)</b> - Major contributor to the repo. Most of the commits come from them.
