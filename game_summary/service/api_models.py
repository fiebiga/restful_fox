from typing import Optional

from pydantic import BaseModel


class GameSummary(BaseModel):
    game_id: Optional[int]
    team: Optional[str]
    opponent: Optional[str]
    total_field_goals: Optional[int]
    total_yards: Optional[int]
    passing_yards: Optional[int]
    rushing_yards: Optional[int]
    penalties: Optional[int]
    penalty_yards: Optional[int]
    turnovers: Optional[int]
    punts: Optional[int]
    punting_yards: Optional[int]
    net_punting_average: Optional[int]