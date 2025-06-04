# Open DRPC v1.4.1

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

Python Script adding Discord RPC support to all Steam Games on Linux

![Screenshot](https://github.com/user-attachments/assets/2caece22-8669-40e6-a92f-6a53a2b6f63f)

## Installation

First, clone the repo:

```bash
git clone https://github.com/mbutsk/open-drpc
```

> [!IMPORTANT]
> Don't run the script as superuser (sudo) and make sure you have systemd installed

Then, run the `install.sh`:

```bash
run install.sh
```

## Configuration

The configuration file is at `~/.config/open-drpc.json`

### Excluded

Add excluded app ids to `excluded` list

### Custom

In the custom field, add dictionaries. The keys in them are Steam app ids. You can change the data for a specific game. For example:
You can also change the game description. By default, this is the developer list

```json
{
"custom": {
    "442070": {
        "name": "Draw!!",
        "description": "Very good game"
    }
}
```

### Mods

Add mods names to `mods` list. Detailed in [Modding](https://github.com/mbutsk/open-drpc/blob/main/README.md#modding)

## Uninstallation

> [!IMPORTANT]
> Don't run the script as superuser (sudo) and make sure you have systemd installed

Then, run the `uninstall.sh`:

```bash
run uninstall.sh
```

### Modding

### Mods installation

In the folder with open-drpc installed, create a `mods` folder. You can clone folders with mods into it. Mod name = folder name

Then add mod name to `mods` list in `~/.config/open-drpc.json`

### Create mod

In the mod folder (open-drpc/mods/mod-name), create a main.py file. It must contain two functions: `setup` and `game_data`

#### `setup`

Actions performed when importing the module. Should return a list of Steam app ids, upon receipt of which the `game_data` function will be called.

### `game_data`

Argument: `game: dict` (Dictionary with game data received from Steam Web API by game id)

The function should return updated information about the game. You can also use `header_image` as the main image in RPC and `description` as state in RPC

### Requirements

Your repo name should start with "open-drpc-"

Please use this badge in your repository README file

[![open-drpc mod](https://img.shields.io/badge/OPEN%20DRPC-MOD-blue?style=for-the-badge&logo=discord&logoColor=white)](https://github.com/mbutsk/open-drpc)

```markdown
[![open-drpc mod](https://img.shields.io/badge/OPEN%20DRPC-MOD-blue?style=for-the-badge&logo=discord&logoColor=white)](https://github.com/mbutsk/open-drpc)
```

## Trusted mods

You can add your mod to Trusted mod by [Issue](https://github.com/mbutsk/open-drpc/issues/new?labels=Mod)

[Undertale mod](https://github.com/mbutsk/open-drpc-undertale)
