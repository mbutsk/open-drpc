# Open DRPC v1.5.0

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

Python Script for adding Discord Rich Presence support to all Steam Games on Linux and MacOS

![Screenshot](https://github.com/user-attachments/assets/2caece22-8669-40e6-a92f-6a53a2b6f63f)

## Installation

First, clone the repo:

```shell
git clone https://github.com/mbutsk/open-drpc
```

> [!IMPORTANT]
> Don't run the script as superuser (sudo)
>
> For Linux make sure you have systemd installed

Then, run `install-linux.sh` or `install-macos.sh`

## Uninstallation

> [!IMPORTANT]
> Don't run the script as superuser (sudo)
>
> For Linux make sure you have systemd installed

To uninstall, run `install-linux.sh` or `install-macos.sh`

## Restarting

You can restart open-drpc for reload mods / config

### Linux

```shell
systemctl --user restart "open-drpc"
```

### MacOS

```shell
launchctl stop "open-drpc"
launchctl start "open-drpc"
```

## Configuration

The configuration file is located at `~/.config/open-drpc.json` on Linux and at `~/Library/Application Support/open-drpc/config.json` on MacOS

### Excluded

You can add excluded app IDs to the `excluded` list.

Excluded games will not show up on your profile.

### Custom

To change any game's data to your own, you can add entries to the `custom` object with app IDs as keys and replacement data as values.

You can change the `name`, `description`, or the `image` (to a URL to any image).

For example:

```json
{
"custom": {
    "442070": {
        "name": "Draw!!",
        "description": "Very good game"
    }
}
```

Note that by default the description of a game will appear as the list of its developers.

### Mods

You can add mod names to the `mods` list. Read more in [Modding](https://github.com/mbutsk/open-drpc/blob/main/README.md#modding)

### Modding

### Mod installation

In a folder with open-drpc installed, create a `mods` folder. You can put mod folders into it.

The mod name is the name of the mod folder.

Add the mods you have installed to the `mods` list in config to enable them.

### Mod creation

Please use this badge in your mod repository README file:

[![open-drpc mod](https://img.shields.io/badge/OPEN%20DRPC-MOD-blue?style=for-the-badge&logo=discord&logoColor=white)](https://github.com/mbutsk/open-drpc)

```markdown
[![open-drpc mod](https://img.shields.io/badge/OPEN%20DRPC-MOD-blue?style=for-the-badge&logo=discord&logoColor=white)](https://github.com/mbutsk/open-drpc)
```

In the mod folder (`open-drpc/mods/mod-name`), create a `main.py` file. It must contain two functions: `setup` and `game_data`

#### `setup`

In here you may put any actions that will be performed when importing the module.

It must return a list of Steam app IDs, upon receiving which open-drpc will call the `game_data` function.

#### `game_data`

This function must accept an argument - a `dict` with the game data received from Steam Web API

It must return the same object with updated information of the game, like the name or links.

You can also change the `image` and `description` in the object to change the image and description of the RPC respectively.

## Trusted mods

You can request the addition of your mod to the Trusted mods list by submitting a new [issue](https://github.com/mbutsk/open-drpc/issues/new?labels=Mod). Your repo name must start with `open-drpc-`

[Undertale mod](https://github.com/mbutsk/open-drpc-undertale)
