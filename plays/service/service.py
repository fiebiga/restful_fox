import converters

from api_models import Play
from foxdemo.common.converters import convert
from persistence_models import PlayDocument
from foxdemo.common.mongo_util import extract_query_modifiers, build_queryset


class PlaysService(object):

    def get(self, **kwargs):
        modifiers, query_parameters = extract_query_modifiers(kwargs)
        object_filter = convert(Play(**query_parameters), PlayDocument)
        query_set = build_queryset(PlayDocument, model_filter_properties=object_filter.to_dict(), **modifiers)
        return [convert(game_document, Play) for game_document in query_set]

    def create(self, creation_model: Play):
        document = convert(Play(**creation_model.dict()), PlayDocument)
        document.save()
        return convert(document, Play)

    def delete(self, **kwargs):
        object_filter = convert(Play(**kwargs), PlayDocument)
        PlayDocument.objects(**object_filter.to_dict()).delete()
