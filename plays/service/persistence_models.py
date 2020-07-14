from mongoengine import StringField, IntField, register_connection

from foxdemo.common.persistence_models import BaseDocument
from foxdemo.common.config import MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASSWORD


class PlayDocument(BaseDocument):
    game_id = IntField()
    play_id = IntField()
    drive_id = IntField()
    quarter = IntField()
    down = IntField()
    time = IntField()
    yrdln = StringField()
    ydstogo = IntField()
    ydsnet = IntField()
    posteam = StringField()
    opponent = StringField()
    description = StringField()
    note = StringField()
    meta = {
        "db_alias": "plays",
        "indexes": [{"fields": ("game_id", "play_id"), "unique": True}]
    }


database = PlayDocument._meta.get("db_alias")
register_connection(database, name=database, db=database,
                    host="{host}:{port}".format(host=MONGO_HOST, port=MONGO_PORT),
                    username=MONGO_USER, password=MONGO_PASSWORD, authentication_source="admin")