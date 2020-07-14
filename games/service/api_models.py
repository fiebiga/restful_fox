from typing import Optional

from pydantic import BaseModel


class Game(BaseModel):
    id: Optional[int]
    home: Optional[str]
    away: Optional[str]
    day: Optional[int]
    month: Optional[int]
    time: Optional[int]
    season_type: Optional[str]
    week: Optional[int]
    year: Optional[int]
    final: Optional[int]
    home_score: Optional[int]
    away_score: Optional[int]
    winning_team: Optional[str]
    losing_team: Optional[str]
