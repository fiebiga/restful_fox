import json

from mongoengine import NotUniqueError

from persistence_models import GameSummaryDocument

if __name__ == '__main__':
    print("Initializing resources...")
    with open("resources/game_summary.json", "r") as file:
        games = list(json.load(file))

    print("Found {length} resources to load. Loading data if it doesn't exist".format(length=len(games)))
    for game in games:
        game["game_id"] = game.pop("nfl_game_id")

    # The only way to insert while avoiding duplicate keys and skipping them
    for game in [GameSummaryDocument(**game) for game in games]:
        try:
            game.save()
        except NotUniqueError as error:
            pass


    print("Loading complete. {length} objects inserted".format(length=len(games)))
