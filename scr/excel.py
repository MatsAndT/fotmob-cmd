import xlwt

class Excel():
    line = 1
    row = 7

    def __init__(self, date):
        self.filename = f"{date}.xml"
        self.wb = xlwt.Workbook()
        self.sheet = self.wb.add_sheet(date)

        self.setUp()

    def setUp(self):
        self.sheet.write(0,0, "name")
        self.sheet.write(0,1, "primaryId")
        self.sheet.write(0,2, "time")
        self.sheet.write(0,3, "away")
        self.sheet.write(0,4, "away_score")
        self.sheet.write(0,5, "home")
        self.sheet.write(0,6, "home_scroe")

        # Top Stats
        self.sheet.write(0,9, "Ball possession")
        self.sheet.write(0,10, "Total shots")
        self.sheet.write(0,11, "Chances created")
        self.sheet.write(0,12, "Big chances")
        self.sheet.write(0,13, "Accurate passes")
        self.sheet.write(0,14, "Pass success")
        self.sheet.write(0,15, "Fouls conceded")
        self.sheet.write(0,16, "Corners")
        self.sheet.write(0,17, "Offsides")

        # Shots
        self.sheet.write(0,19, "Shots")
        self.sheet.write(0,20, "Shots on target")
        self.sheet.write(0,21, "Shots off target")
        self.sheet.write(0,22, "Blocked shots")
        self.sheet.write(0,23, "Shots woodwork")
        self.sheet.write(0,24, "Shots inside box")
        self.sheet.write(0,25, "Shots outside box")

        # Accurate passes
        self.sheet.write(0,27, "Accurate passes")
        self.sheet.write(0,28, "Own half")
        self.sheet.write(0,29, "Opposition half")
        self.sheet.write(0,30, "Passes")
        self.sheet.write(0,31, "Pass success")
        self.sheet.write(0,32, "Touches")
        self.sheet.write(0,34, "Long balls")
        self.sheet.write(0,35, "Accurate long balls")
        self.sheet.write(0,36, "Crosses")
        self.sheet.write(0,37, "Accurate crosses")
        self.sheet.write(0,38, "Throws")

        # Duels won
        self.sheet.write(0,39, "Duels won")
        self.sheet.write(0,40, "Duels")
        self.sheet.write(0,41, "Dribbles attempteds")
        self.sheet.write(0,42, "Dribbles succeeded")
        self.sheet.write(0,43, "Tackles attempted")
        self.sheet.write(0,44, "Tackles succeeded")
        self.sheet.write(0,45, "Aerials won")
        self.sheet.write(0,46, "Interceptions")

        # Discipline
        self.sheet.write(0,48, "Yellow cards")
        self.sheet.write(0,49, "Red cards")

        # Keeper
        self.sheet.write(0,51, "Saves")
        self.sheet.write(0,52, "Diving saves")
        self.sheet.write(0,53, "Saves inside box")
        self.sheet.write(0,54, "Acted as sweeper")

        self.sheet.write(0, 56, "matcheId")


    def addMatches(self, name, primaryId, matche):
        self.sheet.write(self.line,0, name)
        self.sheet.write(self.line,1, primaryId)
        self.sheet.write(self.line,2, matche["time"])
        self.sheet.write(self.line,3, matche["away"]["longName"])
        self.sheet.write(self.line,4, matche["away"]["score"])
        self.sheet.write(self.line,5, matche["home"]["longName"])
        self.sheet.write(self.line,6, matche["home"]["score"])
    
    def addTitle(self, title):
        self.sheet.write(0, self.row+1, title)
    
    def moveRow(self):
        self.row += 1

    def addCol(self, data, addedTitle):
        self.row += 1
        if not addedTitle:
            self.sheet.write(self.line, self.row, data)
        else:
            self.sheet.write(self.line, self.row-1, data)
    
    def texiti(self, splits):
        return f"{splits[0]} : {splits[1]}"

    def trySet(self, line, row, stats, top, bun):
        try:
            self.sheet.write(line,row,self.texiti(stats[top]["stats"][bun]["stats"]))
        except:
            pass
    
    def addStats(self, matcheId, stats, exMove):
        move = 0
        # Top Stats
        self.trySet(self.line,9,  stats, 0,0)
        if exMove:
            self.trySet(self.line,10, stats, 0,1)
        else:
            move = -1
            self.sheet.write(self.line, 10, "not")
        self.trySet(self.line,11, stats, 0,2+move)
        self.trySet(self.line,12, stats, 0,3+move)
        self.trySet(self.line,13, stats, 0,4+move)
        self.trySet(self.line,14, stats, 0,5+move)
        self.trySet(self.line,15, stats, 0,6+move)
        self.trySet(self.line,16, stats, 0,7+move)
        self.trySet(self.line,17, stats, 0,8+move)

        # Shots
        self.trySet(self.line,19, stats, 1,0)
        self.trySet(self.line,20, stats, 1,1)
        self.trySet(self.line,21, stats, 1,2)
        self.trySet(self.line,22, stats, 1,3)
        self.trySet(self.line,23, stats, 1,4)
        self.trySet(self.line,24, stats, 1,5)
        self.trySet(self.line,25, stats, 1,6)

        # Accurate passes
        self.trySet(self.line,27, stats, 2,0)
        self.trySet(self.line,28, stats, 2,1)
        self.trySet(self.line,29, stats, 2,2)
        self.trySet(self.line,30, stats, 2,3)
        self.trySet(self.line,31, stats, 2,4)
        self.trySet(self.line,32, stats, 2,5)
        self.trySet(self.line,34, stats, 2,6)
        self.trySet(self.line,35, stats, 2,7)
        self.trySet(self.line,36, stats, 2,8)
        self.trySet(self.line,37, stats, 2,9)
        self.trySet(self.line,38, stats, 2,10)

        # Duels won
        self.trySet(self.line,39, stats, 3,0)
        self.trySet(self.line,40, stats, 3,1)
        self.trySet(self.line,41, stats, 3,2)
        self.trySet(self.line,42, stats, 3,3)
        self.trySet(self.line,43, stats, 3,4)
        self.trySet(self.line,44, stats, 3,5)
        self.trySet(self.line,45, stats, 3,6)
        self.trySet(self.line,46, stats, 3,7)

        # Discipline
        self.trySet(self.line,48, stats, 4,1)
        self.trySet(self.line,49, stats, 4,0)

        # Keeper
        self.trySet(self.line,51, stats, 5,0)
        self.trySet(self.line,52, stats, 5,1)
        self.trySet(self.line,53, stats, 5,2)
        self.trySet(self.line,54, stats, 5,3)

        self.sheet.insert(self.line, 56, matcheId)


    def resetRow(self):
        self.line += 1
        self.row = 7

    def save(self):
        self.wb.save(self.filename)
