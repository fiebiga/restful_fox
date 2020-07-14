from api_models import Game
from foxdemo.common.converters import Converter
from persistence_models import GameDocument


class GameApiToDocumentConverter(Converter, to_class=Game, from_class=GameDocument):

    def convert(self, source: GameDocument):
        return Game(id=source.game_id,
                    home=source.home,
                    away=source.away,
                    day=source.day,
                    month=source.month,
                    time=source.time,
                    season_type=source.season_type,
                    week=source.week,
                    year=source.year,
                    final=source.final,
                    home_score=source.home_score,
                    away_score=source.away_score,
                    winning_team=source.home if source.home_score > source.away_score else source.away,
                    losing_team=source.away if source.home_score > source.away_score else source.home)


class GameDocumentToApiConverter(Converter, to_class=GameDocument, from_class=Game):

    def convert(self, source: Game):
        return GameDocument(game_id=source.id,
                            home=source.home,
                            away=source.away,
                            day=source.day,
                            month=source.month,
                            time=source.time,
                            season_type=source.season_type,
                            week=source.week,
                            year=source.year,
                            final=source.final,
                            home_score=source.home_score,
                            away_score=source.away_score)