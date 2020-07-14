from flask import request, make_response

from foxdemo.common.controller import ApiController

from api_models import Game
from service import GamesService


class GamesWebController(ApiController):

    path = "/games"
    service = GamesService()

    def get(self, id: str = None):
        games = [game.dict() for game in self.service.get(id=id, **request.args)]
        if id is not None:
            if len(games) == 0:
                return make_response("{id} does not exist".format(id=id), 404)
            else:
                return games[0]

        return games

    def post(self):
        return self.service.create(Game(**request.get_json())).dict()

    def delete(self, id: str = None):
        self.service.delete(id=id, **request.args)

