from api_models import GameSummary
from foxdemo.common.converters import Converter
from persistence_models import GameSummaryDocument


class GameApiToDocumentConverter(Converter, to_class=GameSummary, from_class=GameSummaryDocument):

    def convert(self, source: GameSummaryDocument):
        return GameSummary(game_id=source.game_id,
                           team=source.team,
                           opponent=source.opponent,
                           total_field_goals=source.totfd,
                           total_yards=source.totyds,
                           passing_yards=source.pyds,
                           rushing_yards=source.ryds,
                           penalties=source.pen,
                           penalty_yards=source.penyds,
                           turnovers=source.trnovr,
                           punts=source.pt,
                           punting_yards=source.ptyds,
                           net_punting_average=source.ptavg)


class GameDocumentToApiConverter(Converter, to_class=GameSummaryDocument, from_class=GameSummary):

    def convert(self, source: GameSummary):
        return GameSummaryDocument(game_id=source.game_id,
                                   team=source.team,
                                   opponent=source.opponent,
                                   totfd=source.total_field_goals,
                                   totyds=source.total_yards,
                                   pyds=source.passing_yards,
                                   ryds=source.rushing_yards,
                                   pen=source.penalties,
                                   penyds=source.penalty_yards,
                                   trnovr=source.turnovers,
                                   pt=source.punts,
                                   ptyds=source.punting_yards,
                                   ptavg=source.net_punting_average)