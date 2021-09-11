class Game:
    id: int
    score: int
    name: str
    longName: str

class League:
    ccode: str
    id: int
    primaryId: int
    time: str
    home: Game
    away: Game
    statusId: int
    title: str
