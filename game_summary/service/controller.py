from flask import request, make_response
from foxdemo.common.controller import ApiController

from service import GameSummaryService


class GamesWebController(ApiController):

    path = "/game_summary"
    service = GameSummaryService()

    def get(self, id: str = None):
        models = [model.dict() for model in self.service.get(id=id, **request.args)]
        if id is not None:
            if len(models) == 0:
                return make_response("{id} does not exist".format(id=id), 404)
            else:
                return models[0]

        return models

    def post(self):
        self.service.create()

