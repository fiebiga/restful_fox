import converters

from api_models import Game
from foxdemo.common.converters import convert
from persistence_models import GameDocument
from foxdemo.common.mongo_util import extract_query_modifiers, build_queryset


class GamesService(object):

    def get(self, **kwargs):
        modifiers, query_parameters = extract_query_modifiers(kwargs)
        object_filter = convert(Game(**query_parameters), GameDocument)
        query_set = build_queryset(GameDocument, model_filter_properties=object_filter.to_dict(), **modifiers)
        return [convert(game_document, Game) for game_document in query_set]

    def create(self, creation_model: Game):
        document = convert(Game(**creation_model.dict()), GameDocument)
        document.save()
        return convert(document, Game)

    def delete(self, **kwargs):
        object_filter = convert(Game(**kwargs), GameDocument)
        GameDocument.objects(**object_filter.to_dict()).delete()
