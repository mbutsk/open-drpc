# Open DRPC v1.2.0

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

Add excluded app ids to `excluded` field
