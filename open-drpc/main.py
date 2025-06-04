import psutil
import requests
from pypresence import Presence
from pypresence.exceptions import DiscordNotFound, PipeClosed
from time import sleep, time
import platform
import pathlib
import json
import importlib
import sys

if platform.system() != "Linux":
    print("Sorry, but the script only works on Linux")
    exit(1)

RPC = Presence(1372662863755218944)

mods = {}

def connect_rpc():
    while True:
        try:
            RPC.connect()
            break
        except DiscordNotFound:
            sleep(5)
            connect_rpc()

connect_rpc()

config_path = pathlib.Path("~/.config/open-drpc.json").expanduser()

if not config_path.exists():
    with config_path.open('w') as fp:
        config = {'excluded': [], 'custom': {}, 'mods': []}
        json.dump(config, fp)
else:
    with config_path.open('r+') as fp:
        try:
            config = json.load(fp)
            config['excluded'] = [str(i) for i in config['excluded']]
        except json.JSONDecodeError:
            config = {'excluded': [], 'custom': {}, 'mods': []}
            json.dump(config, fp)

sys.path.append(str(pathlib.Path(__file__).parent.parent))
for mod in config['mods']:
    try:
        module = importlib.import_module(f"mods.{mod}.main")
        mods.update({module: [str(i) for i in module.setup()]})
    except ModuleNotFoundError:
        pass

def game_data(app_id):
    app_id = str(app_id)
    response = requests.get(
        "https://store.steampowered.com/api/appdetails", {"appids": app_id})
    data = response.json()[app_id]["data"]

    if config['custom'].get(app_id):
        for k, v in config['custom'][app_id].items():
            if k == "image":
                data["header_image"] = v
            else:
                data[k] = v

    for mod, ids in mods.items():
        if app_id in ids:
            return mod.game_data(data)

    if not data.get('description'):
        data['description'] = 'by ' + ', '.join(data['developers'])

    return data


def get_game():
    for proc in psutil.process_iter(["environ"]):
        try:
            environ = proc.info["environ"]
            if environ is not None:
                if "SteamAppId" in environ and environ["SteamAppId"] not in config['excluded']:
                    return game_data(environ["SteamAppId"])
        except (psutil.AccessDenied, psutil.NoSuchProcess, KeyError):
            continue
    return None

def rpc_gen(game: dict):
    buttons = [{'label': "View on Steam", 'url': f"https://store.steampowered.com/app/{game['steam_appid']}"}]
                
    if game.get('website'):
        buttons.append({'label': f"{game['name']} website", 'url': game['website']})

    return {'details': game["name"], 'state': game['description'], 'large_image': game['header_image'], 'large_text': game['name'],
    'small_image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/2048px-Steam_icon_logo.svg.png',
    'small_text': 'Using Open DRPC', 'buttons': buttons}

def create(game: dict):
    try:
        RPC.update(**rpc_gen(game))
        in_game()
    except PipeClosed:
        connect_rpc()


def in_game():
    tm = time()
    while True:
        game = get_game()
        if not game:
            RPC.clear()
            wait()
        else:
            RPC.update(start=tm, **rpc_gen(game))
            sleep(15)


def wait():
    while True:
        sleep(15)
        game = get_game()
        if game:
            create(game)


if __name__ == "__main__":
    game = get_game()
    if game:
        create(game)
    else:
        wait()
