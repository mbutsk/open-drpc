import requests

STEAM_APP_LIST_URL = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"


def get_appid(game_name):
    response = requests.get(STEAM_APP_LIST_URL)
    if response.status_code != 200:
        return None

    app_list = response.json().get("applist", {}).get("apps", [])

    for app in app_list:
        if app["name"].lower() == game_name.lower():
            return app["appid"]

    return None


if __name__ == "__main__":
    game_name = input("Game name in Steam: ")
    app_id = get_appid(game_name)
    if app_id:
        print(f"{game_name} app id: {app_id}")
    else:
        print("Game not found")
