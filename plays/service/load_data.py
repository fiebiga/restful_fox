import glob
import json

from mongoengine import NotUniqueError

from persistence_models import PlayDocument

if __name__ == '__main__':
    print("Initializing data...")
    plays = []

    # This is an expensive operation
    if PlayDocument.objects.count() == 0:
        for file in glob.glob("resources/plays_*.json"):
            with open(file, "r") as file:
                plays.extend(list(json.load(file)))

        print("Found {length} resources to load. Loading data if it doesn't exist".format(length=len(plays)))

        for play in plays:
            play["game_id"] = play.pop("nfl_id")

        unique_plays = {}
        for play in plays:
            key = "{game_id}{play_id}".format(game_id=play["game_id"], play_id=play["play_id"])
            unique_plays[key] = unique_plays.get(key, play)
        for play in unique_plays.values():
            try:
                PlayDocument(**play).save()
            except NotUniqueError:
                # Expected. Key collision due to duplicate entries
                pass

        print("Loading complete. {length} objects inserted".format(length=len(unique_plays)))
    else:
        print("Skipping initialization, loading already exists")
