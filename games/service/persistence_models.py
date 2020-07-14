from mongoengine import StringField, IntField, register_connection

from foxdemo.common.persistence_models import BaseDocument
from foxdemo.common.config import MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASSWORD


class GameDocument(BaseDocument):
    game_id = IntField(unique=True)
    home = StringField()
    away = StringField()
    day = IntField()
    month = IntField()
    time = IntField()
    season_type = StringField()
    week = IntField()
    year = IntField()
    final = IntField()
    home_score = IntField()
    away_score = IntField()
    meta = {"db_alias": "games"}


database = GameDocument._meta.get("db_alias")
register_connection(database, name=database, db=database,
                    host="{host}:{port}".format(host=MONGO_HOST, port=MONGO_PORT),
                    username=MONGO_USER, password=MONGO_PASSWORD, authentication_source="admin")