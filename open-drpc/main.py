import psutil
import requests
from pypresence import Presence
from pypresence.exceptions import DiscordNotFound
from time import sleep

RPC = Presence(1372662863755218944)


def connect_rpc():
    while True:
        try:
            RPC.connect()
            break
        except DiscordNotFound:
            sleep(5)
            connect_rpc()


connect_rpc()


def game_data(app_id):
    response = requests.get(
        "https://store.steampowered.com/api/appdetails", {"appids": app_id})
    data = response.json()[str(app_id)]["data"]

    return data


def get_game():
    for proc in psutil.process_iter(["environ"]):
        try:
            environ = proc.info["environ"]
            if environ is not None:
                if "SteamAppId" in environ:
                    return game_data(environ["SteamAppId"])
        except (psutil.AccessDenied, psutil.NoSuchProcess, KeyError):
            continue
    return None


def create(game: dict):
    RPC.update(details=game["name"], state=', '.join(game['developers']), large_image=game['header_image'], large_text=game['name'],
               small_image='https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/2048px-Steam_icon_logo.svg.png',
               small_text='Using Open DRPC', buttons=[{'label': "View on Steam", 'url': f"https://store.steampowered.com/app/{game['steam_appid']}"}])
    in_game()


def in_game():
    while True:
        if not get_game():
            RPC.clear()
            wait()
        else:
            sleep(15)


def wait():
    while True:
        game = get_game()
        if game:
            create(game)
        sleep(15)


if __name__ == "__main__":
    game = get_game()
    if game:
        create(game)
    else:
        wait()
