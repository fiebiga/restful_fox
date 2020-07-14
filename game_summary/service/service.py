import converters

from api_models import GameSummary
from foxdemo.common.converters import convert
from persistence_models import GameSummaryDocument
from foxdemo.common.mongo_util import extract_query_modifiers, build_queryset


class GameSummaryService(object):

    def get(self, **kwargs):
        modifiers, query_parameters = extract_query_modifiers(kwargs)
        object_filter = convert(GameSummary(**query_parameters), GameSummaryDocument)
        query_set = build_queryset(GameSummaryDocument, model_filter_properties=object_filter.to_dict(), **modifiers)
        return [convert(game_document, GameSummary) for game_document in query_set]

    def create(self, creation_model: GameSummary):
        document = convert(GameSummary(**creation_model.dict()), GameSummaryDocument)
        document.save()
        return convert(document, GameSummary)

    def delete(self, **kwargs):
        object_filter = convert(GameSummary(**kwargs), GameSummaryDocument)
        GameSummaryDocument.objects(**object_filter.to_dict()).delete()
