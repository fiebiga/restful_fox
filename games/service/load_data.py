import json

from mongoengine import NotUniqueError

from persistence_models import GameDocument

if __name__ == '__main__':
    print("Initializing resources...")
    with open("resources/games.json", "r") as file:
        games = list(json.load(file))

    print("Found {length} resources to load. Loading data if it doesn't exist".format(length=len(games)))
    for game in games:
        game["game_id"] = game.pop("id")

    unique_games = {}
    for game in games:
        unique_games[game["game_id"]] = unique_games.get("game_id", game)

    # The only way to insert while avoiding duplicate keys and skipping them
    for game in [GameDocument(**game) for game in unique_games.values()]:
        try:
            game.save()
        except NotUniqueError as error:
            pass
    print("Loading complete. {length} objects inserted".format(length=len(unique_games)))
