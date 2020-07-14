from typing import Optional

from pydantic import BaseModel


class Play(BaseModel):
    game_id: Optional[int]
    play_id: Optional[int]
    drive_id: Optional[int]
    quarter: Optional[int]
    down: Optional[int]
    time: Optional[int]
    yard_line: Optional[str]
    yards_to_go: Optional[int]
    yards_net: Optional[int]
    offensive_team: Optional[str]
    defensive_team: Optional[str]
    description: Optional[str]
    note: Optional[str]
