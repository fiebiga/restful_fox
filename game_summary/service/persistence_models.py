from mongoengine import StringField, IntField, register_connection

from foxdemo.common.persistence_models import BaseDocument
from foxdemo.common.config import MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASSWORD


class GameSummaryDocument(BaseDocument):
    game_id = IntField()
    team = StringField()
    opponent = StringField()
    totfd = IntField()
    totyds = IntField()
    pyds = IntField()
    ryds = IntField()
    pen = IntField()
    penyds = IntField()
    trnovr = IntField()
    pt = IntField()
    ptyds = IntField()
    ptavg = IntField()
    meta = {
        "db_alias": "game_summary",
        "indexes": [{"fields": ("game_id", "team"), "unique": True}]
    }

database = GameSummaryDocument._meta.get("db_alias")
register_connection(database, name=database, db=database,
                    host="{host}:{port}".format(host=MONGO_HOST, port=MONGO_PORT),
                    username=MONGO_USER, password=MONGO_PASSWORD, authentication_source="admin")