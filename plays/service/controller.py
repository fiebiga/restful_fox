from flask import request, make_response

from foxdemo.common.controller import ApiController

from api_models import Play
from service import PlaysService


class PlaysWebController(ApiController):

    path = "/plays"
    service = PlaysService()

    def get(self, id: str = None):
        plays = [play.dict() for play in self.service.get(id=id, **request.args)]
        if id is not None:
            if len(plays) == 0:
                return make_response("{id} does not exist".format(id=id), 404)
            else:
                return plays[0]

        return plays

    def post(self):
        return self.service.create(Play(**request.get_json())).dict()

    def delete(self):
        self.service.delete(**request.args)


