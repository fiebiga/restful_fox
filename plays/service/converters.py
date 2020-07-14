from api_models import Play
from foxdemo.common.converters import Converter
from persistence_models import PlayDocument


class PlayApiToDocumentConverter(Converter, to_class=Play, from_class=PlayDocument):

    def convert(self, source: PlayDocument):
        return Play(game_id=source.game_id,
                    play_id=source.play_id,
                    drive_id=source.drive_id,
                    quarter=source.quarter,
                    down=source.down,
                    time=source.time,
                    yard_line=source.yrdln,
                    yards_to_go=source.ydstogo,
                    yards_net=source.ydsnet,
                    offensive_team=source.posteam,
                    defensive_team=source.opponent,
                    description=source.description,
                    note=source.note)


class PlayDocumentToApiConverter(Converter, to_class=PlayDocument, from_class=Play):

    def convert(self, source: Play):
        return PlayDocument(game_id=source.game_id,
                            play_id=source.play_id,
                            drive_id=source.drive_id,
                            quarter=source.quarter,
                            down=source.down,
                            time=source.time,
                            yrdln=source.yard_line,
                            ydstogo=source.yards_to_go,
                            ydsnet=source.yards_net,
                            posteam=source.offensive_team,
                            opponent=source.defensive_team,
                            description=source.description,
                            note=source.note)